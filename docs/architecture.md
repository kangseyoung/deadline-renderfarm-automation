# Architecture

This document describes the public-safe architecture of the Deadline Render Farm Automation System. Real infrastructure values are intentionally replaced with placeholders.

## High-Level Flow

```text
User
  -> PySide Submission UI
  -> MongoDB auth/reservation lookup
  -> Deadline job_info/plugin_info generation
  -> deadlinecommand SubmitJob
  -> Deadline Repository / Database
  -> Deadline Workers
  -> NAS input/output paths
  -> Deadline Monitor / operational review
```

## Main Components

## Public Source Snapshot Structure

The review-friendly source layout is under `src/`.

`src/` is a public portfolio snapshot for interview and code review. It does not replace the original runtime package under `gpclean/`. The original package is kept for project history and to avoid breaking existing imports.

```text
src/
  app_entry/     # copied original application entry point for reference
  ui/            # PySide UI layer
  reservation/   # MongoDB auth/reservation access
  submission/    # Deadline job/plugin info and SubmitJob logic
  config/        # environment placeholder settings
  main.py        # review-friendly system flow summary
```

### PySide Submission UI

The UI layer handles login, scene context, file selection, and render submission entry points. The public source snapshot includes the UI package under `gpclean/ui/`.

In the `src/` snapshot, this maps to `src/ui/`.

### UI Layer

The UI layer includes PySide login, file drop, and render submission views/controllers. Qt Designer `.ui` files define widget layouts and are loaded by Python view/controller code.

### MongoDB Reservation/Auth Data

MongoDB is used for user authentication and reservation/status-related data. Connection settings are read from environment variables:

- `MONGODB_URI`
- `MONGODB_DATABASE`
- `MONGODB_AUTH_COLLECTION`
- `MONGODB_RESERVATION_COLLECTION`

In the `src/` snapshot, this maps to `src/reservation/`.

### Reservation/Auth Layer

This layer checks user authentication and reservation data before a render job is submitted. Public examples use placeholders and environment variables instead of internal database values.

### Google Sheets Reservation Workflow

The project used Google Sheets / Apps Script for reservation operations. The private Apps Script project is not included. The public repository keeps only the Python sync direction and documentation, with service-account paths supplied through `GOOGLE_SERVICE_ACCOUNT_JSON`.

### Deadline Submission Layer

The `gpclean/gpclean_submit/` package builds Deadline-compatible submission files:

- `job_info`
- `plugin_info`

It then calls:

```text
deadlinecommand SubmitJob <job_info> <plugin_info>
```

The package includes Maya and Blender adapters for collecting scene file, frame range, renderer, version, output path, and camera data where available.

In the `src/` snapshot, this maps to `src/submission/`.

### Render Farm Worker Layer

After submission, Deadline Workers pick up tasks from the Repository/Database, read scene data and assets, execute rendering, and write output to shared storage.

### Deadline Repository / Workers

The final project used a Deadline Repository / Database / Worker model. The public repository does not include the full private Repository configuration or raw Worker logs, but the workflow is documented because it was central to the project.

### NAS Shared Storage

Distributed rendering requires all Workers to resolve the same scene and output paths. The project used a NAS/UNC path policy:

```text
\\<nas-server-ip>\<internal-path>\input\<student-id>\<date>
\\<nas-server-ip>\<internal-path>\output\<student-id>\<date>
```

These are placeholder examples only.

### Storage/NAS Layer

The storage layer provides shared input and output paths that must be reachable from UI machines and all Deadline Workers. Public docs use placeholder UNC paths only.

### Status/Log Check Flow

Operators check job state through Deadline Monitor, Worker status, task logs, and project troubleshooting notes. This closes the loop after submission and helps diagnose Worker, path, license, or render engine failures.

## Implemented vs. Private Deployment Artifacts

Implemented in public source:

- PySide UI structure
- MongoDB auth/reservation access
- Google Sheets sync script with environment-based credential path
- Deadline job/plugin info generation
- `deadlinecommand SubmitJob` wrapper
- Maya/Blender DCC adapters
- Public troubleshooting and operation documentation

Not included publicly:

- Real Deadline Repository settings
- Private Apps Script source
- Raw Deadline logs
- Real NAS paths/IPs/license server values
- Unredacted screenshots
- Private benchmark artifacts

## Operational Data Flow

1. User reserves a render slot.
2. Reservation data is synchronized into MongoDB.
3. User logs in through the PySide UI.
4. UI gathers scene and render settings.
5. Submission package creates Deadline `job_info` and `plugin_info`.
6. `deadlinecommand SubmitJob` submits the render job.
7. Deadline Workers read scene/assets from NAS and write output back to NAS.
8. Operator reviews status through Deadline Monitor and project troubleshooting logs.
