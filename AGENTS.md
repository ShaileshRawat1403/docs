# Agents
Sans Serif Sentiments ContentOps Rules

## General Instructions

- Strictly follow the **Microsoft + Google Developer Documentation Style Guides**.
- Write in second-person, active voice, with short and declarative sentences.
- Avoid anthropomorphizing AI or documentation systems (e.g., avoid "The system believes," "AI thinks," etc.).
- Every Markdown (`.md`) file must begin with a single H1 heading matching the filename exactly (kebab-case converted to title case).
- Always provide complete content; never generate placeholder or lorem-ipsum content.
- Clearly mark sections that are intentionally left incomplete, providing a clear reason.

## Documentation Structure

Use the following structured outline for all documentation unless explicitly instructed otherwise:

1. **Overview**  
   - Concise summary of document purpose (1–3 sentences).
2. **Why It Matters**  
   - Explicit business or technical rationale for the task or topic.
3. **Audience, Scope & Personas**  
   - Clearly defined target audience, roles, and scenarios.
4. **Prerequisites**  
   - Technical, access-related, or knowledge-based preconditions.
5. **Security & Compliance**  
   - Explicit security risks, recommended mitigations, and relevant compliance standards (ISO 27001, GDPR, SOC2).
6. **Tasks & Step-by-Step Instructions**  
   - Clearly numbered or bulleted steps for task completion.
7. **Access Control & Permissions**  
   - Recommended role-based access (RBAC) settings or permissions guidelines.
8. **Examples & Templates**  
   - Practical, actionable examples, including ✅ / ❌ comparisons and visual references or code snippets.
9. **Known Issues & Friction Points**  
   - Clearly identified common problems users might encounter, with immediate workarounds.
10. **Tips & Best Practices**  
    - Recommendations to enhance user experience, productivity, or efficiency.
11. **Troubleshooting**  
    - Clear solutions to commonly encountered issues and errors.
12. **Dependencies & Escalation**  
    - Identify system dependencies, related documents, or escalation paths clearly.
13. **Success Metrics & Outcomes**  
    - Defined indicators of successful task completion or measurable improvements.
14. **Resources & References**  
    - Curated internal/external links, further reading, and authoritative references.
15. **Last Reviewed / Last Updated**  
    - Include a clear timestamp of last review/update and responsible author/team.

## Security and Privacy Rules

- Never include sensitive data (e.g., API keys, passwords, tokens) directly in documentation.
- Always instruct users to follow best practices for credential management (vaults, secrets management).
- Clearly document secure handling, storage, and disposal of data and credentials.
- Include explicit compliance standards when referencing data handling.

## Formatting Rules

- Use clean, semantic Markdown syntax with appropriate heading levels (`##`, `###`, etc.).
- Include clearly labeled code blocks and image placeholders as appropriate.
- Keep tables, lists, and headings consistently structured for readability.
- Clearly highlight ✅ / ❌ examples using bullet points or tables for quick visual scanning.

## File Naming and Structure Conventions

- Use lowercase kebab-case exclusively for filenames (e.g., `communication-metrics-dashboard.md`).
- Ensure all documentation files use the `.md` extension.
- Every directory must contain a clearly informative `README.md`.

## Commit and Workflow Rules

- **Branching:**
  - Never create or switch Git branches unless explicitly instructed by a direct user command.
  - Work strictly within the instructed branch context.
- **Commits:**
  - Stage changes clearly (`git add`).
  - Commit frequently, with descriptive commit messages summarizing changes made.
  - If pre-commit checks fail, resolve all issues before recommitting.
- **Repository State:**
  - Run `git status` before and after tasks to confirm a clean working state.
  - Always ensure the repository remains clean post-task.

## Pull Request Standards

All PRs you generate must strictly follow this format:

- **Summary:** Concise description of all changes.
- **Standards:** Explicit mention of documentation structure, style guides, and formatting rules followed.
- **Citations:** Clearly cite all file paths and line numbers changed using:

【F:<file_path>†L<line_start>-L<line_end>】

- **Security Check Confirmation:** Confirm explicitly if security/compliance sections were reviewed and included.
- **Status of Checks:** Confirm clearly that linting, structure validation, and Markdown checks have passed.

## Programmatic Validation Checks

- Before committing documentation changes, always run any available Markdown linters, structural validators, or test scripts in the repo.
- Explicitly document that checks have passed, or clearly report and rectify any validation errors.

## Terminal Interaction and Task Flow

- Always wait until all terminal commands have successfully completed before proceeding.
- Explicitly report terminal command completion and status clearly in task responses.
- Validate the working directory’s clean state (`git status`) explicitly at the end of each task.

## Custom Rule Precedence and Overrides

- Instructions in this `AGENTS.md` file have global scope and apply to the entire repository unless explicitly overridden by another `AGENTS.md` file in a subdirectory.
- If conflicts arise between `AGENTS.md` files, instructions in the more deeply nested file take precedence.
- Direct system or user prompt instructions always override these file-based instructions.

## Escalation Path (Workflow Issues)

If you encounter workflow ambiguity or issues not covered by this document:

- Explicitly request clarification or approval from the user before proceeding.
- Do not assume instructions; wait for explicit confirmation.

## Review and Update Schedule

- Regularly review and update this `AGENTS.md` quarterly, or immediately after significant workflow or security policy changes.
- Clearly document all updates with date-stamped log entries at the end of this file.

---

## Revision Log
- **2025-07-30:** Initial full-structure definition aligned with Microsoft + Google Developer Documentation Standards, Security Practices, and enterprise documentation best practices.

🔍 Why this refined AGENTS.md is better:

Explicit Security: Clearly integrated data security and compliance guidance.

Workflow Clarity: Clearly structured and user-centric instructions.

Future-Proof: Regular update cadence, explicit revision log.

Enterprise-Friendly: Tailored for easy adoption and scalability.



---

