import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location(
    "verify_backup", Path(__file__).resolve().parents[1] / "tools/verify_backup.py"
)
tool = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(tool)


class BackupTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="offline-kit-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "source"
        self.backup = self.root / "backup"
        self.source.mkdir()
        self.backup.mkdir()
        self.report = self.root / "report.private.json"

    def pair(self, name, first=b"sample", second=None):
        for directory, data in (
            (self.source, first), (self.backup, first if second is None else second)
        ):
            path = directory / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)

    def test_equal_unicode_hidden_and_empty_directory(self):
        self.pair("documents/acción.sdr/.reader-state", b"example")
        for directory in (self.source, self.backup):
            (directory / "empty").mkdir()
        result = tool.verify(self.source, self.backup, self.report)
        self.assertTrue(result["match"])
        self.assertFalse(result["complete_device_backup"])
        self.assertEqual(result["source_files"], 1)
        self.assertEqual(json.loads(self.report.read_text())["match"], True)

    def test_same_size_corruption(self):
        self.pair("book.txt", b"abcd", b"abce")
        result = tool.verify(self.source, self.backup, self.report)
        self.assertFalse(result["match"])
        self.assertEqual(result["different_files"], ["book.txt"])

    def test_missing_and_extra_files(self):
        (self.source / "missing.txt").write_text("a")
        (self.backup / "extra.txt").write_text("b")
        result = tool.verify(self.source, self.backup, self.report)
        self.assertEqual(result["missing_files"], ["missing.txt"])
        self.assertEqual(result["extra_files"], ["extra.txt"])

    def test_missing_empty_directory(self):
        self.pair("example.txt")
        (self.source / "empty").mkdir()
        self.assertFalse(tool.verify(self.source, self.backup, self.report)["match"])

    def test_empty_trees_do_not_count_as_a_backup(self):
        with self.assertRaises(ValueError):
            tool.verify(self.source, self.backup, self.report)

    def test_same_source_and_nested_trees_refused(self):
        self.pair("example.txt")
        for backup in (self.source, self.source / "nested"):
            backup.mkdir(exist_ok=True)
            with self.assertRaises(ValueError):
                tool.verify(self.source, backup, self.report)
        self.assertFalse(self.report.exists())

    def test_report_must_not_be_in_input_or_repository(self):
        self.pair("example.txt")
        for target in (
            self.source / "report.json", self.backup / "report.json",
            Path(__file__).resolve().parents[1] / "forbidden-report.json",
        ):
            with self.assertRaises(ValueError):
                tool.verify(self.source, self.backup, target)
            self.assertFalse(target.exists())

    def test_report_never_overwrites(self):
        self.pair("example.txt")
        self.report.write_text("keep")
        with self.assertRaises(FileExistsError):
            tool.verify(self.source, self.backup, self.report)
        self.assertEqual(self.report.read_text(), "keep")

    def test_symlink_is_not_followed(self):
        self.pair("example.txt")
        external = self.root / "outside.txt"
        external.write_text("private")
        link = self.source / "link.txt"
        try:
            link.symlink_to(external)
        except OSError:
            self.skipTest("Creating symlinks is unavailable on this host")
        with self.assertRaises(ValueError):
            tool.verify(self.source, self.backup, self.report)
        self.assertFalse(self.report.exists())

    def test_link_guard_without_os_symlink_privileges(self):
        self.pair("blocked.txt")
        original = tool.is_link
        with patch.object(tool, "is_link", side_effect=lambda p: p.name == "blocked.txt" or original(p)):
            with self.assertRaises(ValueError):
                tool.verify(self.source, self.backup, self.report)
        self.assertFalse(self.report.exists())

    def test_unreadable_directory_aborts_instead_of_silent_omission(self):
        self.pair("example.txt")
        def inaccessible(root, followlinks=False, onerror=None):
            if onerror:
                onerror(PermissionError("synthetic unreadable directory"))
            return iter(())
        with patch.object(tool.os, "walk", side_effect=inaccessible):
            with self.assertRaises(PermissionError):
                tool.verify(self.source, self.backup, self.report)
        self.assertFalse(self.report.exists())


if __name__ == "__main__":
    unittest.main()
