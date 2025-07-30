# Architecture

## Overview
The evaluator separates the user interface from the business logic. Four evaluation stages form the core flow: Ideate, Investigate, Iterate, and Create.

## Why It Matters
A clear architecture lets you update evaluation rules without touching the UI.

## Audience, Scope & Personas
Developers extending the evaluator or embedding it in a larger tool.

## Prerequisites
- Basic Python knowledge
- Familiarity with Streamlit

## Security & Compliance
This local application stores no user data. Review your organization’s data policies before sharing prompts.

## Tasks & Step-by-Step Instructions
1. Review the `logic` module for evaluation rules.
2. Update or add stages as needed.
3. Modify the Streamlit app under `app` if you need a different interface.

## Access Control & Permissions
No elevated permissions are required to modify or run the code.

## Examples & Templates
```bash
prompt-evaluator/
├── app/                # Streamlit UI
├── logic/              # Evaluation logic
├── examples/           # Sample prompts
├── docs/               # Documentation
```

## Known Issues & Friction Points
The keyword matching approach is simple and may not catch nuanced prompt issues.

## Tips & Best Practices
Keep logic isolated. Add tests when expanding evaluation rules.

## Troubleshooting
If the UI fails to display feedback, confirm that your modifications in `logic` return proper `StageFeedback` objects.

## Dependencies & Escalation
- Python standard library
- Streamlit
For complex architectural changes, open a discussion in the repository.

## Success Metrics & Outcomes
Architecture updates should not break existing stages and should maintain UI responsiveness.

## Resources & References
See the main [README](../README.md) for usage details.

## Last Reviewed / Last Updated
2025-07-30
