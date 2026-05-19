# Troubleshooting

This guide summarizes common failure categories found during the render-farm project. Replace all environment-specific values with local private configuration.

## UNC / NAS Path Issues

Symptoms:

- Worker cannot find the scene file.
- Assets are missing only on some machines.
- Output is written to a local path instead of shared storage.

Checks:

- Confirm scene and output paths use UNC-style shared paths.
- Avoid local drive letters for files that Workers must access.
- Confirm all Workers can read input paths and write output paths.
- Confirm NAS permissions are consistent for lab users and Worker accounts.

## Deadline Worker Permission Issues

Symptoms:

- Worker starts but cannot execute jobs.
- Job stays queued or fails immediately.
- Deadline client configuration path is not writable/readable.

Checks:

- Confirm Worker service/user account has access to Deadline client configuration.
- Confirm firewall allows Deadline Repository / Database communication.
- Confirm Worker appears online in Deadline Monitor.
- Confirm pool/group/limit settings match the submitted job.

## Arnold License Server / Firewall Issues

Symptoms:

- MayaBatch starts but Arnold render fails.
- Logs mention license checkout failure.
- Failure appears only on some Worker PCs.

Checks:

- Confirm license environment variables are configured privately.
- Confirm license server is reachable from every Worker.
- Confirm firewall rules allow required license ports.
- Confirm Maya, Arnold, and mtoa versions match the available license policy.

## Environment Variable Issues

Symptoms:

- MongoDB connection fails.
- Google Sheets sync cannot find credentials.
- Deadline command is not found.
- OCIO or license setup differs by machine.

Required private values should come from `.env` or machine-level environment variables:

- `MONGODB_URI`
- `DEADLINE_COMMAND`
- `DEADLINE_REPOSITORY`
- `NAS_ROOT`
- `GOOGLE_SERVICE_ACCOUNT_JSON`
- `ARNOLD_LICENSE_SERVER`
- `OCIO_CONFIG`

Do not commit actual values.

## NAS Access Permission Issues

Symptoms:

- User can access a path but Worker cannot.
- Output folder is not created.
- Render succeeds locally but fails on Deadline.

Checks:

- Confirm Worker account permissions on NAS input/output folders.
- Confirm project assets are stored under the approved shared path.
- Confirm no scene references point to a local user profile path.
- Confirm output directory creation is allowed.

## DCC-Specific Issues

Maya / Arnold:

- Confirm mtoa is available.
- Confirm OCIO configuration is set consistently.
- Confirm MayaBatch version matches the plugin configuration.

Blender:

- Confirm Blender executable path is consistent across Workers.
- Confirm scene files and output paths are accessible from Worker machines.

## Logging Guidance

- Logs may contain internal paths, usernames, machine names, license values, or IP addresses.
- Do not commit raw logs.
- Redact logs before including them in documentation.
