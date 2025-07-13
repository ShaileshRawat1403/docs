# Prompt Thinking Loop Evaluator

This tool helps authors craft better prompts by analyzing them through four
stages: **Ideate → Investigate → Iterate → Create**. It is built with a small
heuristic engine and a Streamlit UI for quick feedback.

## Features

- Simple evaluation rules for each stage
- Streamlit interface to type a prompt and view per‑stage feedback
- Example prompts showing common mistakes
- Documentation outlining architecture and rules

## Installation

1. Clone the repository.
2. Navigate to the `prompt-evaluator` folder.
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the Streamlit application:

```bash
streamlit run app/main.py
```

Enter a prompt in the text area and click **Evaluate**. The app will display the
result for each stage in expandable sections.

## Folder Structure

```
prompt-evaluator/
├── app/                # Streamlit UI
├── logic/              # Evaluation logic
├── examples/           # Sample prompts
├── docs/               # Project documentation
├── requirements.txt    # Python dependencies
└── .github/workflows/  # CI/CD workflow (optional)
```

## Use Cases

- Teaching prompt engineering concepts
- Demonstrating iterative thinking when crafting prompts
- Providing quick feedback for documentation writers

## License

This project is provided under the MIT license. See [LICENSE](../LICENSE) for
details.
