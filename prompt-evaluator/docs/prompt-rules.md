# Prompt Rules

## Overview
Each evaluation stage checks for specific indicators in a prompt.

## Why It Matters
Defined rules provide consistent feedback and encourage clear prompting.

## Audience, Scope & Personas
Prompt engineers and documentation writers using the evaluator to refine prompts.

## Prerequisites
Read the [architecture](architecture.md) to understand the stage flow.

## Security & Compliance
No sensitive data is stored. Follow your organization’s policies when sharing prompts.

## Tasks & Step-by-Step Instructions
1. Review the table of triggers below.
2. Test your prompt with the evaluator.
3. Revise your prompt based on the feedback.

## Access Control & Permissions
No special permissions are needed to use or modify the rules.

## Examples & Templates
| Stage | Trigger | Explanation |
|-------|---------|-------------|
| **Ideate** | Prompt shorter than 10 characters or phrased as a question | Goal is unclear or poorly defined. |
| **Investigate** | Missing words like `context`, `research`, or `background` | Shows no supporting information. |
| **Iterate** | No keywords `revise`, `iterate`, `refine`, or `feedback` | Does not encourage improvement. |
| **Create** | Lacks verbs such as `create`, `generate`, `produce`, or `write` | Output requirement is unclear. |

## Known Issues & Friction Points
Rules are simple keyword checks and may flag false positives.

## Tips & Best Practices
Use explicit verbs and provide context for better evaluation results.

## Troubleshooting
If no rules trigger, ensure your prompt is spelled correctly and meets minimum length.

## Dependencies & Escalation
The rules depend only on the Python logic in the `logic` module. For complex rule additions, open an issue.

## Success Metrics & Outcomes
A successful prompt passes all stages or shows clear guidance on improvements.

## Resources & References
See [README](../README.md) for usage instructions.

## Last Reviewed / Last Updated
2025-07-30
