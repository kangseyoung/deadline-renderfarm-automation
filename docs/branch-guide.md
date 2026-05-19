# Branch Guide

This repository should be reviewed from `main`.

## Current Baseline

- `main`: portfolio baseline branch. Recruiters and reviewers should use this branch and the root README.
- `origin/HEAD`: points to `origin/main`.

## Branches to Review Before Deletion

No branches were deleted as part of this cleanup. The following branches are cleanup candidates and should be reviewed manually in GitHub before removal.

| Branch | Status | Reason |
| --- | --- | --- |
| `master` | old divergent branch | Older development line; not the portfolio baseline. Keeping both `main` and `master` can confuse reviewers. |
| `backup/final-before-codex` | merged into `main` | Same tip as `final`; likely backup checkpoint. |
| `final` | merged into `main` | Historical final/checkpoint branch; no longer needed as default review target. |
| `docs/portfolio-main` | old docs branch | Earlier documentation polish branch; superseded by `main`. |
| `chore/capstone-portfolio-refactor` | merged into `main` | Documentation refactor already merged. |
| `develop` | old divergent branch | Development snapshot from earlier implementation work. |
| `blender` | old divergent branch | Blender experiment branch; inspect before deleting. |
| `DEADLINE` | old divergent branch | Deadline experiment branch; inspect before deleting. |
| `test` | old divergent branch | Test/install-tool branch; inspect before deleting. |

## Recommended GitHub Settings

1. Set the default branch to `main`.
2. Protect `main` if the repository will continue to be updated.
3. Delete only branches that have been reviewed and confirmed unnecessary.
4. Do not rewrite history automatically from this repository cleanup. See [security-cleanup.md](security-cleanup.md) for sensitive-history handling.
