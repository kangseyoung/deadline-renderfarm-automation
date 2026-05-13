# Operation Guide

This guide describes the public-safe operating model. It intentionally avoids real internal paths, server names, IP addresses, account names, and student IDs.

## Expected User Workflow

1. Reserve an available render slot in the shared reservation system.
2. Work from a lab machine during the reserved time.
3. Confirm scene files, caches, and assets are stored under the approved NAS/UNC layout.
4. Open the PySide submission UI.
5. Log in with the assigned user identifier.
6. Review scene path, output path, frame range, renderer, pool/group, and other render settings.
7. Submit the job to Deadline.
8. Monitor progress in Deadline Monitor.
9. Collect output from the NAS output location.

## Reservation Workflow

The final technical paper describes a reservation workflow based on Google Sheets and Google Apps Script. The public source snapshot includes a Python Google Sheets-to-MongoDB sync script; the private Apps Script project is not included. In the designed workflow, synchronized reservation data lets the UI check whether a user is eligible to submit during the selected time.

Public placeholder:

```text
Reservation sheet: <google-sheet-url>
User identifier: <student-id>
```

Operationally, reservations should define:

- user or team identifier.
- date and time block.
- license or Worker allocation, if applicable.
- expected DCC and renderer.
- operator notes for long overnight renders.

## Render Submission Workflow

The branch code supports Deadline submission through `gpclean/gpclean_submit/`:

1. Select DCC adapter: Maya or Blender.
2. Gather scene and render settings from the DCC API.
3. Run common preflight checks.
4. Build Deadline job info and plugin info.
5. Call `deadlinecommand SubmitJob`.
6. Use Deadline Monitor to track job and task state.

## Worker Setup Assumptions

The final paper describes 20 Windows Worker PCs. Public docs should assume:

- Deadline Worker is installed and connected to the Repository.
- Workers can access the NAS shared storage through the approved UNC paths.
- Worker permissions allow Deadline to read scenes/assets and write outputs.
- Arnold license variables are configured where Maya/Arnold rendering is required.
- OCIO configuration is consistent for MayaBatch.
- Firewall rules allow required Deadline, MongoDB, and license-server communication.

Use placeholders for any infrastructure values:

```text
Repository: \\<internal-server-name>\<internal-path>
NAS: \\<nas-server-ip>\<internal-path>
License server: <license-server-ip>
MongoDB: <mongodb-uri>
```

## Checks Before Submitting a Job

- Scene is saved.
- Scene path is under the approved NAS/UNC location.
- All referenced assets and caches are accessible from Workers.
- Output path points to the approved NAS output area.
- Frame range and frame step are correct.
- Renderer is supported by the target Worker group.
- Maya Arnold jobs have mtoa loaded and license variables configured.
- Blender jobs use a Deadline-compatible Blender version.
- Worker pool/group choice matches the job requirements.

## Monitoring Deadline Job Status

In Deadline Monitor:

- Confirm the job is queued or rendering.
- Check assigned Worker names and task progress.
- Inspect failed tasks first, not only the parent job status.
- Review task logs for missing paths, license errors, plugin load errors, OCIO errors, or render engine failures.
- Requeue only after the root cause is corrected.

## Error Recording

The final paper describes a Notion-based error log workflow. For public documentation, the recommended sanitized process is:

1. Open the failed task log in Deadline Monitor.
2. Record the DCC, renderer, frame/task, Worker group, failure category, and sanitized error summary.
3. Remove private paths, user IDs, server names, and license values.
4. Add the resolution steps and whether the job was requeued successfully.

Suggested error categories:

- NAS/UNC path.
- Arnold license.
- OCIO/color management.
- MongoDB/reservation.
- Deadline Repository access.
- Worker offline.
- DCC plugin/version mismatch.
