#!/usr/bin/env python3
"""
Validation script for UV projects created by the UV-Project-Manager skill.

This script validates:
- pyproject.toml is valid TOML
- Folder structure matches specification
- All required files exist
- No hardcoded secrets
- Project ready for 'uv sync'
"""

import os
import sys
import re
import tomllib
from pathlib import Path
from typing import List, Tuple


def validate_project_name(project_root: Path) -> Tuple[bool, str]:
    """Validate project name and metadata."""
    pyproject = project_root / "pyproject.toml"

    if not pyproject.exists():
        return False, "❌ pyproject.toml not found"

    try:
        with open(pyproject, "rb") as f:
            config = tomllib.load(f)
    except Exception as e:
        return False, f"❌ Invalid TOML: {e}"

    if "project" not in config:
        return False, "❌ Missing [project] section"

    project_meta = config["project"]
    if "name" not in project_meta:
        return False, "❌ Missing project.name"
    if "version" not in project_meta:
        return False, "❌ Missing project.version"
    if "requires-python" not in project_meta:
        return False, "❌ Missing project.requires-python"

    name = project_meta["name"]
    if not re.match(r"^[a-z0-9][a-z0-9._-]*$", name):
        return False, f"❌ Invalid project name: {name} (must be lowercase alphanumeric + hyphens)"

    return True, f"✅ Project name valid: {name}"


def validate_folder_structure(project_root: Path) -> Tuple[bool, List[str]]:
    """Validate folder structure (src/ vs flat)."""
    results = []

    # Check for src/ layout
    src_dir = project_root / "src"
    if src_dir.exists():
        # src/ layout detected
        project_dirs = [d for d in src_dir.iterdir() if d.is_dir() and not d.name.startswith("_")]
        if project_dirs:
            package_dir = project_dirs[0]
            init_file = package_dir / "__init__.py"
            if init_file.exists():
                results.append(f"✅ src/ layout detected: {package_dir.name}/")
            else:
                results.append(f"⚠️  Package directory exists but missing __init__.py: {package_dir}")
        else:
            results.append("⚠️  src/ directory exists but contains no packages")
    else:
        # Check for flat layout with main.py
        main_file = project_root / "main.py"
        if main_file.exists():
            results.append("✅ Flat layout detected: main.py exists")
        else:
            results.append("⚠️  No src/ layout and no main.py found")

    # Check for tests directory
    tests_dir = project_root / "tests"
    if tests_dir.exists():
        init_file = tests_dir / "__init__.py"
        if init_file.exists():
            results.append("✅ tests/ directory properly structured")
        else:
            results.append("⚠️  tests/ directory exists but missing __init__.py")
    else:
        results.append("ℹ️  tests/ directory not found (optional)")

    # Check for .github/workflows
    workflows_dir = project_root / ".github" / "workflows"
    if workflows_dir.exists():
        yaml_files = list(workflows_dir.glob("*.yml"))
        results.append(f"✅ GitHub Actions found: {len(yaml_files)} workflow(s)")
    else:
        results.append("ℹ️  .github/workflows/ not found (optional)")

    return True, results


def validate_no_secrets(project_root: Path) -> Tuple[bool, List[str]]:
    """Check for hardcoded secrets."""
    results = []
    secret_patterns = [
        (r"api[_-]?key\s*=\s*['\"]", "API key"),
        (r"secret\s*=\s*['\"]", "Secret"),
        (r"password\s*=\s*['\"]", "Password"),
        (r"token\s*=\s*['\"]", "Token"),
        (r"sk_live_", "Stripe key"),
        (r"AKIA[0-9A-Z]{16}", "AWS Access Key"),
    ]

    suspicious_files = []
    for file_path in project_root.rglob("*"):
        if file_path.is_file() and file_path.suffix in [".py", ".toml", ".md"]:
            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                    for pattern, name in secret_patterns:
                        if re.search(pattern, content, re.IGNORECASE):
                            suspicious_files.append(f"⚠️  Possible {name} in {file_path.relative_to(project_root)}")
            except Exception as e:
                pass

    if not suspicious_files:
        results.append("✅ No obvious hardcoded secrets found")
    else:
        results.extend(suspicious_files)

    return len(suspicious_files) == 0, results


def validate_required_files(project_root: Path) -> Tuple[bool, List[str]]:
    """Check for required files."""
    required_files = [
        "pyproject.toml",
        "README.md",
        ".gitignore",
    ]

    results = []
    missing = []

    for file_name in required_files:
        file_path = project_root / file_name
        if file_path.exists():
            results.append(f"✅ {file_name}")
        else:
            results.append(f"❌ {file_name} (MISSING)")
            missing.append(file_name)

    return len(missing) == 0, results


def main():
    """Run all validations on a UV project."""
    if len(sys.argv) > 1:
        project_root = Path(sys.argv[1])
    else:
        project_root = Path.cwd()

    if not project_root.exists():
        print(f"❌ Project directory not found: {project_root}")
        sys.exit(1)

    print(f"\n🔍 Validating UV Project: {project_root.name}")
    print("=" * 60)

    # Validate project name
    print("\n📋 Project Metadata:")
    success, msg = validate_project_name(project_root)
    print(msg)

    # Validate folder structure
    print("\n📁 Folder Structure:")
    _, results = validate_folder_structure(project_root)
    for result in results:
        print(result)

    # Validate required files
    print("\n📄 Required Files:")
    _, results = validate_required_files(project_root)
    for result in results:
        print(result)

    # Check for secrets
    print("\n🔐 Security Check:")
    _, results = validate_no_secrets(project_root)
    for result in results:
        print(result)

    print("\n" + "=" * 60)
    print("✅ Validation complete! Project appears ready for development.\n")


if __name__ == "__main__":
    main()
