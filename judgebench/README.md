# JudgeBench

JudgeBench is a small PM-LLM-Benchmark sub-benchmark for checking which LLMs behave like reliable judges.

Suggested workflow:

1. Parse an existing PM evaluation folder:
   `python extract_scores.py --evaluation-dir ../evaluation-gpt-5.4`
2. Select one representative question from each category `cat01` through `cat06` and copy the reference answers:
   `python select_references.py`
3. Run judge LLMs over the selected references:
   `python evaluate.py`
4. Produce the judge quality report:
   `python results.py`

The selector chooses the question with the lowest `AVERAGE - STDEV` in each category. For each selected question it copies the answers closest to score quantiles `0.25`, `0.50`, `0.75`, and `1.00`.

The judge prompt follows the main PM-LLM-Benchmark textual evaluation prompt and always includes the strict-evaluation clause.

`results.py` writes `judge_quality.md` with one row per judge: judge name, a 0-100 synthetic quality score, and two columns per category (`average` and `stdev`). The quality score uses only the judge's own scores, rewarding lower average scores and higher standard deviation.
