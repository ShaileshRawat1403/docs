# Soothsayer
---
title: Building Soothsayer
description: A comprehensive, thinking-first guide to building your own CrewAI-powered local AI agent for meaningful content and communication.
status: Stable
version: v1.0
maintainer: Shailesh Rawat (PoeticMayhem)
last_updated: 2025-07-27
tags: [agentic-ai, crewai, markdown-parser, gradio, ollama, langchain, internal-comms, change-translation]
---

# 🧠 Building Soothsayer  
*A thinking assistant isn’t built in a day. It’s built in loops.*

---

## 📍 What Are We Building?

Soothsayer is not your average chatbot.  
It’s a **CrewAI-powered agentic system** designed to **translate chaos into clarity** — turning half-baked thoughts, messy updates, or abstract intentions into well-structured, usable documents.

You’ll learn to build an agent that:

- Reads context from structured Markdown files  
- Thinks through your message using a philosophical system prompt  
- Responds with tone-aligned, structured output  
- Runs **fully offline** using Ollama (no API keys needed)  
- Delivers a styled UI via Gradio

---

## 🧭 Why This Agent Exists

> We don’t suffer from a lack of information.  
We suffer from miscommunication — and unstructured thinking.

Soothsayer was born from a practical pain point:
> *"Why does every team have tons of updates… but no shared understanding?"*

We needed a tool that:
- **Understands the structure behind intent**
- **Bridges thinking and writing**
- **Feels like a mirror, not a machine**

---

## 🔁 The Thinking Loop:  
### Ideate → Investigate → Iterate → Create

This loop powers the agent's process and your own.

| Stage        | Meaning                          |
|--------------|----------------------------------|
| Ideate       | What's the raw input or idea?    |
| Investigate  | What’s unclear or assumed?       |
| Iterate      | How can it be framed better?     |
| Create       | What’s the final usable form?    |

Soothsayer lives in this loop.

---

## ⚙️ System Components (Explained Simply)

| Component | Role |
|----------|------|
| `parse_md_function.py` | Converts your input Markdown doc into structured prompt fields |
| `soothsayer_agent.py` | Defines the CrewAI agent using a system prompt |
| `app.py` (Gradio) | The UI where you chat with the agent |
| Ollama + Mistral | The local LLM that powers reasoning |
| CrewAI | Handles task routing and agent execution |
| Markdown | Your thinking context: forms, requests, drafts |

---

## 🧰 Step-by-Step: Set Up & Understand

### 1. 🐍 Virtual Environment (Clean Install)
```bash
python3 -m venv .venv
source .venv/bin/activate  # Mac/Linux

2. 📦 Install Dependencies

pip install -r requirements.txt

Dependencies include:

gradio

crewai

langchain

langchain-ollama



---

📄 Your First Input File

Create a file inside input_docs/ — for example:
add_numbers.md

---
Title: Add Numbers Utility
Overview: This function takes two integers and returns their sum.
Why It Matters: Helps simplify repeated addition tasks in our service layer.
---

This Markdown is not just content — it's the thinking substrate.
It feeds the agent your context, tone, and structure.


---

🧠 The System Prompt

In soothsayer_agent.py, we dynamically build a prompt like:

You are Soothsayer, an AI strategist built to translate complexity into clarity...
📘 Title: Add Numbers Utility
📎 Overview: This function takes two integers...
...

This is how context meets cognition.
You’re not prompting like a chatbot — you’re creating task-aware AI thinking.


---

🧩 Running the System

cd gradio_ui
python app.py

It opens a Gradio UI where you can chat with Soothsayer — and get back structured, stylized output.


---

❌ Failures We Faced (and Fixed)

> Because every great system is born from its bugs.



🔸 Error: Please provide Prompt Values for: task, lazy_prompt

Cause: CrewAI was expecting input arguments (prompt or task) which were missing.

Fix:
We rewired the Task object to pass expected_output=None and removed lazy prompting logic — allowing the agent to reason from the system prompt directly.


---

🔸 Failure: Agent Not Triggering

Cause: The task wasn't linked correctly to the agent — crew = Crew(...) was missing or empty.

Fix:
Defined a valid Task, and then created a Crew object like:

crew = Crew(
    agents=[soothsayer],
    tasks=[task],
    verbose=True
)


---

🔸 Failure: Markdown Not Parsed

Cause: Missing fields in the Markdown input caused the agent to break on NoneType.

Fix:
We added fallback logic in parse_dev_doc_markdown() to gracefully return empty strings when fields are missing:

data.get("Overview", "")

Always validate the structure of your .md file!


---

🖼️ System Architecture

[Markdown File]
     ⬇
parse_dev_doc_markdown()
     ⬇
System Prompt with Fields
     ⬇
[CrewAI Task] → Soothsayer Agent (Ollama Mistral)
     ⬇
Generated Response
     ⬇
Gradio UI (Blocks API)


---

🧪 Test Output Example

Input Thought:

> "I need to document a small function that adds numbers, but explain why it matters for the new API layer."



Output from Soothsayer:

📘 Title: Add Numbers Utility  
📎 Overview: This function takes two integers and returns their sum.  
📌 Why It Matters: This forms a clean utility for repeated arithmetic logic in our new service layer...

It understood:

The task

The context

The “Why”, not just the “What”



---

✏️ Tuning the Style & Thinking

Want to change how Soothsayer speaks?

Go to soothsayer_agent.py and modify this line:

You are Soothsayer, an AI strategist built to translate complexity into clarity...

You can embed:

Humor

Formality

Departmental language (e.g. legal, HR, UX)


It’s your agent — tune it to your reality.


---

🧠 What You’ve Really Built

This is more than just code.

You’ve built a thinking framework + reflection engine that:

Grounds every AI output in a meaningful structure

Captures the context behind chaos

Scales your communication clarity without dumbing it down


You didn’t just automate.
You made thinking repeatable.


---

🔗 What’s Next?

TECH_STACK.md: Architecture, Docker, GitHub Actions

parse_dev_doc_markdown.py: Grounding parser

soothsayer_agent.py: The reflective agent logic

app.py: Run and stylize the UI



---

✍ Author

Shailesh Rawat a.k.a. PoeticMayhem
Building systems where clarity becomes a practice, not an afterthought.


---

✅ Next: `TECH_STACK.md` with full architecture, file references, Docker, GitHub Actions, and extension roadmap.

Would you like that immediately? Or want to review/edit this first?

