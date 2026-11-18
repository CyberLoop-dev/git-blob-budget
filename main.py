#!/usr/bin/env python3
"""Report large Git blobs reachable from repository refs."""
import argparse
import json
import subprocess
import sys

def parse_object_rows(rows, paths, min_bytes=0, limit=20):
    objects = []
    for row in rows:
        parts = row.split()
        if len(parts) != 3:
            continue
        oid, kind, raw_size = parts
        if kind != "blob":
            continue
        size = int(raw_size)
        if size >= min_bytes:
            objects.append({"oid": oid, "path": paths.get(oid, "(path unavailable)"), "size": size})
    return sorted(objects, key=lambda item: item["size"], reverse=True)[:limit]

def scan_repository(repo=".", min_bytes=0, limit=20):
    rev = subprocess.run(["git", "rev-list", "--objects", "--all"], cwd=repo, text=True, capture_output=True, check=True)
    paths = {}
    for line in rev.stdout.splitlines():
        oid, separator, path = line.partition(" ")
        if separator:
            paths.setdefault(oid, path)
    if not paths:
        return []
    batch = subprocess.run(["git", "cat-file", "--batch-check=%(objectname) %(objecttype) %(objectsize)"],
        cwd=repo, input="\n".join(paths) + "\n", text=True, capture_output=True, check=True)
    return parse_object_rows(batch.stdout.splitlines(), paths, min_bytes, limit)

def human_size(size):
    units = ("B", "KB", "MB", "GB", "TB")
    value = float(size)
    for unit in units:
        if value < 1024 or unit == units[-1]:
            return f"{value:.1f} {unit}"
        value /= 1024
    return f"{value:.1f} TB"

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=".", help="Git repository path")
    parser.add_argument("--min-mb", type=float, default=1.0, help="Minimum blob size in MiB")
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        rows = scan_repository(args.repo, max(0, int(args.min_mb * 1024 * 1024)), max(1, args.limit))
    except (subprocess.CalledProcessError, FileNotFoundError) as exc:
        print(f"git-blob-budget: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(rows, indent=2))
    elif not rows:
        print("No reachable blobs matched the size threshold.")
    else:
        print(f"{'SIZE':>12}  {'OBJECT':<12}  PATH")
        for item in rows:
            print(f"{human_size(item['size']):>12}  {item['oid'][:12]:<12}  {item['path']}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
