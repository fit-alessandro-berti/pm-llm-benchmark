import os.path
import traceback
import threading
import time
from collections import deque
from datetime import datetime, timedelta

import requests
import re
import json
import base64
import sys

from typing import Dict, Any

# the model used to respond to the questions
ANSWERING_MODEL_NAME = "claude-sonnet-4-5-thinking-20250929" if len(sys.argv) < 3 else sys.argv[1]

# judge model
EVALUATING_MODEL_NAME = "grok-4-1-fast-reasoning" if len(sys.argv) < 3 else sys.argv[2]


class RateLimiter:
    """Thread-safe rate limiter for API requests with support for multiple limits."""
    
    def __init__(self, requests_per_minute=60, requests_per_hour=1000, 
                 tokens_per_minute=90000, tokens_per_hour=2000000,
                 max_concurrent=10):
        # Keep hour-level limits at least as large as the minute-level limits to avoid
        # unintentionally throttling long runs (e.g., 900k tokens/min vs 2M tokens/hour
        # caps you at ~500 requests/hr with 4k estimates).
        self.requests_per_minute = requests_per_minute
        self.requests_per_hour = max(requests_per_hour, requests_per_minute * 60)
        self.tokens_per_minute = tokens_per_minute
        self.tokens_per_hour = max(tokens_per_hour, tokens_per_minute * 60)
        self.max_concurrent = max_concurrent

        self.lock = threading.Lock()
        self.request_times = deque()
        self.token_usage = deque()  # (timestamp, token_count, request_id)
        self.concurrent_requests = 0
        self.processing_files = {}  # Track files being processed: {filepath: {thread_id, request_id}}
        self.next_request_id = 0
        
    def can_acquire(self, estimated_tokens=4000, filepath=None):
        """Check if a request can be made based on rate limits."""
        with self.lock:
            now = datetime.now()
            
            # Check if file is already being processed
            if filepath and filepath in self.processing_files:
                return False, "File already being processed"
            
            # Check concurrent requests limit
            if self.concurrent_requests >= self.max_concurrent:
                return False, "Max concurrent requests reached"
            
            # Clean old entries
            minute_ago = now - timedelta(minutes=1)
            hour_ago = now - timedelta(hours=1)
            
            self.request_times = deque([t for t in self.request_times if t > hour_ago])
            self.token_usage = deque([(t, tokens, req_id) for t, tokens, req_id in self.token_usage if t > hour_ago])
            
            # Count requests in windows
            requests_last_minute = sum(1 for t in self.request_times if t > minute_ago)
            requests_last_hour = len(self.request_times)
            
            # Count tokens in windows
            tokens_last_minute = sum(tokens for t, tokens, _ in self.token_usage if t > minute_ago)
            tokens_last_hour = sum(tokens for _, tokens, _ in self.token_usage)
            
            # Check all limits
            if requests_last_minute >= self.requests_per_minute:
                return False, "Requests per minute limit reached"
            if requests_last_hour >= self.requests_per_hour:
                return False, "Requests per hour limit reached"
            if tokens_last_minute + estimated_tokens > self.tokens_per_minute:
                return False, "Tokens per minute limit reached"
            if tokens_last_hour + estimated_tokens > self.tokens_per_hour:
                return False, "Tokens per hour limit reached"
            
            return True, "OK"
    
    def acquire(self, estimated_tokens=4000, filepath=None):
        """Acquire a slot for making a request. Returns (success, reason, request_id)."""
        can_proceed, reason = self.can_acquire(estimated_tokens, filepath)
        if not can_proceed:
            return False, reason, None
        
        with self.lock:
            now = datetime.now()
            request_id = self.next_request_id
            self.next_request_id += 1
            self.request_times.append(now)
            self.token_usage.append((now, estimated_tokens, request_id))
            self.concurrent_requests += 1
            
            if filepath:
                self.processing_files[filepath] = {
                    "thread_id": threading.current_thread().ident,
                    "request_id": request_id
                }
            
            return True, "Acquired", request_id
    
    def release(self, actual_tokens=None, filepath=None, request_id=None):
        """Release the slot after request completion."""
        with self.lock:
            self.concurrent_requests = max(0, self.concurrent_requests - 1)
            
            stored_request_id = request_id
            if filepath and filepath in self.processing_files:
                info = self.processing_files.pop(filepath)
                if stored_request_id is None and isinstance(info, dict):
                    stored_request_id = info.get("request_id")
            
            if stored_request_id is None:
                return
            
            if actual_tokens is not None and self.token_usage:
                for idx in range(len(self.token_usage) - 1, -1, -1):
                    ts, recorded_tokens, req_id = self.token_usage[idx]
                    if req_id == stored_request_id:
                        if recorded_tokens != actual_tokens:
                            self.token_usage[idx] = (ts, actual_tokens, req_id)
                        break
    
    def wait_for_slot(self, estimated_tokens=4000, filepath=None, max_wait=300):
        """Wait until a slot becomes available or timeout."""
        start_time = time.time()
        wait_interval = 1  # Start with 1 second wait
        
        while time.time() - start_time < max_wait:
            acquired, reason, request_id = self.acquire(estimated_tokens, filepath)
            if acquired:
                return True, reason, request_id
            
            # Exponential backoff with jitter
            time.sleep(wait_interval + (time.time() % 0.5))
            wait_interval = min(wait_interval * 1.2, 10)  # Cap at 10 seconds
        
        return False, "Timeout waiting for slot", None
    
    def is_file_processing(self, filepath):
        """Check if a file is currently being processed."""
        with self.lock:
            return filepath in self.processing_files
    
    def get_stats(self):
        """Get current rate limiter statistics."""
        with self.lock:
            now = datetime.now()
            minute_ago = now - timedelta(minutes=1)
            hour_ago = now - timedelta(hours=1)
            
            requests_last_minute = sum(1 for t in self.request_times if t > minute_ago)
            requests_last_hour = len([t for t in self.request_times if t > hour_ago])
            tokens_last_minute = sum(tokens for t, tokens, _ in self.token_usage if t > minute_ago)
            tokens_last_hour = sum(tokens for t, tokens, _ in self.token_usage if t > hour_ago)
            
            return {
                "concurrent_requests": self.concurrent_requests,
                "requests_last_minute": requests_last_minute,
                "requests_last_hour": requests_last_hour,
                "tokens_last_minute": tokens_last_minute,
                "tokens_last_hour": tokens_last_hour,
                "processing_files": list(self.processing_files.keys())
            }


# Global rate limiter instance
RATE_LIMITER = RateLimiter(
    requests_per_minute=100,
    requests_per_hour=20000,
    tokens_per_minute=900000,
    tokens_per_hour=2000000,
    max_concurrent=50
)


class Shared:
    API_KEY = None
    MODEL_NAME = None
    ALIAS_MODEL_NAME = None
    MAX_REQUESTED_TOKENS = 32000
    API_URL = "https://api.x.ai/v1/"
    # API_URL = "https://openrouter.ai/api/v1/"
    # API_URL = "https://generativelanguage.googleapis.com/v1beta/"
    # API_URL = "https://api.openai.com/v1/"
    # API_URL = "http://137.226.117.70:11434/v1/"
    # API_URL = "https://api.deepinfra.com/v1/openai/"
    # API_URL = "https://api.mistral.ai/v1/"
    # API_URL = "https://api.anthropic.com/v1/"
    # API_URL = "https://api.groq.com/openai/v1/"
    # API_URL = "https://api.deepseek.com/"
    # API_URL = "https://api.hyperbolic.xyz/v1/"
    # API_URL = "https://api.perplexity.ai/"
    # API_URL = "https://dashscope-intl.aliyuncs.com/compatible-mode/v1/"
    # API_URL = "https://integrate.api.nvidia.com/v1/"
    SYSTEM_PROMPT = None
    # SYSTEM_PROMPT = "You are a helpful and harmless assistant. You should think step-by-step."
    # SYSTEM_PROMPT = "You are a helpful and harmless assistant."
    # SYSTEM_PROMPT = "detailed thinking on"
    # SYSTEM_PROMPT = "Enable deep thinking subroutine."
    TRIAL_CHANGE_EVALUATION_LRM = False
    CUSTOM_TEMPERATURE = None
    #CUSTOM_TEMPERATURE = 0.6
    TRIAL_SEVERE_EVALUATION = True
    ANTHROPIC_THINKING_TOKENS = 16000
    ANTHROPIC_THINKING_TOKENS = None
    PAYLOAD_REASONING_EFFORT = "low"
    PAYLOAD_REASONING_EFFORT = None
    TOOLS_PAYLOAD = None
    ADDED_TO_PAYLOAD = None
    ADDED_TO_PROMPT = " /no_think"
    ADDED_TO_PROMPT = None


MODELS_DICT = {
    "openai": {
        "api_url": "https://api.openai.com/v1/",
        "api_key": "sk-",
        "models": {
            "gpt-4o-2024-11-20", "gpt-3.5-turbo",
            "gpt-4-turbo-2024-04-09", "o1-2024-12-17", "gpt-4o-mini-2024-07-18",
            "o3-mini-2025-01-31", "gpt-4.1-2025-04-14", "gpt-4.1-mini-2025-04-14",
            "gpt-4.1-nano-2025-04-14", "o3-2025-04-16", "gpt-4o-2024-05-13",
            "o3-pro-2025-06-10", "gpt-5-nano-2025-08-07", "gpt-5-mini-2025-08-07",
            "gpt-5-2025-08-07", "gpt-5-pro-2025-10-06"
        }
    },
    "google": {
        "api_url": "https://generativelanguage.googleapis.com/v1beta/",
        "api_key": "sk-",
        "models": {
            "gemini-1.5-pro-002", "gemini-2.0-flash", "gemini-2.0-flash-lite",
            "gemma-3n-e4b-it", "gemini-3-pro-preview"
        }
    },
    "claude": {
        "api_url": "https://api.anthropic.com/v1/",
        "api_key": "sk-",
        "models": {
            "claude-3-7-sonnet-20250219",
            "claude-4-opus-20250514",
            "claude-4-sonnet-20250514",
            "claude-opus-4-1-20250805",
            "claude-sonnet-4-5-20250929",
            "claude-haiku-4-5-20251001",
            "claude-opus-4-5-20251101"
        }
    },
    "mistral": {
        "api_url": "https://api.mistral.ai/v1/",
        "api_key": "sk-",
        "models": {
            "pixtral-large-2411", "pixtral-12b-2409", "ministral-3b-2410",
            "mistral-large-2411", "mistral-small-2506",
            "mistral-medium-2505", "devstral-medium-2507", "mistral-medium-2508",
            "magistral-small-2509", "magistral-medium-2509", "ministral-3b-2512",
            "ministral-8b-2512", "ministral-14b-2512", "mistral-large-2512"
        }
    },
    "grok": {
        "api_url": "https://api.x.ai/v1/",
        "api_key": "sk-",
        "models": {
            "grok-2-1212", "grok-3", "grok-4-0709", "grok-code-fast-1",
            "grok-4-fast-reasoning", "grok-4-fast-non-reasoning",
            "grok-4-1-fast-reasoning", "grok-4-1-fast-non-reasoning",
        }
    },
    "deepinfra": {
        "api_url": "https://api.deepinfra.com/v1/openai/",
        "api_key": "sk-",
        "models": {
            "nvidia/Llama-3.1-Nemotron-70B-Instruct",
            "microsoft/phi-4", "microsoft/WizardLM-2-8x22B",
            "deepseek-ai/DeepSeek-V3-0324", "deepseek-ai/DeepSeek-V3", "deepseek-ai/DeepSeek-R1",
            "Qwen/Qwen3-32B", "Qwen/Qwen3-14B",
            "deepseek-ai/DeepSeek-R1-0528", "deepseek-ai/DeepSeek-V3.1"
        }
    },
    "ollama_local": {
        "api_url": "http://137.226.117.70:11434/v1/",
        "api_key": "sk-",
        "models": {
            "falcon3:10b-instruct-q8_0", "falcon3:7b-instruct-q8_0",
            "falcon3:3b-instruct-q8_0",
            "olmo2:7b-1124-instruct-q8_0", "exaone-deep:32b-fp16",
            "exaone-deep:7.8b-fp16", "exaone-deep:2.4b-fp16",
            "gemma3:27b-it-q8_0", "gemma3:12b-it-q8_0", "gemma3:4b-it-q8_0",
            "gemma3:1b-it-q8_0",
            "granite3.3", "qwen3:0.6b", "qwen3:1.7b", "qwen3:4b", "qwen3:8b",
            "phi4-mini-reasoning", "phi4-reasoning", "phi4-reasoning:plus",
            "qwen3:4b-instruct-2507-q8_0", "qwen3:4b-thinking-2507-q8_0",
            "granite4:micro", "granite4:micro-h", "granite4:tiny-h", "granite4:small-h",
            "ibm/granite4:350m-h", "ibm/granite4:1b-h"
        }
    },
    "qwen": {
        "api_url": "https://dashscope-intl.aliyuncs.com/compatible-mode/v1/",
        "api_key": "sk-",
        "models": {}
    },
    "nvidia": {
        "api_url": "https://integrate.api.nvidia.com/v1/",
        "api_key": "sk-",
        "models": {
        }
    },
    "perplexity": {
        "api_url": "https://api.perplexity.ai/",
        "api_key": "sk-",
        "models": {
            "sonar-reasoning-pro", "sonar-pro", "r1-1776"
        }
    },
    "groq": {
        "api_url": "https://api.groq.com/openai/v1/",
        "api_key": "sk-",
        "models": {

        }
    },
    "openrouter": {
        "api_url": "https://openrouter.ai/api/v1/",
        "api_key": "sk-",
        "models": {
            "meta-llama/llama-4-scout", "meta-llama/llama-4-maverick",
            "inception/mercury", "baidu/ernie-4.5-300b-a47b",
            "qwen/qwen3-coder",
            "z-ai/glm-4.5", "z-ai/glm-4.5-air", "qwen/qwen3-30b-a3b-instruct-2507",
            "ai21/jamba-large-1.7", "ai21/jamba-mini-1.7",
            "moonshotai/kimi-k2-0905", "qwen/qwen3-max",
            "qwen/qwen3-next-80b-a3b-instruct", "qwen/qwen3-next-80b-a3b-thinking",
            "openai/gpt-5-codex", "z-ai/glm-4.6", "baidu/ernie-4.5-21b-a3b-thinking",
            "liquid/lfm-2.2-6b", "liquid/lfm2-8b-a1b",
            "moonshotai/kimi-k2-thinking",
            "moonshotai/kimi-linear-48b-a3b-instruct",
            "allenai/olmo-3-7b-think",
            "allenai/olmo-3-7b-instruct", "allenai/olmo-3-32b-think",
            "arcee-ai/trinity-mini", "amazon/nova-2-lite-v1"
        }
    },
    "manual": {
        "api_url": "http://0.0.0.0:1000/v1/",
        "api_key": "sk-",
        "models": {
            "claude-3-5-sonnet-20241022": {
                "provider": "claude",
                "base_model": "claude-3-5-sonnet-20241022",
                "max_tokens": 8192
            },
            "claude-3-opus-20240229": {
                "provider": "claude",
                "base_model": "claude-3-5-sonnet-20241022",
                "max_tokens": 4096
            },
            "claude-3-5-haiku-20241022": {
                "provider": "claude",
                "base_model": "claude-3-5-sonnet-20241022",
                "max_tokens": 8192
            },
            "nvidia/llama-3.3-nemotron-super-49b-v1-thinkenab": {
                "provider": "nvidia",
                "base_model": "nvidia/llama-3.3-nemotron-super-49b-v1",
                "system_prompt": "detailed thinking on"
            },
            "o3-mini-20250131-HIGH": {
                "provider": "openai",
                "base_model": "o3-mini-2025-01-31",
                "reasoning_effort": "high"
            },
            "o4-mini-2025-04-16-HIGH": {
                "provider": "openai",
                "base_model": "o4-mini-2025-04-16",
                "reasoning_effort": "high"
            },
            "gpt-5-2025-08-07-HIGH": {
                "provider": "openai",
                "base_model": "gpt-5-2025-08-07",
                "reasoning_effort": "high"
            },
            "gpt-5.1-2025-11-13-HIGH": {
                "provider": "openai",
                "base_model": "gpt-5.1-2025-11-13",
                "reasoning_effort": "high"
            },
            "o3-pro-2025-06-10-HIGH": {
                "provider": "openai",
                "base_model": "o3-pro-2025-06-10",
                "reasoning_effort": "high"
            },
            "o3-2025-04-16-search": {
                "provider": "openai",
                "base_model": "o3-2025-04-16",
                "tools": [{"type": "web_search"}]
            },
            "o3-2025-04-16-codeinterpr": {
                "provider": "openai",
                "base_model": "o3-2025-04-16",
                "tools": [{"type": "code_interpreter", "container": {"type": "auto"}}]
            },
            "o3-pro-2025-06-10-search": {
                "provider": "openai",
                "base_model": "o3-pro-2025-06-10",
                "tools": [{"type": "web_search"}]
            },
            "o3-pro-2025-06-10-codeinterpr": {
                "provider": "openai",
                "base_model": "o3-pro-2025-06-10",
                "tools": [{"type": "code_interpreter", "container": {"type": "auto"}}]
            },
            "o4-mini-2025-04-16-search-HIGH": {
                "provider": "openai",
                "base_model": "o4-mini-2025-04-16",
                "tools": [{"type": "web_search"}],
                "reasoning_effort": "high"
            },
            "o4-mini-2025-04-16-codeinterpr-HIGH": {
                "provider": "openai",
                "base_model": "o4-mini-2025-04-16",
                "tools": [{"type": "code_interpreter", "container": {"type": "auto"}}],
                "reasoning_effort": "high"
            },
            "chatgpt-4o-latest-2025-03-26": {
                "provider": "openai",
                "base_model": "chatgpt-4o-latest"
            },
            "gpt-5-chat-latest-2025-08-22": {
                "provider": "openai",
                "base_model": "gpt-5-chat-latest"
            },
            "Qwen-3-32B-nothink": {
                "provider": "deepinfra",
                "base_model": "Qwen/Qwen3-32B",
                "added_to_prompt": " /no_think"
            },
            "Qwen-3-14B-nothink": {
                "provider": "deepinfra",
                "base_model": "Qwen/Qwen3-14B",
                "added_to_prompt": " /no_think"
            },
            "nousresearch/hermes-4-70b": {
                "provider": "openrouter",
                "base_model": "nousresearch/hermes-4-70b",
                "added_to_payload": {"reasoning": {"enabled": True}}
            },
            "nvidia/nemotron-nano-9b-v2-thinking": {
                "provider": "openrouter",
                "base_model": "nvidia/nemotron-nano-9b-v2",
                "added_to_payload": {"reasoning": {"enabled": True}}
            },
            "nvidia/llama-3.3-nemotron-super-49b-v1.5-thinking": {
                "provider": "openrouter",
                "base_model": "nvidia/llama-3.3-nemotron-super-49b-v1.5",
                "added_to_payload": {"reasoning": {"enabled": True}}
            },
            "deepseek/deepseek-v3.2-thinking": {
                "provider": "openrouter",
                "base_model": "deepseek/deepseek-v3.2",
                "added_to_payload": {"reasoning": {"enabled": True}}
            },
            "deepseek/deepseek-v3.2-speciale-thinking": {
                "provider": "openrouter",
                "base_model": "deepseek/deepseek-v3.2-speciale",
                "added_to_payload": {"reasoning": {"enabled": True}}
            },
            "prime-intellect/intellect-3": {
                "provider": "openrouter",
                "base_model": "prime-intellect/intellect-3",
                "added_to_payload": {"reasoning": {"enabled": True}}
            },
            "claude-3-7-sonnet-thinkhigh-20250219": {
                "provider": "claude",
                "base_model": "claude-3-7-sonnet-20250219",
                "thinking_tokens": 98304
            },
            "claude-4-sonnet-thinking-20250514": {
                "provider": "claude",
                "base_model": "claude-4-sonnet-20250514",
                "thinking_tokens": 32000,
            },
            "claude-sonnet-4-5-thinking-20250929": {
                "provider": "claude",
                "base_model": "claude-sonnet-4-5-20250929",
                "thinking_tokens": 32000,
            },
            "claude-4-opus-thinking-20250514": {
                "provider": "claude",
                "base_model": "claude-4-opus-20250514",
                "thinking_tokens": 16000,
                "max_tokens": 16000
            },
            "claude-opus-4-1-thinking-20250805": {
                "provider": "claude",
                "base_model": "claude-opus-4-1-20250805",
                "thinking_tokens": 16000,
                "max_tokens": 16000
            },
            "claude-opus-4-5-thinking-20251101": {
                "provider": "claude",
                "base_model": "claude-opus-4-5-20251101",
                "thinking_tokens": 16000,
                "max_tokens": 16000
            },
            "gemini-2.5-flash-09-2025-nothink": {
                "provider": "google",
                "base_model": "gemini-2.5-flash-preview-09-2025",
                "thinking_tokens": 0
            },
            "gemini-2.5-flash-09-2025-thinkhigh": {
                "provider": "google",
                "base_model": "gemini-2.5-flash-preview-09-2025",
                "thinking_tokens": 24576
            },
            "gemini-2.5-flash-lite-09-2025-thinkhigh": {
                "provider": "google",
                "base_model": "gemini-2.5-flash-lite-preview-09-2025",
                "thinking_tokens": 24576
            },
            "gemini-2.5-flash-lite-09-2025-nothink": {
                "provider": "google",
                "base_model": "gemini-2.5-flash-lite-preview-09-2025",
                "thinking_tokens": 0
            },
            "gemini-2.5-flash-nothink": {
                "provider": "google",
                "base_model": "gemini-2.5-flash",
                "thinking_tokens": 0
            },
            "gemini-2.5-flash-thinkhigh": {
                "provider": "google",
                "base_model": "gemini-2.5-flash",
                "thinking_tokens": 24576
            },
            "gemini-2.5-flash-lite-thinkhigh": {
                "provider": "google",
                "base_model": "gemini-2.5-flash-lite-preview-06-17",
                "thinking_tokens": 24576
            },
            "gemini-2.5-flash-lite-nothink": {
                "provider": "google",
                "base_model": "gemini-2.5-flash-lite-preview-06-17",
                "thinking_tokens": 0
            },
            "gemini-2.5-pro-thinklow": {
                "provider": "google",
                "base_model": "gemini-2.5-pro",
                "thinking_tokens": 2048
            },
            "gemini-2.5-pro-thinkhigh": {
                "provider": "google",
                "base_model": "gemini-2.5-pro",
                "thinking_tokens": 32768
            },
            "nvidia/llama-3.1-nemotron-ultra-253b-v1-thinkenab": {
                "provider": "nvidia",
                "base_model": "nvidia/llama-3.1-nemotron-ultra-253b-v1",
                "system_prompt": "detailed thinking on"
            }
        }
    }
}


def is_excluded_from_table(model_name):
    patterns = []
    for p in patterns:
        if p.lower() in model_name.lower():
            return True
    return False


def get_ordered_references_llms(base_path="."):
    try:
        from utils import overall_table
        output, all_jsons, ordered_llms = overall_table.execute(os.path.join(base_path, "evaluation-grok41-fast"),
                                                                None, include_closed_source=True, require_vision=False,
                                                                leaderboard_title="Overall Leaderboard")
    except:
        traceback.print_exc()
        ordered_llms = []

    referenced_llms = set()
    for provider in MODELS_DICT:
        info = MODELS_DICT[provider]
        referenced_llms = referenced_llms.union(info["models"])
    referenced_llms = {x for x in referenced_llms if not is_excluded_from_table(x)}
    referenced_llms = [clean_model_name(x) for x in referenced_llms if
                       clean_model_name(x) not in ordered_llms]

    return ordered_llms, referenced_llms


def is_visual_model(model_name):
    patterns = ["qwen2-vl", "qwen2.5-vl", "qwen-vl", "pixtral", "gpt-4o", "gpt-4-turbo", "gpt-4.5", "Llama-3.2-11B", "Llama-3.2-90B", "gemini-", "claude-", "grok-vision-beta", "multimodal-", "gemma3:4b", "gemma-3-4b", "gemma3:12b", "gemma-3-12b", "gemma3:12b", "gemma3:27b", "mistral-small-2503", "mistral-small-2506", "-omni-", "llama-4", "quasar", "optimus", "gpt-4.1", "o3-2", "o3-pro-2", "o4-mini-2", "mistral-medium", "grok-4", "horizon", "gpt-5", "sonoma", "polaris-alpha", "sherlock", "ministral-3b-2512", "ministral-8b-2512", "ministral-14b-2512", "mistral-large-2512"]

    for p in patterns:
        if p.lower() in model_name.lower():
            if "haiku" not in model_name.lower():
                return True

    return False


def is_open_source(m_name):
    m_name = m_name.lower()
    patterns = ["gpt-4", "gpt-3.5", "claude", "gemini", "o1-", "o3-", "ministral-3b", "grok", "sonus", "2.5-plus", "2.5-turbo", "2.5-max", "sonar-", "quasar", "optimus", "o3-2", "o4-mini-2", "gpt-5", "horizon", "cypher", "mistral-medium", "magistral-medium", "sonoma"]

    for p in patterns:
        if p in m_name:
            return False

    if "qwen3-max" in m_name:
        return False

    return True


def is_large_reasoning_model(m_name):
    m_name = m_name.lower()
    patterns = ["o1-", "o3-", "-thinking-", "qwq", "marco", "deepseek-r1", "reason", "r1-1776", "exaone", "gemini-2.5-pro", "gemini-3", "-thinkenab", "grok-3-mini", "-think", "cogito", "o3-2", "o4-mini-2", "glm", "qwen3", "phi4-mini-reasoning", "phi4-reasoning", "magistral", "grok-4", "gpt-oss", "gpt-5", "-reasoner", "grok-code", "nous", "olmo-3-32b-think", "olmo-3-7b-think", "trinity-mini", "intellect-3"]

    for p in patterns:
        if p in m_name:
            if (not "qwen3" in m_name) or ("qwen3" in m_name and not ("nstruct" in m_name or "coder" in m_name or "max" in m_name)):
                if not ("chat" in m_name or "none" in m_name):
                    return True

    return False


def force_custom_evaluation_lrm(answering_model_name):
    model_name = answering_model_name.lower()
    for p in ["qwq", "qvq", "deepseek-r1-distill", "deepseek-ai", "deepseek-r1-zero", "grok-3-beta-thinking", "deepseek-r1-dynamic-quant", "r1-1776", "sonar-reasoning", "exaone", "671b-hb", "-thinkenab", "grok-3-mini", "cogito", "qwen3", "phi4-mini-reasoning", "phi4-reasoning", "magistral", "gpt-oss", "-reasoner", "grok-code", "nous", "qwen3-next-80b-a3b-thinking", "nemotron-nano-9b-v2-thinking", "deepseek-v3.2-exp-thinking", "deepseek-v3.2-thinking", "deepseek-v3.2-speciale-thinking", "nemotron-super-49b-v1.5-thinking", "kimi-k2-thinking", "olmo-3-32b-think", "olmo-3-7b-think", "trinity-mini", "intellect-3"]:
        if p in model_name and not ("deepseek-v3" in model_name and not ("-reasoner" in model_name or "-thinking" in model_name)):
            if (not "qwen3" in model_name) or ("qwen3" in model_name and not ("nstruct" in model_name or "coder" in model_name or "max" in model_name)):
                return True
    return False


def set_api_key(type_key):
    if type_key == "answer":
        answering_api_key_path = "answering_api_key.txt" if os.path.exists(
            "answering_api_key.txt") else "../answering_api_key.txt"
        Shared.API_KEY = open(answering_api_key_path, "r").read().strip()
        Shared.MODEL_NAME = ANSWERING_MODEL_NAME
        Shared.ALIAS_MODEL_NAME = Shared.MODEL_NAME
    else:
        #judge_api_key_path = "judge_api_key.txt" if os.path.exists("judge_api_key.txt") else "../judge_api_key.txt"
        #Shared.API_KEY = open(judge_api_key_path, "r").read().strip()
        Shared.API_KEY = os.environ["GROK_API_KEY"]
        Shared.MODEL_NAME = EVALUATING_MODEL_NAME
        Shared.ALIAS_MODEL_NAME = Shared.MODEL_NAME


def strip_non_unicode_characters(text):
    # Define a pattern that matches all valid Unicode characters.
    pattern = re.compile(r'[^\u0000-\uFFFF]', re.UNICODE)
    # Replace characters not matching the pattern with an empty string.
    cleaned_text = pattern.sub('', text)
    cleaned_text = cleaned_text.encode('cp1252', errors='ignore').decode('cp1252')

    return cleaned_text


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def callback_write(response_message, target_path):
    if response_message and response_message is not None:
        response_message = strip_non_unicode_characters(response_message)

        if response_message:
            F = open(target_path, "w")
            F.write(response_message)
            F.close()


def get_llm_specific_settings() -> Dict[str, Any]:
    model_name = Shared.MODEL_NAME.lower()
    options = {}

    if "api.mistral" not in Shared.API_URL:
        if "mistral" in model_name:
            options["temperature"] = 0.3
            if "7b" in model_name:
                options["temperature"] = 1.0

    if "deepinfra" in Shared.API_URL:
        max_tokens = Shared.MAX_REQUESTED_TOKENS if Shared.MAX_REQUESTED_TOKENS is not None else 65536
        options["max_tokens"] = max_tokens

    if "qwen3" in model_name.lower():
        options["temperature"] = 0.6

    if "x-ai/grok-4-fast" in model_name:
        options["reasoning"] = {"enabled": True}
        #print(options)

    if "qwen3" in model_name.lower():
        options["top_p"] = 0.95
        options["top_k"] = 0.20
        options["min_p"] = 0

    if Shared.CUSTOM_TEMPERATURE is not None:
        options["temperature"] = Shared.CUSTOM_TEMPERATURE

    if options:
        #print(options)
        pass

    return options


def dump_payload(payload, target_file):
    if "answers" in target_file:
        target_file = target_file.replace("answers", "json_payload")
        # print(target_file)

        try:
            json.dump(payload, open(target_file, "w"), indent=2)
        except:
            print("payload dumping failed")


def dump_response(response, target_file):
    if "answers" in target_file:
        target_file = target_file.replace("answers", "json_resp")
        # print(target_file)

        try:
            json.dump(response, open(target_file, "w"), indent=2)
        except:
            print("response dumping failed")


def query_text_simple_openai_new(question, api_url, target_file):
    complete_url = api_url
    if not complete_url.endswith("/"):
        complete_url += "/"
    complete_url += "responses"

    payload = {
        "model": Shared.MODEL_NAME,
        "input": question
    }

    if Shared.PAYLOAD_REASONING_EFFORT:
        payload["reasoning"] = {"effort": Shared.PAYLOAD_REASONING_EFFORT}

    if Shared.SYSTEM_PROMPT is not None:
        payload["instructions"] = Shared.SYSTEM_PROMPT

    if Shared.TOOLS_PAYLOAD is not None:
        payload["tools"] = Shared.TOOLS_PAYLOAD

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {Shared.API_KEY}"
    }

    dump_payload(payload, target_file)

    response = requests.post(complete_url, headers=headers, json=payload, timeout=30*60)
    if response.status_code != 200:
        print(response)
        print(response.status_code)
        print(response.text)

    response = response.json()

    dump_response(response, target_file)

    return response["output"][-1]["content"][0]["text"]


def query_text_simple_generic(question, api_url, target_file):
    """
    Generic function to query LLM endpoints:
      - OLLAMA (if "11434" is in api_url)
      - Otherwise, standard OpenAI /v1/chat/completions (optionally streaming)
    """

    # Usually OpenAI's Chat endpoint is /v1/chat/completions
    # If your base api_url doesn't already end with '/v1/',
    # you can do something like:
    complete_url = api_url
    if not complete_url.endswith("/"):
        complete_url += "/"
    complete_url += "chat/completions"  # might be /v1/chat/completions, depending on your setup

    messages = [{"role": "user", "content": question}]

    if Shared.SYSTEM_PROMPT is not None:
        messages = [{"role": "system", "content": Shared.SYSTEM_PROMPT}] + messages

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {Shared.API_KEY}"
    }

    # Base payload for OpenAI-like
    payload = {
        "model": Shared.MODEL_NAME,
        "messages": messages,
    }

    if Shared.TOOLS_PAYLOAD is not None:
        raise Exception("fail")

    if Shared.ADDED_TO_PAYLOAD is not None:
        payload.update(Shared.ADDED_TO_PAYLOAD)

        #print(payload)

    # Check if "11434" in api_url (OLLAMA case)
    if "11434" in api_url:
        # OLLAMA with streaming enabled
        options = {"num_ctx": Shared.MAX_REQUESTED_TOKENS}
        options.update(get_llm_specific_settings())

        # Include "stream": True in the payload
        sent_text = question

        if Shared.SYSTEM_PROMPT is not None:
            sent_text = Shared.SYSTEM_PROMPT + "\n\nUser: " + sent_text

        payload = {
            "model": Shared.MODEL_NAME,
            "prompt": sent_text,
            "options": options,
            "stream": True  # ask for a streamed response
        }

        # OLLAMA’s generate endpoint
        ollama_url = complete_url.replace("v1/chat/completions", "api/generate")

        response_message = ""
        chunk_count = 0

        # Use stream=True to process response chunks as they arrive
        with requests.post(ollama_url, headers=headers, json=payload, stream=True) as resp:
            # Iterate over each line in the streamed response
            for line in resp.iter_lines():
                if not line:
                    continue  # skip empty lines

                try:
                    # Each line should be a JSON-encoded object with a "response" field
                    data = json.loads(line.decode("utf-8"))
                except json.JSONDecodeError:
                    # If the line is not valid JSON, skip it
                    continue

                # Append the chunk's text to our overall response message

                chunk = data.get("response", "")
                response_message += chunk
                chunk_count += 1
                #print(chunk_count)

                if chunk_count % 10 == 0:
                    #print(target_file, chunk_count)
                    #print(chunk_count, len(response_message), response_message.replace("\n", " ").replace("\r", "").strip())
                    pass

    else:
        # Non-OLLAMA (OpenAI or OpenAI-compatible endpoint)
        payload.update(get_llm_specific_settings())

        #print(payload)

        # For debugging/logging
        dump_payload(payload, target_file)

        # Decide if we want streaming
        streaming_enabled = False
        streaming_enabled = Shared.PAYLOAD_REASONING_EFFORT is None
        if "stral" in Shared.MODEL_NAME.lower():
            streaming_enabled = False

        if streaming_enabled:
            payload["stream"] = True
            response_message = ""
            thinking_content = ""

            chunk_count = 0

            # We add stream=True to requests so we can iterate over chunks
            with requests.post(complete_url, headers=headers, json=payload, stream=True) as resp:
                #print(resp)
                #print(resp.status_code)
                #print(resp.text)

                for line in resp.iter_lines():
                    if not line:
                        continue
                    decoded_line = line.decode("utf-8")

                    # OpenAI-style streaming lines begin with "data: "
                    if decoded_line.startswith("data: "):
                        data_str = decoded_line[len("data: "):].strip()
                        if data_str == "[DONE]":
                            # End of stream
                            break
                        try:
                            data_json = json.loads(data_str)
                            if "choices" in data_json:
                                # Each chunk has a delta with partial content
                                #print(data_json)
                                delta = data_json["choices"][0]["delta"]
                                chunk_content = delta.get("content", "")
                                chunk_reasoning_content = ""
                                if "reasoning_content" in delta:
                                    chunk_reasoning_content = delta.get("reasoning_content", "")
                                elif "reasoning" in delta:
                                    chunk_reasoning_content = delta.get("reasoning", "")

                                #print(chunk_reasoning_content)

                                if chunk_content:
                                    response_message += chunk_content
                                    chunk_count += 1
                                    #print(chunk_count)
                                    if chunk_count % 10 == 0:
                                        #print(target_file, chunk_count, len(response_message))
                                        #print(target_file, chunk_count, len(response_message), response_message.replace("\n", " ").replace("\r", "").strip())
                                        pass
                                elif chunk_reasoning_content:
                                    thinking_content += chunk_reasoning_content
                                    chunk_count += 1
                                    #print("thinking", chunk_count)
                                    if chunk_count % 10 == 0:
                                        #print("thinking", target_file, chunk_count, len(thinking_content))
                                        #print("thinking", chunk_count, len(thinking_content), thinking_content.replace("\n", " ").replace("\r", "").strip())
                                        pass
                        except json.JSONDecodeError:
                            # Possibly a keep-alive or incomplete chunk
                            traceback.print_exc()

            if thinking_content:
                response_message = ["<think>", thinking_content, "</think>", response_message]
                response_message = "\n".join(response_message)

            # Optionally store the final result so you can debug
            final_response = {
                "choices": [
                    {"message": {"content": response_message}}
                ]
            }
            dump_response(final_response, target_file)

        else:
            if Shared.PAYLOAD_REASONING_EFFORT:
                payload["reasoning_effort"] = Shared.PAYLOAD_REASONING_EFFORT

            # Non-streaming call
            response = requests.post(complete_url, headers=headers, json=payload)

            response = response.json()

            try:
                dump_response(response, target_file)
                message = response["choices"][0]["message"]

                response_message = message["content"]

                if isinstance(response_message, list) and len(response_message) == 2 and isinstance(response_message[0], dict) and isinstance(response_message[1], dict):
                    if response_message[0]["type"] == "thinking" and response_message[1]["type"] == "text":
                        response_message = "<think>\n" + response_message[0]["thinking"][-1]["text"].strip() + "\n</think>\n\n" + response_message[1]["text"].strip()
                elif "reasoning_content" in message:
                    response_message = "<think>\n" + message["reasoning_content"] + "\n</think>\n\n" + response_message.strip()

            except Exception as e:
                print(response)
                print(response.status_code)

                raise Exception(str(response))

    return response_message



def query_text_simple_anthropic(question, api_url, target_file):
    complete_url = api_url + "messages"

    messages = [{"role": "user", "content": question}]

    headers = {
        "content-type": "application/json",
        "anthropic-version": "2023-06-01",
        "anthropic-beta": "output-128k-2025-02-19",
        "x-api-key": Shared.API_KEY
    }

    payload = {
        "model": Shared.MODEL_NAME,
        "max_tokens": Shared.MAX_REQUESTED_TOKENS,
        "messages": messages
    }

    if Shared.ANTHROPIC_THINKING_TOKENS is not None:
        payload["thinking"] = {"type": "enabled", "budget_tokens": Shared.ANTHROPIC_THINKING_TOKENS}
        payload["max_tokens"] += Shared.ANTHROPIC_THINKING_TOKENS
        payload["max_tokens"] = min(64000, payload["max_tokens"])

    dump_payload(payload, target_file)

    response_message = ""

    streaming_enabled = False

    if streaming_enabled:
        payload["stream"] = True
        chunk_count = 0

        # Make a streaming POST request
        with requests.post(complete_url, headers=headers, json=payload, stream=True) as resp:
            for line in resp.iter_lines():
                if not line:
                    continue
                # Decode the line
                decoded_line = line.decode("utf-8").strip()

                # Optionally check for a stream end marker (Anthropic may send "[DONE]")
                if "message_stop" in decoded_line:
                    break

                if "message_start" in decoded_line:
                    continue

                try:
                    decoded_line = decoded_line.split("data: ")[-1].strip()
                    if "text" in decoded_line:
                        chunk = decoded_line.split('"text":"')[-1].split('"')[0].replace("\\n", "\n")
                        response_message += chunk
                        chunk_count += 1
                        #print(chunk_count)

                        # You could add logging or progress updates here if desired
                        if chunk_count % 10 == 0:
                            #print(chunk_count, len(response_message), response_message)
                            pass

                except json.JSONDecodeError:
                    # Skip any malformed lines
                    traceback.print_exc()
                    continue
    else:
        with requests.post(complete_url, headers=headers, json=payload) as resp:
            if resp.status_code != 200:
                print(resp)
                print(resp.text)
                print(resp.status_code)
            respj = resp.json()
            response_message = respj["content"][-1]["text"]

    # Optionally, dump the final aggregated response for debugging
    final_response = {"content": [{"text": response_message}]}
    dump_response(final_response, target_file)

    return response_message


def query_text_simple_google(question, api_url, target_file):
    complete_url = api_url + "models/" + Shared.MODEL_NAME + ":generateContent?key=" + Shared.API_KEY

    headers = {
        "Content-Type": "application/json",
    }

    payload = {
        "contents": [
            {"parts": [
                {"text": question}
            ]}
        ]
    }

    if "gemini-2.5" in Shared.MODEL_NAME:
        payload["generationConfig"] = {
            "thinkingConfig": {
                "thinkingBudget": Shared.ANTHROPIC_THINKING_TOKENS if Shared.ANTHROPIC_THINKING_TOKENS is not None else 8192
            }
        }

    dump_payload(payload, target_file)

    response = requests.post(complete_url, headers=headers, json=payload).json()
    dump_response(response, target_file)

    try:
        response_message = response["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        raise Exception(str(response))

    return response_message


def _load_prompt_text(question_path, explicit_text):
    if explicit_text is not None:
        return explicit_text
    if not question_path:
        return ""
    try:
        with open(question_path, "r", encoding="utf-8") as handler:
            return handler.read()
    except Exception:
        try:
            with open(question_path, "r") as handler:
                return handler.read()
        except Exception:
            return ""


def _estimate_text_tokens(text):
    if not text:
        return 0
    return max(1, len(text) // 4)


def _estimate_pre_request_tokens(prompt_text, fallback, extra_tokens=0):
    prompt_tokens = _estimate_text_tokens(prompt_text)
    if prompt_tokens == 0:
        return fallback
    response_guess = min(max(prompt_tokens // 2, 512), 4096)
    total = prompt_tokens + response_guess + extra_tokens
    buffer = max(256, int(total * 0.15))
    estimate = total + buffer
    if fallback:
        estimate = max(int(fallback * 0.5), estimate)
    return estimate


def _estimate_actual_tokens(prompt_text, response_text, fallback, extra_tokens=0):
    prompt_tokens = _estimate_text_tokens(prompt_text)
    response_tokens = _estimate_text_tokens(response_text)
    total = prompt_tokens + response_tokens + extra_tokens
    if total == 0:
        return fallback
    buffer = max(128, int(total * 0.1))
    return total + buffer


def query_text_simple_with_rate_limit(question_path, target_file, callback, question=None, 
                                      use_rate_limit=True, estimated_tokens=4000):
    """Wrapper for query_text_simple with rate limiting support."""
    filepath = target_file if use_rate_limit else None
    prompt_text = _load_prompt_text(question_path, question)
    effective_estimate = estimated_tokens or 0
    if use_rate_limit:
        if not effective_estimate:
            effective_estimate = 4000
        effective_estimate = _estimate_pre_request_tokens(prompt_text, effective_estimate)
        acquired, reason, request_id = RATE_LIMITER.wait_for_slot(effective_estimate, filepath, max_wait=300)
        if not acquired:
            raise Exception(f"Failed to acquire rate limit slot: {reason}")
    else:
        request_id = None
        if not effective_estimate:
            effective_estimate = 4000
    response_message = None
    try:
        # Call the original function
        response_message = query_text_simple(question_path, target_file, callback, question)
        return response_message
    finally:
        if use_rate_limit and request_id is not None:
            actual_tokens = _estimate_actual_tokens(prompt_text, response_message, effective_estimate)
            RATE_LIMITER.release(actual_tokens, filepath, request_id=request_id)


def query_text_simple(question_path, target_file, callback, question=None):
    if question is None:
        question = open(question_path, "r", encoding="utf-8").read()

    if Shared.ADDED_TO_PROMPT is not None:
        question = question + " " + Shared.ADDED_TO_PROMPT

    if "api.openai" in Shared.API_URL:
        try:
            response_message = query_text_simple_openai_new(question, Shared.API_URL, target_file)
        except:
            response_message = query_text_simple_generic(question, Shared.API_URL, target_file)
    elif "googleapis" in Shared.API_URL:
        response_message = query_text_simple_google(question, Shared.API_URL, target_file)
    elif "anthropic" in Shared.API_URL:
        response_message = query_text_simple_anthropic(question, Shared.API_URL, target_file)
    else:
        response_message = query_text_simple_generic(question, Shared.API_URL, target_file)

    if response_message:
        callback(response_message, target_file)

    return response_message


def query_image_simple_openai_new(base64_image, api_url, target_file, text):
    complete_url = api_url
    if not complete_url.endswith("/"):
        complete_url += "/"
    complete_url += "responses"

    payload = {
        "model": Shared.MODEL_NAME,
        "input": [
            {
                "role": "user",
                "content": [
                    {"type": "input_text", "text": text},
                    {"type": "input_image", "image_url": f"data:image/png;base64,{base64_image}"}
                ]
            }
        ]
    }

    if Shared.SYSTEM_PROMPT is not None:
        payload["instructions"] = Shared.SYSTEM_PROMPT

    if Shared.PAYLOAD_REASONING_EFFORT:
        payload["reasoning"] = {"effort": Shared.PAYLOAD_REASONING_EFFORT}

    if Shared.TOOLS_PAYLOAD is not None:
        payload["tools"] = Shared.TOOLS_PAYLOAD

        #print(payload["tools"])

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {Shared.API_KEY}"
    }

    dump_payload(payload, target_file)

    response = requests.post(complete_url, headers=headers, json=payload, timeout=30*60)
    if response.status_code != 200:
        print(response)
        print(response.status_code)
        print(response.text)

    response = response.json()

    dump_response(response, target_file)

    return response["output"][-1]["content"][0]["text"]


def query_image_simple_generic(base64_image, api_url, target_file, text):
    complete_url = api_url + "chat/completions"

    messages = [{"role": "user", "content": [{"type": "text", "text": text},
                                             {"type": "image_url",
                                              "image_url": {"url": f"data:image/png;base64,{base64_image}"}}]}]

    if Shared.SYSTEM_PROMPT is not None:
        messages = [{"role": "system", "content": Shared.SYSTEM_PROMPT}] + messages

    payload = {
        "model": Shared.MODEL_NAME,
        "messages": messages,
        "max_tokens": Shared.MAX_REQUESTED_TOKENS,
    }

    if Shared.TOOLS_PAYLOAD is not None:
        raise Exception("fail")

    if Shared.ADDED_TO_PAYLOAD is not None:
        payload.update(Shared.ADDED_TO_PAYLOAD)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {Shared.API_KEY}"
    }

    payload.update(get_llm_specific_settings())

    streaming_enabled = True

    if streaming_enabled:
        payload["stream"] = True
        response_message = ""
        chunk_count = 0

        # We add stream=True to requests so we can iterate over chunks
        with requests.post(complete_url, headers=headers, json=payload, stream=True) as resp:
            if resp.status_code != 200:
                print(resp)
                print(resp.status_code)
                print(resp.text)

            for line in resp.iter_lines():
                if not line:
                    continue
                decoded_line = line.decode("utf-8")

                # OpenAI-style streaming lines begin with "data: "
                if decoded_line.startswith("data: "):
                    data_str = decoded_line[len("data: "):].strip()
                    if data_str == "[DONE]":
                        # End of stream
                        break
                    try:
                        data_json = json.loads(data_str)
                        if "choices" in data_json:
                            # Each chunk has a delta with partial content
                            chunk_content = data_json["choices"][0]["delta"].get("content", "")
                            if chunk_content:
                                response_message += chunk_content
                                chunk_count += 1
                                # print(chunk_count)
                                if chunk_count % 10 == 0:
                                    # print(chunk_count, len(response_message), response_message.replace("\n", " ").replace("\r", "").strip())
                                    pass
                    except json.JSONDecodeError:
                        # Possibly a keep-alive or incomplete chunk
                        traceback.print_exc()
    else:
        response = requests.post(complete_url, headers=headers, json=payload)
        #print(response)
        #print(response.status_code)
        #print(response.text)

        response = response.json()
        dump_response(response, target_file)

        try:
            response_message = response["choices"][0]["message"]["content"]
        except Exception as e:
            print(response)
            raise Exception(e)

    return response_message


def query_image_simple_anthropic(base64_image, api_url, target_file, text):
    complete_url = api_url + "messages"

    messages = [
        {"role": "user", "content": [
            {"type": "text", "text": text},
            {"type": "image", "source": {
                "type": "base64",
                "media_type": "image/png",
                "data": base64_image
            }}
        ]}
    ]

    headers = {
        "content-type": "application/json",
        "anthropic-version": "2023-06-01",
        "anthropic-beta": "output-128k-2025-02-19",
        "x-api-key": Shared.API_KEY
    }

    payload = {
        "model": Shared.MODEL_NAME,
        "max_tokens": Shared.MAX_REQUESTED_TOKENS
    }

    if Shared.ANTHROPIC_THINKING_TOKENS is not None:
        payload["thinking"] = {"type": "enabled", "budget_tokens": Shared.ANTHROPIC_THINKING_TOKENS}
        payload["max_tokens"] += Shared.ANTHROPIC_THINKING_TOKENS
        payload["max_tokens"] = min(128000, payload["max_tokens"])

    payload["messages"] = messages

    response = requests.post(complete_url, headers=headers, json=payload).json()
    dump_response(response, target_file)

    try:
        response_message = response["content"][-1]["text"]
    except Exception as e:
        raise Exception(str(response))

    return response_message


def query_image_simple_google(base64_image, api_url, target_file, text):
    complete_url = api_url + "models/" + Shared.MODEL_NAME + ":generateContent?key=" + Shared.API_KEY

    headers = {
        "Content-Type": "application/json",
    }

    payload = {
        "contents": [
            {"parts": [
                {"text": text},
                {"inline_data": {
                    "mime_type": "image/png",
                    "data": base64_image
                }}
            ]}
        ]
    }

    if "gemini-2.5-flash" in Shared.MODEL_NAME:
        payload["generationConfig"] = {
            "thinkingConfig": {
                "thinkingBudget": Shared.ANTHROPIC_THINKING_TOKENS if Shared.ANTHROPIC_THINKING_TOKENS is not None else 0
            }
        }

    response = requests.post(complete_url, headers=headers, json=payload).json()
    dump_response(response, target_file)

    try:
        response_message = response["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        raise Exception(str(response))

    return response_message


def query_image_simple_with_rate_limit(question_path, target_file, callback, base64_image=None, 
                                       text=None, use_rate_limit=True, estimated_tokens=4000):
    """Wrapper for query_image_simple with rate limiting support."""
    filepath = target_file if use_rate_limit else None
    prompt_text = text if text is not None else "Can you describe the provided visualization?"
    effective_estimate = estimated_tokens or 0
    if use_rate_limit:
        if not effective_estimate:
            effective_estimate = 4000
        # Images typically add extra latency/tokens on the request
        effective_estimate = _estimate_pre_request_tokens(prompt_text, effective_estimate, extra_tokens=512)
        acquired, reason, request_id = RATE_LIMITER.wait_for_slot(effective_estimate, filepath, max_wait=300)
        if not acquired:
            raise Exception(f"Failed to acquire rate limit slot: {reason}")
    else:
        request_id = None
        if not effective_estimate:
            effective_estimate = 4000
    response_message = None
    try:
        # Call the original function
        response_message = query_image_simple(question_path, target_file, callback, base64_image, prompt_text)
        return response_message
    finally:
        if use_rate_limit and request_id is not None:
            actual_tokens = _estimate_actual_tokens(prompt_text, response_message, effective_estimate, extra_tokens=512)
            RATE_LIMITER.release(actual_tokens, filepath, request_id=request_id)


def query_image_simple(question_path, target_file, callback, base64_image=None, text=None):
    if text is None:
        text = "Can you describe the provided visualization?"

    if base64_image is None:
        base64_image = encode_image(question_path)

    if "api.openai" in Shared.API_URL:
        try:
            response_message = query_image_simple_openai_new(base64_image, Shared.API_URL, target_file, text)
        except:
            response_message = query_image_simple_generic(base64_image, Shared.API_URL, target_file, text)
    elif "googleapis" in Shared.API_URL:
        response_message = query_image_simple_google(base64_image, Shared.API_URL, target_file, text)
    elif "anthropic" in Shared.API_URL:
        response_message = query_image_simple_anthropic(base64_image, Shared.API_URL, target_file, text)
    else:
        response_message = query_image_simple_generic(base64_image, Shared.API_URL, target_file, text)

    callback(response_message, target_file)
    return response_message


def get_models():
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {Shared.API_KEY}"
    }

    complete_url = Shared.API_URL+"models"

    response = requests.get(complete_url, headers=headers)

    models = response.json()

    return models


def insert_api_keys():
    MODELS_DICT["openai"]["api_key"] = open("../api_openai.txt", "r").read().strip()
    MODELS_DICT["mistral"]["api_key"] = open("../api_mistral.txt", "r").read().strip()
    MODELS_DICT["grok"]["api_key"] = open("../api_grok.txt", "r").read().strip()
    MODELS_DICT["deepinfra"]["api_key"] = open("../api_deepinfra.txt", "r").read().strip()
    MODELS_DICT["qwen"]["api_key"] = open("../api_qwen.txt", "r").read().strip()
    MODELS_DICT["nvidia"]["api_key"] = open("../api_nvidia.txt", "r").read().strip()
    MODELS_DICT["google"]["api_key"] = open("../api_google.txt", "r").read().strip()
    MODELS_DICT["claude"]["api_key"] = open("../api_anthropic.txt", "r").read().strip()
    MODELS_DICT["perplexity"]["api_key"] = open("../api_perplexity.txt", "r").read().strip()
    MODELS_DICT["groq"]["api_key"] = open("../api_groq.txt", "r").read().strip()
    MODELS_DICT["openrouter"]["api_key"] = open("../api_openrouter.txt", "r").read().strip()


def check_all_models():
    insert_api_keys()

    for provider in MODELS_DICT:
        if provider not in {"google", "claude", "grok", "qwen", "manual", "perplexity", "ollama_local"}:
            print(provider)
            info = MODELS_DICT[provider]
            Shared.API_URL = info["api_url"]
            Shared.API_KEY = info["api_key"]
            models = get_models()
            models = {x["id"].split(":latest")[0] for x in models["data"]}
            models_specified = set(info["models"])

            for x, y in MODELS_DICT["manual"]["models"].items():
                if y["provider"] == provider:
                    models_specified.add(y["base_model"])

            print("info", provider, models)

            diff = models_specified.difference(models)
            if len(diff) > 0:
                print("ERROR")
                print(diff)
                print(models_specified)
                print(models)
                input()


def check_missing_models():
    responding_models = set(x.split("_cat")[0] for x in os.listdir("answers") if not x.startswith("__init"))
    catalogue_models = set()
    for provider in MODELS_DICT:
        info = MODELS_DICT[provider]
        for model in info["models"]:
            catalogue_models.add(clean_model_name(model))
    diff = set(catalogue_models).difference(responding_models)
    if diff:
        raise Exception("catalogue_models outdated: "+str(diff))
    diff = set(responding_models).difference(catalogue_models)
    diff = {x for x in diff if not is_excluded_from_table(x)}
    print(diff)


def clean_model_name(m_name):
    return m_name.replace("/", "").replace(":", "")


def get_base_evaluation_path(model_name):
    return "evaluation-grok41-fast" if ("grok-4.1-fast" in model_name or "grok-4-1-fast" in model_name) else "evaluation-" + clean_model_name(model_name).split("-exp")[0].split("-preview")[0]


def configure_rate_limiter(requests_per_minute=60, requests_per_hour=1000,
                          tokens_per_minute=90000, tokens_per_hour=2000000,
                          max_concurrent=10):
    """Configure the global rate limiter with new settings."""
    global RATE_LIMITER
    RATE_LIMITER = RateLimiter(
        requests_per_minute=requests_per_minute,
        requests_per_hour=requests_per_hour,
        tokens_per_minute=tokens_per_minute,
        tokens_per_hour=tokens_per_hour,
        max_concurrent=max_concurrent
    )
    return RATE_LIMITER


if __name__ == "__main__":
    check_missing_models()
    check_all_models()
    #set_api_key("answer")
    #models = get_models()
    #print(models)
