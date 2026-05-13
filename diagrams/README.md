# Diagrams

This directory contains public-safe Mermaid source diagrams. They intentionally use generic labels and placeholders instead of real infrastructure identifiers.

The diagrams represent the designed/deployed system described in the final technical paper. They are portfolio architecture diagrams, not a promise that every deployment script, private Google Apps Script project, Deadline Repository setting, or raw operation log is present in this repository.

Files:

- `system-architecture.mmd`: high-level infrastructure architecture.
- `render-submission-workflow.mmd`: user and Deadline submission workflow.
- `data-flow.mmd`: data movement between reservation, UI, MongoDB, Deadline, Workers, and NAS.
- `troubleshooting-flow.mmd`: operator triage flow for failed renders.

Recommended usage:

- Render these diagrams in GitHub Markdown or a Mermaid-compatible tool.
- Do not replace placeholders with real server names, IPs, paths, sheet URLs, or account names.
- If screenshots from `agent_reference/` are used later, redraw them as sanitized Mermaid diagrams unless every private value has been removed.
