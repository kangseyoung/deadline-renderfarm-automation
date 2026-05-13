# Screenshots

No screenshots are committed by default. The private reference directory contains images and exports that may include sensitive paths, user identifiers, logs, server names, or UI state.

During this documentation pass, reference images were inspected only as private visual material. At least one workflow image included a private account label, so the images should not be copied directly into the repository.

## Recommended Screenshots to Add Later

Add only manually redacted screenshots:

- `reservation-sheet-redacted.png`: Google Sheets reservation view with all user IDs, URLs, and private sheet names hidden.
- `pyside-login-redacted.png`: PySide login screen without real user IDs.
- `pyside-submit-redacted.png`: submission UI with placeholder paths.
- `deadline-monitor-redacted.png`: Deadline Monitor job list with Worker names, job names, paths, users, and timestamps redacted.
- `worker-status-redacted.png`: Worker status view with internal hostnames removed.
- `nas-output-redacted.png`: output folder layout using placeholder names only.

## Redaction Rules

Before publishing screenshots, remove or blur:

- IP addresses.
- UNC paths.
- internal server names.
- student IDs.
- account names.
- private account labels.
- Google Sheet URLs.
- Google Apps Script project URLs.
- MongoDB URIs.
- license server values.
- Deadline Worker hostnames.
- raw render logs with private paths.
- local filesystem paths.
- browser address bars, bookmarks, and tabs if they reveal private services.
- timestamps if they identify private schedules or users.

## README Placement

Suggested placements:

- Architecture section: system diagram rendered from Mermaid, not a private screenshot.
- Key Features section: redacted PySide UI screenshot.
- Results section: redacted Deadline Monitor screenshot if benchmark logs are sanitized.
- Troubleshooting section: redacted failed-task log screenshot only if all private values are removed.
