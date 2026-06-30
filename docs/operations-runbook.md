# Operations Runbook

## Purpose

This runbook summarizes the operational checks for the Deadline Render Farm Automation project in a public-safe way.

## Scope

This document does not include private IPs, machine names, NAS paths, license server values, raw logs, or credentials.

## Operator Checklist

### 1. Before Submission

- Check reservation/auth data availability.
- Check scene path policy.
- Check expected renderer/plugin.
- Check NAS input/output path format.
- Check Deadline command availability.

### 2. During Submission

- Confirm job info/plugin info generation.
- Confirm `deadlinecommand SubmitJob` execution result.
- Confirm job appears in Deadline Monitor.

### 3. Worker Health Check

- Check Worker online/offline status.
- Check plugin availability.
- Check renderer/license readiness.
- Check shared storage access.

### 4. Log Check

- Check submission logs.
- Check Worker render logs.
- Check path resolution errors.
- Check license or plugin loading errors.

### 5. Common Failure Cases

| Symptom | Likely Area | First Check | Recovery |
|---|---|---|---|
| Job not submitted | Submission layer | deadlinecommand path/env | Check `.env`, command path, preflight |
| Job submitted but not rendering | Worker layer | Worker status/plugin | Check Worker, plugin, license |
| File not found | Storage/NAS | Shared path policy | Verify NAS mount/path mapping |
| Auth/reservation fails | MongoDB/reservation | MongoDB URI/collection | Check env and reservation data |
| Render fails mid-job | Renderer/license | Worker log | Check license/plugin/log |

## Escalation Notes

If the issue involves private infrastructure values, keep them out of public logs and document only sanitized symptoms and recovery steps.
