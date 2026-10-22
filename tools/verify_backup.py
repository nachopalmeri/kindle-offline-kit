"""Compare two already acquired directory trees; never write to either input.

Standard library only, Python 3.10+. This does not access Windows MTP directly,
copy books, snapshot a live database or certify a full-device backup.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import stat
import sys

REPOSITORY = Path(__file__).resolve().parents[1]


def is_link(path):
    if path.is_symlink() or (
        hasattr(path, "is_junction") and path.is_junction()
    ):
        return True
    try:
        attributes = getattr(path.lstat(), "st_file_attributes", 0)
    except FileNotFoundError:
        return False
    return bool(attributes & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0))


def directory(value):
    path = Path(value).expanduser()
    if is_link(path):
        raise ValueError("Input directory must not be a link or junction")
    path = path.resolve(strict=True)
    if not path.is_dir():
        raise ValueError("Expected an ordinary filesystem directory, not an MTP display name")
    return path


def scan(root):
    files, directories = {}, []
    def fail(error):
        raise error
    for parent, subdirs, filenames in os.walk(root, followlinks=False, onerror=fail):
        subdirs.sort()
        filenames.sort()
        for name in subdirs:
            path = Path(parent) / name
            if is_link(path):
                raise ValueError("A directory link or junction prevents safe verification")
            directories.append(path.relative_to(root).as_posix())
        for name in filenames:
            path = Path(parent) / name
            if is_link(path) or not stat.S_ISREG(path.lstat().st_mode):
                raise ValueError("Only ordinary files are supported")
            before = path.stat()
            digest = hashlib.sha256()
            with path.open("rb") as stream:
                for block in iter(lambda: stream.read(1024 * 1024), b""):
                    digest.update(block)
            after = path.stat()
            if (before.st_size, before.st_mtime_ns, before.st_ino) != (
                after.st_size, after.st_mtime_ns, after.st_ino
            ):
                raise ValueError("A file changed during hashing; acquire a stable copy first")
            files[path.relative_to(root).as_posix()] = {
                "bytes": after.st_size, "sha256": digest.hexdigest()
            }
    return files, sorted(directories)


def verify(source, backup, report):
    source, backup = directory(source), directory(backup)
    if source.is_relative_to(backup) or backup.is_relative_to(source):
        raise ValueError("Source and backup must be separate, non-overlapping directories")
    report = Path(report).expanduser()
    if is_link(report):
        raise ValueError("Report must not be a link or reparse point")
    report = report.resolve()
    if any(report.is_relative_to(path) for path in (REPOSITORY, source, backup)):
        raise ValueError("Write private reports outside this repository and both input trees")
    if report.exists():
        raise FileExistsError("Refusing to replace an existing report")
    if not report.parent.is_dir():
        raise ValueError("Report parent directory must already exist")
    source_files, source_dirs = scan(source)
    backup_files, backup_dirs = scan(backup)
    if not source_files:
        raise ValueError("An empty source tree cannot establish a useful backup")
    missing = sorted(source_files.keys() - backup_files.keys())
    extra = sorted(backup_files.keys() - source_files.keys())
    different = sorted(
        key for key in source_files.keys() & backup_files.keys()
        if source_files[key] != backup_files[key]
    )
    result = {
        "checked_utc": datetime.now(timezone.utc).isoformat(),
        "match": not (missing or extra or different or source_dirs != backup_dirs),
        "scope": "two supplied directory trees only; not an atomic snapshot",
        "complete_device_backup": False,
        "source_files": len(source_files),
        "backup_files": len(backup_files),
        "missing_files": missing,
        "extra_files": extra,
        "different_files": different,
        "source_directories": source_dirs,
        "backup_directories": backup_dirs,
        "source_manifest": source_files,
        "backup_manifest": backup_files,
    }
    with report.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, help="First privately acquired directory")
    parser.add_argument("--backup", required=True, help="Second privately acquired directory")
    parser.add_argument("--report", required=True, help="New private report outside this repository")
    args = parser.parse_args()
    try:
        result = verify(args.source, args.backup, args.report)
    except (OSError, ValueError):
        # Do not echo exception paths, filenames or private book names.
        print("Verification stopped: check input paths, links, stable files and report destination.", file=sys.stderr)
        return 2
    print(json.dumps({
        "match": result["match"], "source_files": result["source_files"],
        "backup_files": result["backup_files"], "complete_device_backup": False
    }))
    return 0 if result["match"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
