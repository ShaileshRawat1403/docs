"""Streamlit application for the Prompt Thinking Loop Evaluator."""

import streamlit as st
from logic.evaluator import PromptEvaluator


def main() -> None:
    """Run the Streamlit UI."""
    st.title("Prompt Thinking Loop Evaluator")
    st.write("Analyze your prompt through the Ideate → Investigate → Iterate → Create loop.")

    evaluator = PromptEvaluator()

    prompt = st.text_area("Enter your prompt", height=200)
    if st.button("Evaluate"):
        if not prompt.strip():
            st.warning("Please enter a prompt to evaluate.")
            return

        results = evaluator.evaluate(prompt)

        for stage in evaluator.stages:
            feedback = results[stage]
            with st.expander(stage):
                status = "✅ Passed" if feedback.passed else "❌ Failed"
                st.markdown(f"**Result:** {status}")
                st.write(feedback.feedback)


if __name__ == "__main__":
    main()
