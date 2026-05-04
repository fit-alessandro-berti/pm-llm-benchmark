import os
import sys
from pathlib import Path


UTILS_DIR = Path(__file__).resolve().parent
REPO_ROOT = UTILS_DIR.parent


def add_repo_root_to_path():
    repo_root = str(REPO_ROOT)
    if repo_root not in sys.path:
        sys.path.insert(0, repo_root)


def chdir_repo_root():
    os.chdir(REPO_ROOT)


add_repo_root_to_path()
