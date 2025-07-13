"""Prompt Thinking Loop Evaluator logic.

This module defines the evaluator for analyzing prompts using the
Ideate → Investigate → Iterate → Create loop. Each stage has a
set of simple heuristics to determine whether the prompt sufficiently
addresses that phase.
"""

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class StageFeedback:
    """Holds evaluation result for a single stage."""

    stage: str
    passed: bool
    feedback: str


class PromptEvaluator:
    """Evaluates prompts based on the Prompt Thinking Loop."""

    stages: List[str] = ["Ideate", "Investigate", "Iterate", "Create"]

    def __init__(self) -> None:
        pass

    def evaluate(self, prompt: str) -> Dict[str, StageFeedback]:
        """Evaluate the given prompt.

        Parameters
        ----------
        prompt : str
            The user provided prompt.

        Returns
        -------
        Dict[str, StageFeedback]
            Mapping of stage name to feedback.
        """
        prompt_lower = prompt.lower()
        results: Dict[str, StageFeedback] = {}

        # Ideate: prompt should communicate a clear idea or goal
        if len(prompt.strip()) < 10 or "?" in prompt:
            results["Ideate"] = StageFeedback(
                stage="Ideate",
                passed=False,
                feedback="Prompt lacks a clear goal or is too short."
            )
        else:
            results["Ideate"] = StageFeedback(
                stage="Ideate",
                passed=True,
                feedback="Clear goal identified."
            )

        # Investigate: should reference context or mention research
        if any(word in prompt_lower for word in ["context", "research", "background"]):
            results["Investigate"] = StageFeedback(
                stage="Investigate",
                passed=True,
                feedback="Includes context or research hints."
            )
        else:
            results["Investigate"] = StageFeedback(
                stage="Investigate",
                passed=False,
                feedback="No investigation or context found."
            )

        # Iterate: should encourage refinement or iteration
        if any(word in prompt_lower for word in ["revise", "iterate", "refine", "feedback"]):
            results["Iterate"] = StageFeedback(
                stage="Iterate",
                passed=True,
                feedback="Mentions iteration or refinement."
            )
        else:
            results["Iterate"] = StageFeedback(
                stage="Iterate",
                passed=False,
                feedback="No sign of iteration or refinement."
            )

        # Create: should request generation or final deliverable
        if any(word in prompt_lower for word in ["create", "generate", "produce", "write"]):
            results["Create"] = StageFeedback(
                stage="Create",
                passed=True,
                feedback="Specifies a deliverable."
            )
        else:
            results["Create"] = StageFeedback(
                stage="Create",
                passed=False,
                feedback="Does not specify what to create."
            )

        return results


__all__ = ["PromptEvaluator", "StageFeedback"]
