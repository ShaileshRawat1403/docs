# Markdown Lint Pipeline

## Overview
A short process to automatically check Markdown files for style and formatting issues before merging.

## Why It Matters
Early linting ensures consistent documentation quality and catches errors quickly.

## Audience, Scope & Personas
Technical writers and DevOps teams implementing documentation automation.

## Prerequisites
Access to a CI system and repository with Markdown files.

## Security & Compliance
Linting tools should run with minimal permissions and without exposing source code externally.

## Tasks & Step-by-Step Instructions
1. Set up a CI job using a linting action or container.
2. Specify file globs for `.md` files.
3. Fail the job if linting issues appear and require resolution before merging.

## Access Control & Permissions
Limit pipeline configuration changes to maintainers. Developers can view lint results for their pull requests.

## Examples & Templates
✅ Configure `markdownlint-cli` for common style rules.
❌ Ignore warning messages that highlight readability problems.

## Known Issues & Friction Points
Lint rules may conflict with custom styles. Adjust configuration to match your guide.

## Tips & Best Practices
Run linting locally before committing to save CI time.

## Troubleshooting
If the lint job fails unexpectedly, check version compatibility and rule configurations.

## Dependencies & Escalation
Consult with documentation leads when changing lint rules. Escalate persistent failures to DevOps.

## Success Metrics & Outcomes
Reduced formatting errors and cleaner merges.

## Resources & References
Example CI workflow files and official markdownlint documentation.

## Last Reviewed / Last Updated
2025-07-30
