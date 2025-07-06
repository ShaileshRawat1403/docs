# Confluence Sync Explainer

## Overview

This document outlines a workflow for synchronizing Confluence pages with GitHub repositories. The process ensures that documentation maintained in Confluence remains consistent with documentation in GitHub. It covers setup, best practices, and troubleshooting tips for enterprise environments.

## Audience

This guide is for technical writers, internal communications managers, and DevOps teams responsible for maintaining up-to-date documentation across collaboration platforms.

## Objective

The objective is to establish a repeatable process that automatically exports Confluence content, converts it to Markdown, and commits it to a GitHub repository. By automating this workflow, teams can centralize content management and reduce manual effort.

## Usage Scenarios

- **Centralizing documentation:** Consolidate all internal docs into GitHub to streamline version control.
- **Migration projects:** Move existing Confluence spaces to GitHub as part of a broader documentation strategy.
- **Continuous updates:** Keep Confluence content in sync with GitHub, ensuring both platforms reflect the latest changes.

## Best Practices

1. **Use API tokens.** Create dedicated API tokens with limited permissions for automation tasks. Store them securely in your CI/CD system.
2. **Validate Markdown output.** After conversion, run markdownlint to maintain consistent formatting.
3. **Schedule regular syncs.** Set a daily or weekly schedule depending on how frequently content changes.
4. **Review diffs carefully.** Treat updates from Confluence like any other pull request and perform peer reviews before merging.
5. **Communicate changes.** Notify stakeholders when the workflow syncs large updates, especially during migration phases.

## Workflow Steps

1. **Export Confluence pages.** Use the Confluence API to export pages as XHTML or storage format.
2. **Convert to Markdown.** Pipe the export through a converter such as `pandoc` or specialized tools like `confluence-pull`.
3. **Commit to GitHub.** Use a bot account to create a pull request containing the converted Markdown files.
4. **Review and merge.** Review the pull request, apply any necessary edits, and merge when approved.
5. **Trigger downstream actions.** Optionally run additional workflows, such as link checking or PDF export.

## Troubleshooting

- **Missing images:** Ensure that attachments referenced in Confluence are also exported and uploaded to GitHub.
- **Formatting issues:** Adjust your conversion settings to preserve lists, tables, and other formatting elements.
- **Large pages:** Split large Confluence pages into smaller Markdown files to simplify reviews.

## Additional Resources / References

- Confluence REST API documentation
- GitHub Actions documentation
- pandoc user guide

## Detailed Setup

### Prerequisites

Before configuring the workflow, ensure that you have administrator access to both Confluence and GitHub. Confirm that your Confluence instance allows API access and that your GitHub repository has workflow permissions enabled. If your organization uses a proxy or firewall, coordinate with your network team to allow outbound requests to both services.

### Environment Variables

Store sensitive values such as API tokens, user credentials, or webhook URLs in your CI/CD platform's secure storage. Many teams use GitHub Secrets to manage these values. Name the secrets clearly, for example, `CONFLUENCE_TOKEN` and `DOCS_BOT_TOKEN`, so that the workflow file remains readable.

### Repository Structure

Create a dedicated folder, such as `confluence-import`, within your repository. This folder will store all Markdown files generated from Confluence. Organize the files by space or project, mirroring your Confluence hierarchy to help writers quickly find content.

## Implementation Steps in Depth

1. **Connect to Confluence.** Use a script or tool that authenticates to Confluence via REST API. Popular options include `curl`, Python's `atlassian-python-api` package, or specialized utilities developed in-house.
2. **Export content as storage format.** The storage format preserves formatting elements like headings, tables, and lists. Retrieve pages recursively to include all child pages.
3. **Transform to Markdown.** Convert the storage format to Markdown. If you use `pandoc`, consider customizing the conversion template to match your organization's style guidelines. Test the output against typical Confluence pages, including pages with complex tables or macros.
4. **Manage attachments.** Many Confluence pages rely on images or other attachments. Update your script to download these files, store them under an `assets` folder, and update links in the Markdown accordingly.
5. **Create a pull request.** After converting the pages, push them to a branch and open a pull request using a bot account. Include a summary of changes to help reviewers understand what content has been added or updated.
6. **Review and merge.** Ensure the pull request triggers your markdown linter, link checker, and any other validation workflows. Address formatting issues before merging to the main branch.

## Security Considerations

Keeping documentation secure is as important as keeping code secure. Limit token scope to read-only access where possible. Monitor logs for suspicious activity, such as repeated failed login attempts. Implement rate limiting to prevent accidental API overuse. If your organization enforces multi-factor authentication, confirm that your automation method aligns with security policies.

## Scheduling Strategies

A simple approach is to run the synchronization workflow nightly, capturing changes from the previous day. For teams that update Confluence more frequently, an hourly schedule may be better. Evaluate your CI minutes and repository activity to find a balance. Some teams use webhooks to trigger synchronization when authors update Confluence pages.

## Onboarding New Teams

Share documentation explaining how the sync works and how to troubleshoot common issues. Provide a checklist for new projects joining the process: verify permissions, confirm page hierarchy, and identify any content that requires manual review. Encourage teams to maintain consistent templates in Confluence to ensure smooth conversion to Markdown.

## Maintenance and Monitoring

Periodically review the script or workflow to accommodate Confluence and GitHub API changes. Keep dependencies up to date and pin versions to prevent unexpected behavior. Establish a logging mechanism to track successful runs, skipped pages, and errors. If your organization uses a monitoring platform, integrate alerts for failed syncs so you can respond quickly.

## Troubleshooting Expanded

- **API rate limits:** If you see 429 errors, reduce the frequency of requests or add retry logic with exponential backoff.
- **Permission denied errors:** Double-check that the token has access to the Confluence space or GitHub repository. If using a bot account, verify that it hasn't been disabled.
- **Conflicting changes:** When multiple teams edit the same page, conflicts may arise during conversion. Establish guidelines to resolve conflicts, such as designating page owners.

## Additional Resources / References

- [Confluence REST API](https://developer.atlassian.com/cloud/confluence/rest/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [pandoc User Guide](https://pandoc.org/MANUAL.html)


## Example Implementation

Below is a high-level example of how a team might configure a synchronization workflow using GitHub Actions. The workflow runs nightly, pulls specific pages from Confluence, converts them to Markdown, and opens a pull request with any updates.

```yaml
name: Sync Confluence
on:
  schedule:
    - cron: '0 2 * * *'
jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Export Confluence Pages
        run: |
          python scripts/export_confluence.py --space KEY --token ${{ secrets.CONFLUENCE_TOKEN }}
      - name: Convert to Markdown
        run: |
          pandoc -f html -t gfm exported_page.html -o README.md
      - name: Commit Changes
        run: |
          git config user.name "Docs Bot"
          git config user.email "docs@example.com"
          git add .
          git commit -m "Automated sync" || echo "No changes"
          git push origin HEAD:sync-confluence
      - name: Create Pull Request
        uses: peter-evans/create-pull-request@v5
        with:
          branch: sync-confluence
          title: 'Automated Confluence Sync'
          body: 'This PR contains the latest updates from Confluence.'
```

This example uses a Python script to export pages, but you can adapt it to your preferred language or tool. The main focus is to demonstrate how each step fits together in the workflow.

## Continuous Improvement

As your team becomes more comfortable with the synchronization process, consider adding automated quality checks. For instance, integrate a style guide linter to enforce consistent terminology. You might also introduce a content validation step that checks for broken links or outdated screenshots. Incorporate these checks early to catch issues before they reach production.

## Case Study: Marketing Department Adoption

The marketing department at ExampleCorp relied heavily on Confluence to track campaign plans, metrics, and internal guidelines. When the company shifted to GitHub for content management, the marketing team needed a straightforward way to migrate without losing historical data. By implementing a synchronization workflow similar to the one described in this guide, the department moved over a thousand pages in a matter of weeks. They scheduled weekly syncs to keep active pages current while gradually archiving obsolete ones. The team reported a reduction in duplicate content and improved collaboration with product teams that were already using GitHub.


## Future Enhancements

As your synchronization workflow matures, consider adding a notification step that posts a summary of changes to a shared chat channel. This keeps stakeholders aware of updates without requiring them to monitor GitHub. You can also extend the script to create issues for pages that fail to convert properly, ensuring that broken content is addressed promptly.

When your organization expands to additional documentation platforms, you can reuse much of the same logic for exporting content, converting it to Markdown, and pushing updates to GitHub. Documenting each enhancement thoroughly will help new team members understand the process and contribute improvements.

By following the guidance in this explainer, your team can maintain consistent documentation across platforms with minimal manual intervention. Adjust the workflow as needed to suit your environment, and always perform regular reviews to ensure accuracy.
