import pytest
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from logic.evaluator import PromptEvaluator


def test_all_pass():
    prompt = "Research the background, create a report, and revise it afterward."
    results = PromptEvaluator().evaluate(prompt)
    assert all(feedback.passed for feedback in results.values())


def test_ideate_fail():
    results = PromptEvaluator().evaluate("Help?")
    assert not results["Ideate"].passed


def test_investigate_fail():
    results = PromptEvaluator().evaluate("Create a short story.")
    assert not results["Investigate"].passed


def test_iterate_fail():
    prompt = "Provide context and create a plan."
    results = PromptEvaluator().evaluate(prompt)
    assert not results["Iterate"].passed


def test_create_fail():
    prompt = "Research the topic and refine the approach based on feedback."
    results = PromptEvaluator().evaluate(prompt)
    assert not results["Create"].passed
