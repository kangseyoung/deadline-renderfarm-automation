# Security Cleanup

This document records the public-repository security cleanup approach. It intentionally does not expose any secret value.

## What Was Checked

The repository was scanned for common sensitive patterns:

- `password`, `passwd`, `pwd`
- `secret`, `token`
- `api_key`, `API_KEY`, `access_key`, `private_key`
- MongoDB connection strings and database URIs
- Google credential references
- Deadline Repository paths
- IP addresses
- student/account identifiers
- internal machine names
- UNC/NAS paths

## Cleanup Actions

- Hardcoded MongoDB configuration was moved to environment variables.
- Google service-account JSON path was moved to `GOOGLE_SERVICE_ACCOUNT_JSON`.
- Local user-specific Python/Maya paths were moved to environment variables.
- Public sample student IDs/passwords were replaced with placeholders.
- Password hash logging and full login dictionary logging were removed.
- `.env.example` was expanded as a placeholder-only configuration template.

## Environment Configuration

Create a private `.env` file locally from `.env.example`.

Never commit:

- `.env`
- service-account JSON files
- license files
- private keys or certificates
- real NAS/UNC paths
- real IP addresses
- real account names or student IDs
- raw logs or unredacted screenshots

## If a Secret Was Already Exposed

Assume any exposed password, token, API key, credential file, license value, or database URI is compromised.

Required response:

1. Revoke or rotate the exposed value immediately.
2. Remove the value from current files.
3. Check GitHub secret scanning alerts.
4. Decide whether history cleanup is required.

## Git History Cleanup

History rewrite was not performed automatically because it can disrupt collaborators and remote branches.

If the repository owner decides history cleanup is required, use one of these tools after backing up the repository:

- `git filter-repo`
- BFG Repo-Cleaner

Typical process:

1. Clone a fresh copy of the repository.
2. Run the chosen history-cleanup tool against the specific file/path/pattern.
3. Inspect the rewritten history.
4. Force-push only after confirming the impact.
5. Ask GitHub Support to purge cached sensitive blobs if necessary.

Do not rely on history rewrite as a substitute for secret rotation.
