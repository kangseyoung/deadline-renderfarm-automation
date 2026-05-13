# Development History

This document summarizes development history from local Notion exports and time logs. It is not the final architecture source of truth. If this history conflicts with the final technical paper or final branch code, follow the paper for final claims and the code for implementation details.

## Phase 1: Planning and Architecture Exploration

Early notes describe project planning, system architecture sketches, reservation workflow ideas, and database schema exploration. Some notes mention MySQL, Flask, IP restrictions, Docker, and generic API endpoints. These should be treated as planning artifacts, not final implementation claims.

Outcome:

- Render farm automation direction selected.
- Reservation-first workflow defined.
- Deadline, MongoDB, PySide, and Google Sheets/GAS became the final stack direction.

## Phase 2: Deadline and Lab Infrastructure Testing

Notes and the final paper describe work around Deadline Repository, Database, Client/Worker concepts, NAS roles, and Windows lab constraints.

Key themes:

- understanding Deadline Repository versus Worker responsibilities.
- testing Deadline command submission.
- identifying that Workers require consistent network storage access.
- handling firewall, permissions, and reset-policy constraints.

## Phase 3: Reservation System Work

The Notion exports include Google Sheets reservation plans and Google Sheets-to-MongoDB sync notes. The final branch includes a Python `gspread` sync script, while the final paper describes Google Sheets / Google Apps Script as the reservation interface.

Public conclusion:

- Google Sheets was used as an operator-friendly reservation surface.
- MongoDB was used to make reservation data available to the UI.
- Exact GAS source is not included in the final branch and needs verification.

## Phase 4: PySide UI Development

UI notes describe a model/view/controller direction. The final branch contains:

- login UI.
- file-drop UI.
- main submitter UI.
- model methods for DCC detection, current scene path, output path, user ID, and reservation list.

Some controller code remains placeholder-like, and the UI-to-submission button wiring needs verification.

## Phase 5: DCC Adapter and Deadline Submission Package

The September notes align closely with the final branch code under `gpclean/gpclean_submit/`:

- config defaults for `deadlinecommand`, pool, group, priority, and chunk size.
- Deadline submission wrapper.
- job/plugin info builder.
- Maya and Blender adapters.
- common preflight checks.

This is one of the clearest code-backed implementation areas in the repository.

## Phase 6: Worker Setup and Operations

Later notes describe Worker setup steps, NAS connection, Deadline Worker installation, database/firewall access, Arnold license environment settings, and operator checklists.

Public-safe takeaways:

- Workers need shared storage access.
- Workers need consistent Deadline configuration.
- Arnold jobs require license environment setup.
- Operators should verify Worker status before long render windows.

Do not publish raw commands from private notes unless they are redacted and rewritten with placeholders.

## Phase 7: Debugging and Troubleshooting

The PRFS guide and handoff notes describe recurring operational errors:

- path and NAS access failures.
- license failures.
- DCC plugin or renderer failures.
- color management / OCIO failures.
- Worker offline or stale configuration.

The final paper formalizes these into troubleshooting categories and reports that operational workflow improved after standardization.

## Considered but Not Adopted

The final paper supports documenting these as trade-offs:

- Docker was considered for Worker standardization but not adopted because Maya/Arnold licensing, GUI/DCC behavior, network drives, and Deep Freeze made it unsuitable.
- Ansible was considered for Worker automation but not adopted because Windows remote management and lab permission constraints were unreliable.

## Documentation Phase

This public documentation pass converts private notes and final-paper claims into redacted portfolio material. Private reference files, screenshots, logs, student IDs, server values, and credentials are intentionally not copied into the repository.

