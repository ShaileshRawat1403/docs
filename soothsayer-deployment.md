```markdown

---
title: Soothsayer Technical Stack & Deployment Guide
description: Full architecture, setup, and DevOps workflow for the Soothsayer agentic AI system powered by CrewAI, LangChain, and Gradio.
status: Stable
version: v1.0
maintainer: Shailesh Rawat (PoeticMayhem)
last_updated: 2025-07-27
tags: [crew-ai, langchain, ollama, gradio, devops, markdown-parsing, local-agent, docker, github-actions]
---

# 🧱 Soothsayer Tech Stack & Deployment Guide

A system-level overview for developers, DevOps engineers, and technical content builders working with the Soothsayer agentic AI system. This document includes architecture, setup, local and containerized deployment, CI/CD guidance, and extension patterns.

---

## 📁 Folder Structure

```plaintext
soothsayer-crewai/
├── agents/
│   └── soothsayer_agent.py           # Defines the CrewAI logic for the reflective agent
├── configs/
│   └── tools/
│       └── parse_md_function.py      # Custom parser to extract fields from Markdown
├── input_docs/
│   └── add_numbers.md                # Example Markdown file (context input)
├── gradio_ui/
│   └── app.py                        # Gradio-based UI application
├── requirements.txt                  # Python dependencies
├── Dockerfile                        # Container setup (optional)
├── .github/
│   └── workflows/
│       └── ci.yml                    # GitHub Actions for linting & MD validation
├── .venv/                            # Local Python virtual environment (ignored)
├── BUILDING_SOOTHSAYER.md            # Conceptual & guided walkthrough
└── TECH_STACK.md                     # You're here


---

⚙️ Tooling Breakdown

Layer	Tool / Library	Purpose

🧠 LLM Engine	Ollama + Mistral	Local language model, no API key required
🧩 Agent Logic	CrewAI	Task-driven, modular multi-agent orchestration
📄 Prompt Parser	Custom Markdown Parser	Reads .md into structured prompt components
🖥 UI	Gradio	Interactive frontend via Blocks API
🎨 Styling	Custom CSS	Reflects Sans Serif Sentiments visual identity
🔧 Infra	Docker, GitHub Actions	Local containerization + CI/CD automation



---

🧠 Architecture Flow

[Markdown Input File]
        |
        v
parse_dev_doc_markdown()
        |
        v
System Prompt → [CrewAI Task] → Soothsayer Agent → Ollama LLM (Mistral)
        |
        v
Structured Output → Gradio UI → Copyable/Exportable Markdown


---

🛠 Local Setup Instructions

Step 1: Create Virtual Environment

python3 -m venv .venv
source .venv/bin/activate  # Mac/Linux

Step 2: Install Requirements

pip install -r requirements.txt

Ensure Ollama is running locally with the mistral model pulled:

ollama pull mistral

Step 3: Add Your Markdown File

Place your content inside input_docs/:

---
Title: Add Numbers Utility
Overview: This function adds two numbers.
Why It Matters: Used in our API logic and reduces redundancy.
---

Step 4: Launch the Gradio Interface

cd gradio_ui
python app.py

Open the local Gradio link in your browser.


---

🐳 Docker Deployment (Optional)

Step 1: Create Dockerfile

Example minimal Dockerfile:

FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "gradio_ui/app.py"]

Step 2: Build & Run

docker build -t soothsayer-agent .
docker run -p 7860:7860 soothsayer-agent


---

🚀 GitHub Actions: CI Workflow

Example .github/workflows/ci.yml:

name: Validate Markdown & Lint
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  validate-md:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install deps
        run: pip install markdownlint-cli2 ruff
      - name: Lint markdown
        run: npx markdownlint-cli2 **/*.md
      - name: Lint Python
        run: ruff .


---

🧩 Extension Opportunities

Feature	Description

🔄 Slack input	Auto-pull structured content → send to Soothsayer
📝 PDF/HTML export	Use markdown2, pdfkit, or Gradio export buttons
⚙️ Streamlit/FastAPI UI	Optional UI alternatives for lightweight or API-driven deployment
📤 Notion/Git sync	Push outputs to Notion/GitHub via script



---

🧨 Common Pitfalls

Issue	Root Cause	Fix

Prompt field error	Missing expected Markdown keys	Use .get("field", "") in parser
Agent not triggering	Task not linked to Crew	Ensure Crew(agents=[...], tasks=[...]) is configured
Broken Markdown output	Improperly closed fences	Always wrap with consistent ```markdown syntax
Ollama not responding	Model not pulled	Run ollama pull mistral before launching app



---

✅ System Validated Environments

OS	Status

MacOS	✅ Tested
Ubuntu 22	✅ Tested
Windows 11 (WSL)	✅ Tested
GitHub Codespaces	⚠️ LLM model must run externally



---

🧠 Final Notes

Soothsayer isn't just a system — it's a philosophy-in-action. Every component is designed to help you translate fuzzy ideas into structured intelligence, grounded in your own context and tone. This technical stack is modular, extensible, and ready to scale across content, communication, and product documentation workflows.


---

🔗 Related Files

BUILDING_SOOTHSAYER.md — Narrative build log & conceptual guide

soothsayer_agent.py — Reflective system prompt agent logic

parse_md_function.py — Structured Markdown ingestion

app.py — Gradio UI renderer



---

✍ Maintainer

Shailesh Rawat (PoeticMayhem)
GitHub • LinkedIn


---

```

