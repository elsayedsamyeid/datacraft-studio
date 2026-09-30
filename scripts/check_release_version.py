"""Keep public copy in step with the newest prepared release folder.

Run without arguments to update the copy after preparing a new release, or use
--check in CI to catch a forgotten version update.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RELEASES = ROOT / "releases"
TARGETS = {
    "docs/index.html": (
        r"(DataCraft Studio )\d+\.\d+\.\d+( · Free for Windows)",
        r"(Free &amp; Pro · v)\d+\.\d+\.\d+",
    ),
    "guide/README.md": (r"(Written for version \*\*)\d+\.\d+\.\d+(\*\*)",),
    "ROADMAP.md": (r"(## Available now — )\d+\.\d+\.\d+",),
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if a version is stale")
    args = parser.parse_args()

    versions = []
    for folder in RELEASES.glob("v*"):
        if folder.is_dir() and re.fullmatch(r"v\d+\.\d+\.\d+", folder.name):
            versions.append((tuple(map(int, folder.name[1:].split("."))), folder.name[1:]))
    if not versions:
        raise SystemExit("No releases/vMAJOR.MINOR.PATCH folder found")
    version = max(versions)[1]
    stale = []

    for relative, patterns in TARGETS.items():
        path = ROOT / relative
        content = path.read_text(encoding="utf-8")
        updated = content
        for pattern in patterns:
            updated, count = re.subn(pattern, lambda match: f"{match.group(1)}{version}{match.group(2) if match.lastindex == 2 else ''}", updated)
            if count != 1:
                raise SystemExit(f"Expected one match for {pattern!r} in {relative}; found {count}")
        if updated != content:
            stale.append(relative)
            if not args.check:
                path.write_text(updated, encoding="utf-8")

    if stale:
        action = "Out of date" if args.check else "Updated"
        print(f"{action} for v{version}: {', '.join(stale)}")
        return 1 if args.check else 0
    print(f"Release copy matches v{version}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
