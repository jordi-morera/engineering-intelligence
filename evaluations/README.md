# Evaluation

The long-term system must not be judged only by whether it produces convincing-looking
documentation. This directory will hold the evaluation strategy and, eventually,
evaluation harnesses.

## Guiding metrics

The following metrics define what "good" means for Engineering Intelligence:

- **Specification completeness** — whether all schema fields are meaningfully populated.
- **Research accuracy** — whether documented facts match their cited sources.
- **Root cause accuracy** — for bugs, whether the identified root cause is correct.
- **Unsupported assumptions** — the number of assumptions recorded without evidence or verification.
- **Contradictions detected** — whether the critique phase surfaces internal contradictions.
- **Human corrections** — how often and how much a human corrects the agent's output.
- **First-pass validation success** — fraction of specs validated without a BLOCKED outcome.
- **Tool calls** — the number and appropriateness of tool calls made.
- **Token usage** — total tokens consumed per output.
- **Repeated/redundant searches** — duplicated or wasteful research steps.
- **Execution time** — wall-clock time to produce a validated specification.

## Status

Evaluation is currently documentation-only. No automated evaluation harness is
implemented yet. The next step is to define concrete evaluation scenarios (golden
specifications) and capture telemetry needed to compute the metrics above.

## Future design goals

The evaluation harness should be deterministic, runnable without a real API, and
designed around small focused contexts, structured intermediate artifacts, and
reusable research — consistent with the token-efficiency objective.
