# Prompt Thinking Loop Evaluator

## Deviation Notice
This README intentionally uses a descriptive heading and does not match the filename as required in `AGENTS.md`.

## Overview
The Prompt Thinking Loop Evaluator analyzes prompts through four stages to help you refine your ideas. The Streamlit app provides immediate feedback.

## Why It Matters
Clear prompts create better results. This tool shows where your prompt lacks context or iterative steps.

## Audience, Scope & Personas
This tool is for technical writers and prompt engineers who need quick feedback when drafting prompts.

## Prerequisites
- Python 3.10 or later
- `pip` for installing dependencies

## Security & Compliance
The evaluator runs locally and does not send data externally. Follow your organization’s data handling guidelines.

## Tasks & Step-by-Step Instructions
1. Clone the repository.
2. Navigate to `prompt-evaluator`.
3. Install dependencies with `pip install -r requirements.txt`.
4. Launch the UI with `streamlit run app/main.py`.
5. Enter a prompt and select **Evaluate**.

## Access Control & Permissions
No special permissions are required. Run the tool as a regular user.

## Examples & Templates
```bash
streamlit run app/main.py
```
Enter: `Write a short summary of the history of aviation.`

## Known Issues & Friction Points
- Dependency installation may fail on restricted networks.
- Streamlit requires an available port to run the app.

## Tips & Best Practices
Iterate on prompts and include context about the desired output.

## Troubleshooting
If the app fails to load, ensure Streamlit is installed and the port is free. Rerun `streamlit run app/main.py`.

## Dependencies & Escalation
- Streamlit
- Python standard library
For major issues, open an issue in the repository.

## Success Metrics & Outcomes
You successfully evaluate prompts when each stage in the UI shows a pass.

## Resources & References
- [Architecture](docs/architecture.md)
- [Prompt Rules](docs/prompt-rules.md)

## Last Reviewed / Last Updated
2025-07-30
