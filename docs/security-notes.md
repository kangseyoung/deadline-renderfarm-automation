# Security Notes

This project documents a real lab-style infrastructure workflow. Public documentation must be sanitized before publishing.

## Values That Must Stay Private

Never commit or publish:

- real IP addresses.
- NAS paths.
- Deadline Repository paths if they reveal internal servers.
- license server addresses.
- MongoDB URIs.
- Google Sheet URLs.
- Google Apps Script project links.
- passwords.
- API keys.
- OAuth client IDs or secrets.
- service account JSON files.
- student IDs.
- private account names.
- internal server names.
- raw Deadline logs containing private paths or users.

## Placeholder Policy

Use these placeholders in public docs:

- `<nas-server-ip>`
- `<license-server-ip>`
- `<mongodb-uri>`
- `<google-sheet-url>`
- `<student-id>`
- `<internal-path>`
- `<internal-server-name>`
- `<private-account>`
- `<secret>`

## Local Reference Files

The `agent_reference/` directory is outside the repository and must remain outside the repository. It may contain private papers, Notion exports, screenshots, diagrams, logs, links, tokens, account data, and internal paths.

Do not copy reference files into this repository. Summarize them only after redaction.

## Environment Variables

Runtime configuration should come from environment variables or a private, ignored config file.

Recommended variables are listed in `.env.example`:

- `MONGODB_URI`
- `DEADLINE_COMMAND`
- `DEADLINE_REPOSITORY`
- `NAS_ROOT`
- `GOOGLE_SHEET_URL`
- `GOOGLE_SERVICE_ACCOUNT_JSON`
- `ARNOLD_LICENSE_SERVER`
- `OCIO_CONFIG`

## Public Auth Fixtures

Auth workbooks and seed scripts in this public repository must contain only dummy fixture data for local testing. They must not contain real users, real passwords, real password hashes, student IDs, private account names, or deployment credentials.

Deployment environments must replace these fixtures with environment-specific private data stored outside the public repository.

## Public Release Checklist

Before publishing:

- Search for real IP addresses and private hostnames.
- Search for student ID patterns and account names.
- Search for `mongodb://`, Google OAuth values, API keys, and service account material.
- Search for internal UNC paths, Deadline Repository names, license server values, and NAS share names.
- Verify screenshots do not show paths, server names, IDs, logs, or URLs.
- Verify diagrams use placeholders only.
- Verify `.env`, credentials, workbooks, logs, and generated caches are ignored.
- Confirm auth workbooks and seed scripts contain only dummy fixtures.
- Confirm the final paper is not committed unless redacted.
- Confirm paper-only deployment features are labeled as "documented in the technical paper" or "not included in this public source snapshot".
- Confirm raw benchmark and troubleshooting logs are either excluded or fully redacted.
- Confirm `.gitignore` covers future generated files, even if older generated artifacts are still tracked in the current history.
