# Project Time Log

This document summarizes the development process behind the graduation project and technical paper. It is a public-safe timeline, so internal paths, IP addresses, credentials, account names, license details, and raw screenshots are intentionally excluded.

## March 2025 - Initial Planning

### 2025-03-12 - Infrastructure Requirement Research

- Identified the main requirements for a lab-based render farm.
- Reviewed network bandwidth, shared storage, worker PC count, and main server requirements.
- Considered worker grouping, idle-machine usage, and render queue behavior.

### 2025-03-13 - Workflow and Backend Architecture Design

- Drafted the first end-to-end workflow from reservation to Deadline submission.
- Planned MongoDB collections for users, reservations, and render status.
- Selected Python, PySide, MongoDB, Google Sheets, Google Apps Script, Flask, and Deadline tooling as the initial stack.

### 2025-03-15 - Previous Pipeline Tool Reference

- Reviewed an earlier PySide/FFmpeg pipeline utility.
- Reused ideas around file selection, metadata extraction, command generation, and subprocess progress handling.
- Applied those ideas to the later render submission UI.

### 2025-03-16 - Google OAuth and Calendar API Experiment

- Tested a Flask-based Google authentication flow.
- Prototyped route/callback handling and Google service integration.
- Later narrowed the reservation workflow toward Google Sheets instead of Calendar.

### 2025-03-18 - Google Apps Script Reservation Prototype

- Built an early Google Apps Script reservation prototype.
- Generated daily sheets, time blocks, PC group columns, and simple interaction flows.
- Used this as the first user-facing reservation interface concept.

### 2025-03-19 - Feedback Reflection

- Refined the plan after feedback about scene file localization and NAS/shared storage.
- Identified Deadline API research as a key follow-up task.

## April 2025 - Lab Environment and Remote Management

### 2025-03-31 - Lab PC Specification Research

- Collected public-safe notes about lab PC capacity and expected worker usage.
- Estimated whether the available machines could support a render farm.
- Started thinking about how many machines should be grouped for heavy render jobs.

### 2025-04-01 - Scheduled Sync and Headless Rendering Research

- Researched scheduled data synchronization between reservation data and the render system.
- Reviewed headless rendering options for Maya, Blender, and related DCC tools.
- Compared batch rendering behavior across supported tools.

### 2025-04-02 - OpenSSH and Ansible Direction

- Investigated Windows OpenSSH setup for remote worker management.
- Compared manual setup, script-based setup, and Ansible-based orchestration.
- Shifted the project from a simple UI tool toward a broader infrastructure workflow.

### 2025-04-15 - Ansible Control Plan

- Planned a WSL-based Ansible controller for Windows lab machines.
- Reviewed requirements for remote access, stable host addressing, and repeatable setup.
- Identified network stability as a prerequisite for automation.

### 2025-04-16 - NAS, License, and Output Directory Planning

- Planned shared storage rules for input scenes and render output.
- Researched license-server related requirements for Maya/Arnold rendering.
- Defined why local paths should be avoided in distributed rendering.

## May 2025 - License and NAS Integration

### 2025-05-14 - Autodesk/Arnold Network License Setup Research

- Studied Autodesk Network License Manager and Arnold-related license behavior.
- Identified firewall, hostname resolution, and environment variable setup as operational concerns.
- Documented this as a security-sensitive area that must use placeholders in public material.

### 2025-05-21 - UI and Data Flow Refinement

- Refined the PySide UI structure and data flow.
- Separated UI display logic from controller and data access logic.
- Clarified how reservation data should connect to render submission behavior.

### 2025-05-28 - NAS Issue Resolved

- Resolved a shared-storage planning issue and clarified the NAS direction.
- Reconfirmed that scene input and render output must use consistent shared paths.
- Decided to focus first on Maya and Blender integration.

## June 2025 - Remote Setup, UI, DB, and Packaging

### 2025-06-08 - Ansible and Docker Testing

- Tested Ansible and Docker ideas for worker setup and environment isolation.
- Found that Windows lab management still required careful host/network preparation.
- Kept Docker/Ansible as useful experiments rather than the main final deployment path.

### 2025-06-11 - Static IP and Remote Access Issue

- Investigated static addressing and remote access issues.
- Considered stable addressing, hostname-based access, and improved network management.
- Treated network consistency as an operational risk.

### 2025-06-20 - MongoDB and Google Sheets Integration

- Connected reservation-style data with MongoDB storage.
- Tested synchronization concepts between Google Sheets and backend data.
- Clarified how render status and reservation status could be tracked.

### 2025-06-21 - Config and Security Planning

- Planned configuration handling with environment variables and sample config files.
- Reviewed GitHub push protection after sensitive files were accidentally included during development.
- Confirmed that credentials, tokens, passwords, and internal IPs must not be committed.

### 2025-06-24 - Project Packaging and UI Login Flow

- Organized the project into a clearer Python package structure.
- Built login-flow related UI and backend wiring.
- Linked the project to the GitHub repository with a public-safe structure.

### 2025-06-25 - DCC Tool Integration Planning

- Planned how Maya, Blender, and possible future DCC adapters would submit render jobs.
- Defined adapter-style boundaries between UI settings and Deadline submission logic.
- Prioritized Maya and Blender for the first working path.

### 2025-06-26 - Maya Deployment Direction

- Prepared Maya-side deployment and startup behavior.
- Considered scheduled Windows operations for environment setup and maintenance.
- Reviewed how Maya scripts would integrate with the broader submission flow.

## August 2025 - Deadline Worker and Tool Integration

### 2025-08-06 - Docker-based Deadline Worker Design

- Explored Docker-based Deadline Worker concepts.
- Compared container-based setup with the reality of the Windows lab environment.
- Kept the findings as design context rather than final implementation proof.

### 2025-08-07 - Blender Integration Completed

- Completed a Blender-oriented submission path.
- Connected Blender scene/render settings to the project submission structure.
- Verified that Blender needed consistent executable paths and shared storage access.

### 2025-08-23 - Deadline Worker Operation Design

- Researched Deadline Worker pools, groups, limits, chunk size, and concurrent task behavior.
- Documented worker management ideas for lab scheduling and resource control.
- Identified monitoring and troubleshooting as core operational needs.

## September 2025 - Deadline Security and Submit Tool

### 2025-09-01 - Deadline Certificate Structure Research

- Studied Deadline certificate and client connection concepts.
- Reviewed how certificates might be distributed or referenced during worker setup.
- Kept certificate files and private keys out of the public repository.

### 2025-09-02 - Deadline Submitter Code Structure

- Organized submitter code around DCC adapters, job settings, and Deadline command generation.
- Structured the UI so scene/render settings could be collected consistently.
- Improved maintainability by separating UI, adapter, and submission responsibilities.

### 2025-09-10 - Deadline Client Permission Issue

- Checked Windows permission issues related to Deadline client/worker folders.
- Considered how normal lab users and shared accounts should access configuration paths.
- Used this work to stabilize worker execution on shared PCs.

### 2025-09-17 - Worker / Monitor State Verification

- Reviewed setup and monitoring evidence from Deadline-related screens.
- Summarized the verification result without publishing internal screenshots.
- Treated screenshots as private unless all paths, machine names, and server values are blurred.

## October 2025 - Worker Setup and Final Operation

### 2025-10-11 - Network License Server Planning

- Documented the standard setup process for a network license environment.
- Reviewed firewall, hostname, environment variable, and log-monitoring concerns.
- Removed account, serial, product key, host, and server details from the public version.

### 2025-10-13 - Deadline Worker Setup Manual

- Created a repeatable worker setup checklist.
- Covered shared repository access, worker installation, firewall access, certificates, license-related environment variables, and reboot/restart steps.
- Kept real network paths and credential-like values out of the public repository.

### 2025-10-20 - Visual Verification / Environment Check

- Collected visual verification records during render farm setup.
- Summarized the purpose of the screenshots instead of publishing raw internal images.
- Confirmed that screenshots must be redacted before any future upload.

### 2025-10-29 - Final Render Farm Operation Issues

- Tracked issues found during practical lab usage.
- Noted path differences, machine-specific failures, team communication gaps, and hardware support needs.
- Confirmed that the project had moved from prototype work into real operation and troubleshooting.

## Key Technical Work

- Render farm workflow design for a real computer lab environment.
- Deadline, NAS/shared storage, MongoDB, Google Sheets, PySide, Flask, Ansible, Docker, Maya, and Blender research.
- Reservation and render status data flow design.
- Deadline submitter architecture for Maya/Blender workflows.
- Worker grouping, monitoring, permissions, and troubleshooting planning.
- Public documentation and security redaction policy.

## Lessons Learned

- Render farm development is infrastructure-heavy, not only UI or job submission work.
- Shared paths must be standardized before distributed rendering can be reliable.
- Worker setup needs to be repeatable because manual configuration does not scale.
- License handling is a core operational dependency.
- A render submission UI still needs database logic, scheduling logic, path validation, worker monitoring, and error reporting.
- Real operation reveals issues that are hard to predict during prototype development.

## Public Repository Safety Checklist

- Real IP addresses, UNC/NAS paths, hostnames, student IDs, account names, and email addresses must be removed.
- Passwords, tokens, API keys, OAuth secrets, product keys, serials, certificates, and private keys must not be committed.
- Screenshots must be blurred or removed if they show paths, machine names, users, logs, or license-related information.
- Public examples should use placeholders such as `<nas-server-ip>`, `<internal-path>`, `<license-server-ip>`, `<student-id>`, and `<secret>`.
- Git history should be checked before publishing sensitive project material.
