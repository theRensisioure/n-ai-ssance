#!/usr/bin/env python3
"""Fail if the SSFS working tree / staged set looks non-sterile.

Usage:
  python scripts/sterile-check.py           # scan repo (tracked + untracked non-ignored)
  python scripts/sterile-check.py --staged  # scan git staged blob paths only
  python scripts/sterile-check.py --diff    # also scan staged patch text

Exit 0 = clean. Exit 1 = refuse push.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Path names that must never appear in the tree
FORBIDDEN_NAME_RE = re.compile(
    r"(?i)("
    r"chat_history\.jsonl|prompt_history\.jsonl|events\.jsonl|"
    r"hunk_records\.jsonl|btw_history\.jsonl|updates\.jsonl|"
    r"^\.env($|\.)|id_rsa|id_ed25519|\.pem$|"
    r"confirmations\.csv|"
    r"credentials\.json|service.account"
    r")"
)

# Content patterns (tracked text files only)
FORBIDDEN_CONTENT = [
    (re.compile(r"\bgho_[A-Za-z0-9_]{20,}"), "GitHub OAuth token-shaped string"),
    (re.compile(r"\bghp_[A-Za-z0-9_]{20,}"), "GitHub PAT-shaped string"),
    (re.compile(r"\bsk-[A-Za-z0-9]{20,}"), "sk- API key-shaped string"),
    (re.compile(r"(?i)-----BEGIN (RSA |OPENSSH |EC )?PRIVATE KEY-----"), "private key block"),
    (re.compile(r"(?i)api[_-]?key\s*[:=]\s*['\"][^'\"]{12,}"), "api_key assignment"),
    (re.compile(r"(?i)password\s*[:=]\s*['\"][^'\"]{6,}"), "password assignment"),
    # Real machine user homes (not generic placeholders)
    (re.compile(r"(?i)C:\\\\Users\\\\(?!Public\\)[A-Za-z0-9._-]+\\\\"), "Windows user absolute path"),
    (re.compile(r"(?i)C:/Users/(?!Public/)[A-Za-z0-9._-]+/"), "Windows user absolute path"),
    (re.compile(r"/home/[a-z][a-z0-9._-]{1,32}/"), "Linux home absolute path"),
    (re.compile(r"/Users/[A-Za-z][A-Za-z0-9._-]{1,32}/"), "macOS home absolute path"),
]

# Files that may mention patterns only as documentation of the ban
ALLOWLIST_PATHS = {
    "STERILE.md",
    "scripts/sterile-check.py",
    "README.md",  # may say %USERPROFILE% only — still scanned for secrets
    "PRODUCT.md",
    "SOURCE.md",
}

TEXT_SUFFIX = {
    ".md",
    ".txt",
    ".py",
    ".json",
    ".jsonl",
    ".yml",
    ".yaml",
    ".toml",
    ".sh",
    ".ps1",
    ".html",
    ".js",
    ".ts",
    ".css",
    ".skill",
    "",  # LICENSE etc.
}


def git_ls(staged: bool) -> list[Path]:
    if staged:
        out = subprocess.check_output(
            ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"],
            cwd=ROOT,
            text=True,
        )
        rels = [ln.strip() for ln in out.splitlines() if ln.strip()]
    else:
        out = subprocess.check_output(
            ["git", "ls-files", "-co", "--exclude-standard"],
            cwd=ROOT,
            text=True,
        )
        rels = [ln.strip() for ln in out.splitlines() if ln.strip()]
    return [ROOT / r for r in rels if r]


def staged_patch() -> str:
    try:
        return subprocess.check_output(
            ["git", "diff", "--cached"],
            cwd=ROOT,
            text=True,
            errors="replace",
        )
    except subprocess.CalledProcessError:
        return ""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--staged", action="store_true")
    ap.add_argument("--diff", action="store_true", help="also scan staged patch text")
    args = ap.parse_args()

    issues: list[str] = []
    files = git_ls(staged=args.staged)

    for path in files:
        rel = path.relative_to(ROOT).as_posix()
        if FORBIDDEN_NAME_RE.search(path.name) or FORBIDDEN_NAME_RE.search(rel):
            issues.append(f"FORBIDDEN_NAME  {rel}")
            continue
        if not path.is_file():
            continue
        if path.suffix.lower() not in TEXT_SUFFIX and path.suffix != "":
            # still check name only for binaries
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            issues.append(f"READ_FAIL  {rel}: {e}")
            continue
        # STERILE.md documents banned patterns — skip content hits there
        if rel in ("STERILE.md", "scripts/sterile-check.py"):
            continue
        for cre, label in FORBIDDEN_CONTENT:
            if cre.search(text):
                # allowlist generic env placeholders in docs
                if label.endswith("absolute path") and rel in (
                    "README.md",
                    "PRODUCT.md",
                    "skills/README.md",
                ):
                    # only fail if real username-looking path, not %USERPROFILE%
                    if "%USERPROFILE%" in text or "~/.grok" in text:
                        # still fail if C:\\Users\\something appears
                        if not re.search(
                            r"(?i)C:[/\\\\]Users[/\\\\](?!Public)", text
                        ) and not re.search(r"/home/[a-z]", text):
                            continue
                issues.append(f"FORBIDDEN_CONTENT  {rel}: {label}")

    if args.diff or args.staged:
        patch = staged_patch()
        if patch:
            # Drop hunks that only document the ban (STERILE.md / this script)
            filtered_lines = []
            skip = False
            for line in patch.splitlines():
                if line.startswith("diff --git"):
                    skip = (
                        " STERILE.md" in line
                        or " sterile-check.py" in line
                        or line.endswith("STERILE.md")
                        or line.endswith("sterile-check.py")
                    )
                if skip:
                    continue
                filtered_lines.append(line)
            filtered = "\n".join(filtered_lines)
            for cre, label in FORBIDDEN_CONTENT:
                if cre.search(filtered):
                    issues.append(f"FORBIDDEN_IN_STAGED_DIFF  {label}")

    if issues:
        print("STERILE CHECK FAILED — do not push\n", file=sys.stderr)
        for i in issues:
            print(f"  - {i}", file=sys.stderr)
        print(
            "\nSee STERILE.md. Strip the data or keep it outside this repo.",
            file=sys.stderr,
        )
        return 1

    print("sterile-check: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
