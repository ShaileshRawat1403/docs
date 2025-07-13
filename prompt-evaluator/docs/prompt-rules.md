# Prompt Rules

Each stage in the Prompt Thinking Loop checks for specific attributes in a
prompt. When a rule is triggered, the evaluator marks the stage as failed and
returns a short explanation.

| Stage | Trigger | Explanation |
|-------|---------|-------------|
| **Ideate** | Prompt shorter than 10 characters or phrased as a question | Indicates the goal is unclear or not well defined. |
| **Investigate** | Absence of words like `context`, `research`, or `background` | Shows that no research or prior information is referenced. |
| **Iterate** | Missing keywords `revise`, `iterate`, `refine`, or `feedback` | The prompt does not encourage improving or refining the output. |
| **Create** | No verbs such as `create`, `generate`, `produce`, or `write` | The prompt does not specify what should be produced. |

These rules can be extended with more sophisticated natural language checks as
the project evolves.
