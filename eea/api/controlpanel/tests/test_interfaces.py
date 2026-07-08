"""Tests for IEEAVersionsBackend and IEEAVersionsFrontend interfaces."""

import unittest

from zope import schema

from eea.api.controlpanel.interfaces import IEEAVersionsBackend, IEEAVersionsFrontend


class TestIEEAVersionsBackend(unittest.TestCase):
    """Test IEEAVersionsBackend interface."""

    def test_has_date_field(self):
        """Test that date field exists."""
        self.assertIn("date", list(IEEAVersionsBackend.names()))

    def test_has_version_field(self):
        """Test that version field exists."""
        self.assertIn("version", list(IEEAVersionsBackend.names()))

    def test_has_old_version_field(self):
        """Test that old_version field exists."""
        self.assertIn("old_version", list(IEEAVersionsBackend.names()))

    def test_date_is_datetime(self):
        """Test that date field is Datetime."""
        self.assertIsInstance(IEEAVersionsBackend["date"], schema.Datetime)

    def test_version_is_text(self):
        """Test that version field is Text."""
        self.assertIsInstance(IEEAVersionsBackend["version"], schema.Text)

    def test_old_version_is_text(self):
        """Test that old_version field is Text."""
        self.assertIsInstance(IEEAVersionsBackend["old_version"], schema.Text)

    def test_date_required(self):
        """Test that date field is required."""
        self.assertTrue(IEEAVersionsBackend["date"].required)

    def test_version_required(self):
        """Test that version field is required."""
        self.assertTrue(IEEAVersionsBackend["version"].required)

    def test_old_version_not_required(self):
        """Test that old_version field is optional."""
        self.assertFalse(IEEAVersionsBackend["old_version"].required)


class TestIEEAVersionsFrontend(unittest.TestCase):
    """Test IEEAVersionsFrontend interface."""

    def test_has_date_field(self):
        """Test that date field exists."""
        self.assertIn("date", list(IEEAVersionsFrontend.names()))

    def test_has_version_field(self):
        """Test that version field exists."""
        self.assertIn("version", list(IEEAVersionsFrontend.names()))

    def test_has_old_version_field(self):
        """Test that old_version field exists."""
        self.assertIn("old_version", list(IEEAVersionsFrontend.names()))

    def test_date_is_datetime(self):
        """Test that date field is Datetime."""
        self.assertIsInstance(IEEAVersionsFrontend["date"], schema.Datetime)

    def test_version_is_text(self):
        """Test that version field is Text."""
        self.assertIsInstance(IEEAVersionsFrontend["version"], schema.Text)

    def test_old_version_is_text(self):
        """Test that old_version field is Text."""
        self.assertIsInstance(IEEAVersionsFrontend["old_version"], schema.Text)

    def test_date_required(self):
        """Test that date field is required."""
        self.assertTrue(IEEAVersionsFrontend["date"].required)

    def test_version_required(self):
        """Test that version field is required."""
        self.assertTrue(IEEAVersionsFrontend["version"].required)

    def test_old_version_not_required(self):
        """Test that old_version field is optional."""
        self.assertFalse(IEEAVersionsFrontend["old_version"].required)

    def test_same_fields_as_backend(self):
        """Test that frontend has same field names as backend."""
        backend_fields = set(IEEAVersionsBackend.names())
        frontend_fields = set(IEEAVersionsFrontend.names())
        self.assertEqual(backend_fields, frontend_fields)


def test_suite():
    """Test suite."""
    return unittest.defaultTestLoader.loadTestsFromName(__name__)