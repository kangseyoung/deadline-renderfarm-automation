# Implementation

This document maps the final branch code to the public portfolio architecture. It separates source that is present in this repository from features that are only documented in the technical paper or still need verification.

## Snapshot Scope

The repository is strongest as a public source snapshot for:

- PySide UI experiments and login/submission flow.
- MongoDB-backed auth and reservation lookup scripts.
- Deadline job/plugin info generation.
- Maya and Blender DCC adapter structure.
- Public architecture, operations, and troubleshooting documentation.

The deployed lab infrastructure, raw Deadline logs, private Google Apps Script project, and some operator scripts are documented in the technical paper or private references, but are not included in this public snapshot.

## Source Layout

```text
gpclean/
├── main.py
├── logging_setup.py
├── installer.py
├── ui/
│   ├── login/
│   ├── main/
│   ├── file_drop/
│   └── image/
├── backend/
│   └── authDB/
└── gpclean_submit/
    ├── cli.py
    ├── core/
    ├── dcc/
    ├── examples/
    └── ui/
```

There is also a duplicated `blender/gpclean/` tree. Its intended ownership relative to `gpclean/` needs verification before refactoring.

## Present in Repository

### UI Layer

- `gpclean/main.py`
  - Creates or reuses a Qt application.
  - Launches `LoginView`.
  - Wires login data to `Receiver` and `SubmissionDataModel`.

- `gpclean/ui/login/login_view.py`
  - Loads the login `.ui` file and emits login data.

- `gpclean/ui/login/login_controller.py`
  - Authenticates a user against MongoDB.
  - Hashes the entered password with SHA-256 and compares it to stored hashes.
  - Opens the next UI flow after successful login.

- `gpclean/ui/file_drop/file_drop_view.py`
  - Loads the file drop UI.
  - Displays current and upload directory labels.
  - Accepts dropped file URLs, but the current drop handler is minimal.

- `gpclean/ui/main/model.py`
  - Detects the active DCC by attempting Maya, Blender, then Nuke imports.
  - Reads current scene path from Maya or Blender.
  - Builds an output path using logged-in user/time data.
  - Reads reservation entries from MongoDB.

- `gpclean/ui/main/view.py`
  - Loads the main submission UI.
  - Populates current path, output path, user field, filename, reservation list, and icons.
  - Connects the send-to-Deadline button.

- `gpclean/ui/main/controller.py`
  - Placeholder class. Controller behavior needs verification.

### Deadline Submission Layer

- `gpclean/gpclean_submit/cli.py`
  - Main Python API for `submit_job(dcc, name, **kwargs)`.
  - Selects Maya or Blender adapter.
  - Runs adapter validation and common checks.
  - Builds job/plugin info and submits through Deadline.

- `gpclean/gpclean_submit/core/config.py`
  - Holds default `deadlinecommand` path, pool, group, priority, and chunk size.
  - Should later be environment-configured for public-safe deployment.

- `gpclean/gpclean_submit/core/deadline.py`
  - Writes temporary `job_info` and `plugin_info` files.
  - Runs `deadlinecommand SubmitJob`.
  - Returns success flag, stdout, and stderr.

- `gpclean/gpclean_submit/core/job_builder.py`
  - Builds Deadline job info.
  - Uses `MayaBatch` for Maya and `Blender` for Blender.
  - Adds frames, frame step, chunk size, priority, pool, group, output, and optional environment key-values.

- `gpclean/gpclean_submit/core/preflight.py`
  - Checks for scene path presence.
  - Checks frame range validity.
  - Additional NAS/UNC validation needs verification.

- `gpclean/gpclean_submit/core/types.py`
  - Defines `SceneInfo`, `RenderSettings`, and `JobSpec` dataclasses.

### DCC Adapters

- `gpclean/gpclean_submit/dcc/maya_adapter.py`
  - Uses `maya.cmds`.
  - Reads scene file, project root, renderable camera, render layers, renderer, Maya version, frame range, image prefix, and output directory.
  - Loads or validates Arnold/mtoa when the renderer indicates Arnold.

- `gpclean/gpclean_submit/dcc/blender_adapter.py`
  - Uses `bpy`.
  - Reads scene file, render engine, frame range, frame step, output path, file extension, and Blender version.

The adapter design matches the final paper's DCC adapter concept. Support for Houdini/Nuke is not implemented in the submission package.

### Backend / Auth / Reservation Components

- `gpclean/backend/authDB/db.py`
  - Creates a MongoDB client.
  - Exposes reservation and auth collections.
  - Reads MongoDB URI, database, and collection names from environment variables.

- `gpclean/backend/authDB/sheetToMongo.py`
  - Reads Google Sheets using `gspread` and `oauth2client`.
  - Upserts reservation slots into MongoDB.
  - Reads service-account path and sheet names from environment variables.

- `gpclean/backend/authDB/auth_hashed_pw.py`
  - Seeds dummy fixture auth data into MongoDB for local testing only.
  - Uses placeholder sample IDs/passwords only; deployment credentials must remain private.

- `gpclean/backend/authDB/exel_creator.py`
  - Generates an Excel auth workbook from dummy fixture data for local testing only.
  - Deployment environments must replace these fixtures with environment-specific private data outside the public repository.

### Scripts and Helper Tools

- `ShaderMain.py` and `ShaderSetup.py`
  - Maya shader automation tools for creating and connecting texture nodes.
  - Useful as supporting DCC pipeline work, but not part of the core Deadline render submission path.

- `userSetup.py`
  - DCC startup hook. Exact runtime behavior should be verified in Maya.

## Documented in Paper but Not Included in Public Snapshot

- 20 Worker PC deployment inventory and live Deadline Worker configuration.
- Deadline Repository configuration and Deadline database deployment files.
- Google Apps Script project source.
- Arnold license environment setup script.
- OCIO reset script.
- Raw Deadline benchmark logs and failed-task logs.
- Private Notion operation database/log templates.

These items should be described as deployed or documented only when tied to the final technical paper, and not presented as files available in this repository.

## Needs Verification

- UI button call path to `on_click_send_to_deadline()` appears to omit required `dcc` and `job_name` arguments.
- Full MongoDB job/status schema is not present in the final branch.
- Google Apps Script source is not present in the final branch.
- OCIO reset and Arnold license setup scripts are described in the paper but not present in the repository.
- Deadline Repository and Worker configuration are not represented as sanitized config files.
- The duplicated `blender/gpclean/` tree may need consolidation, but files were not moved or deleted in this task.
- The committed workbook artifacts are confirmed dummy fixture data; deployment-specific workbooks must remain private and untracked.
