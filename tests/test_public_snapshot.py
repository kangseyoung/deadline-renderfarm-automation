from pathlib import Path
import ast


ROOT = Path(__file__).resolve().parents[1]


def test_public_snapshot_paths_exist():
    required_paths = [
        "src/README.md",
        "src/main.py",
        "src/submission",
        "src/ui",
        "src/reservation",
        ".env.example",
        "docs/architecture.md",
        "docs/troubleshooting.md",
        "docs/operations-runbook.md",
    ]

    for relative_path in required_paths:
        assert (ROOT / relative_path).exists(), f"Missing required path: {relative_path}"


def test_public_python_files_are_parseable():
    python_files = [
        ROOT / "src/main.py",
        *list((ROOT / "src/submission").rglob("*.py")),
        *list((ROOT / "src/reservation").rglob("*.py")),
    ]

    assert python_files, "No Python files found for smoke parsing"

    for file_path in python_files:
        source = file_path.read_text(encoding="utf-8")
        ast.parse(source, filename=str(file_path))
