# Troubleshooting

This guide is public-safe and uses placeholders instead of real infrastructure values.

## Triage Flow

1. Check whether the job reached Deadline.
2. Check whether Workers are online and assigned.
3. Open the failed task log in Deadline Monitor.
4. Classify the error: database, Repository, Worker, license, OCIO, NAS/path, or user submission.
5. Fix the root cause.
6. Requeue a small frame range before requeueing the full job.

## MongoDB Connection Failure

Symptoms:

- UI login fails.
- Reservation list does not load.
- Reservation sync script cannot write records.

Checks:

- Confirm `<mongodb-uri>` is reachable from the UI machine.
- Confirm firewall and bind settings allow the expected client.
- Confirm the expected database and collections exist.
- Confirm credentials are loaded from environment variables or a private config file.

Resolution:

- Restart MongoDB service if appropriate.
- Correct bind/firewall settings.
- Verify collection names used by the UI and sync script.

## Deadline Repository Access Failure

Symptoms:

- Worker cannot start or connect.
- Job submission fails after `deadlinecommand SubmitJob`.
- Workers report missing Repository or plugin files.

Checks:

- Confirm Repository share is reachable through `\\<internal-server-name>\<internal-path>`.
- Confirm user/Worker permissions.
- Confirm Deadline client points to the correct Repository.

Resolution:

- Restore share permissions.
- Reconnect the Repository path.
- Restart Deadline Worker after path or permission changes.

## Worker Offline

Symptoms:

- Job stays queued.
- Only a subset of frames render.
- Deadline Monitor shows Workers offline or stalled.

Checks:

- Confirm the PC is powered on and network-connected.
- Confirm Deadline Worker is running.
- Confirm the Worker belongs to the expected pool/group.
- Confirm Deep Freeze or reboot policy did not reset required settings.

Resolution:

- Restart Deadline Worker.
- Reapply required environment settings.
- Reconnect NAS path if needed.
- Requeue failed tasks after the Worker is healthy.

## Arnold License Failure

Symptoms:

- MayaBatch starts but Arnold render fails.
- Logs mention license checkout failure or missing Arnold/mtoa authorization.

Checks:

- Confirm the license server placeholder `<license-server-ip>` is reachable.
- Confirm required variables are set for the Worker:
  - `ADSKFLEX_LICENSE_FILE`
  - `solidangle_LICENSE`
  - `ARNOLD_PLUGIN_PATH`
  - `MTOA_EXTENSIONS_PATH`
  - `MTOA_TEMPLATES_PATH`
- Confirm the Maya/Arnold version matches the available license policy.

Resolution:

- Reapply the Arnold license environment setup.
- Restart Deadline Worker or reboot if system environment variables changed.
- Test a small frame before requeueing the full job.

## OCIO Config Failure

Symptoms:

- MayaBatch fails with an OCIO config error.
- Render output has unexpected color management behavior.
- Logs mention a missing or unreadable `config.ocio`.

Checks:

- Confirm the Worker points to the expected OCIO config.
- Confirm the config path is accessible to Deadline Worker.
- Confirm user-specific Maya preferences are not overriding the shared config.

Resolution:

- Run the OCIO reset process described by the operator guide.
- Remove stale user-level OCIO overrides.
- Restart MayaBatch/Worker and test one frame.

Repository note: the final paper describes OCIO reset tooling, but the script was not found in the final branch and needs verification.

## NAS / UNC Path Issues

Symptoms:

- Missing texture, cache, Alembic, or scene references.
- Render works locally but fails on Workers.
- Output is written to the wrong local path.

Checks:

- Scene path starts with `\\<nas-server-ip>\<internal-path>`.
- Output path uses the approved NAS output location.
- Asset paths are not local drive paths.
- Worker account has read/write permission.

Resolution:

- Convert local paths to UNC paths.
- Relink missing assets through the NAS share.
- Re-run a small test frame from a Worker.

## User Submission Path Errors

Symptoms:

- UI shows an unexpected current path.
- Output path does not include the expected user/date layout.
- Deadline job submits but cannot find scene or output folder.

Checks:

- Confirm the scene is saved before submission.
- Confirm the UI detected the correct DCC.
- Confirm output folder exists or can be created.
- Confirm the selected reservation/user context is correct.

Resolution:

- Save the scene under the approved NAS project folder.
- Reopen the UI after the scene path is corrected.
- Re-submit with a small frame range.

## Path Validation Failures

The current repository includes minimal preflight checks for empty scene path and invalid frame range. Full validation should also check:

- UNC path prefix.
- output directory writability.
- asset reference accessibility.
- frame range limits.
- supported renderer and DCC version.

These stronger validations are recommended future work unless verified elsewhere.

