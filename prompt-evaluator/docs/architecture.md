# Architecture Overview

The Prompt Thinking Loop Evaluator is organized into a small set of modules to
keep logic isolated from the user interface. The high‑level flow follows the
four evaluation stages:

```
Prompt -> Ideate -> Investigate -> Iterate -> Create -> Results
```

## Components

- **`logic/evaluator.py`**
  Contains the heuristics for each stage. The `PromptEvaluator` returns detailed
  feedback for the input prompt in the form of `StageFeedback` data classes.

- **`app/main.py`**
  Implements a Streamlit UI for entering prompts. It imports `PromptEvaluator`
  from the logic layer and displays feedback for each stage using expanders.

- **`examples/`**
  Sample prompts used for testing and demonstration of failing cases.

- **`docs/`**
  This documentation folder describes the architecture and the rules that each
  stage checks.

## Reasoning Behind the Design

The tool follows the typical pattern of separating presentation (Streamlit) from
business logic. This makes it easier to update rules without changing the UI.
The evaluator uses simple keyword matching so that it can run without external
dependencies or network calls. Each stage can be expanded in the future with
more sophisticated natural language processing.
