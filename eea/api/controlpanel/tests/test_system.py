"""Tests for SystemGet REST API endpoint."""

import unittest
from unittest.mock import patch, MagicMock


from eea.api.controlpanel.restapi.get import SystemGet
from eea.api.controlpanel.interfaces import IEEAVersionsBackend, IEEAVersionsFrontend


class TestSystemGetEggs(unittest.TestCase):
    """Test SystemGet.eggs()."""

    def setUp(self):
        """Create SystemGet instance without full Plone init."""
        self.service = SystemGet.__new__(SystemGet)
        self.service.context = MagicMock()
        self.service.request = MagicMock()
        self.service.request._rest_cors_preflight = False

    def test_eggs_returns_generator(self):
        """Test that eggs() returns a generator."""
        result = self.service.eggs()
        self.assertTrue(hasattr(result, "__iter__"))

    def test_eggs_yields_tuples(self):
        """Test that eggs() yields (key, version) tuples."""
        result = list(self.service.eggs())
        self.assertGreater(len(result), 0)
        for item in result:
            self.assertIsInstance(item, tuple)
            self.assertEqual(len(item), 2)

    def test_eggs_contains_setuptools(self):
        """Test that eggs() includes setuptools package."""
        result = dict(self.service.eggs())
        self.assertIn("setuptools", result)

    def test_eggs_values_are_strings(self):
        """Test that egg versions are strings."""
        result = list(self.service.eggs())
        for key, version in result:
            self.assertIsInstance(key, str)
            self.assertIsInstance(version, str)

    def test_eggs_dict_has_multiple_packages(self):
        """Test that eggs() returns multiple packages."""
        result = dict(self.service.eggs())
        self.assertGreater(len(result), 1)


class TestSystemGetFrontend(unittest.TestCase):
    """Test SystemGet.frontend()."""

    def setUp(self):
        self.service = SystemGet.__new__(SystemGet)
        self.service.context = MagicMock()
        self.service.request = MagicMock()
        self.service.request._rest_cors_preflight = False

    @patch("eea.api.controlpanel.restapi.get.get_registry_record")
    def test_frontend_returns_dict_with_keys(self, mock_registry):
        """Test that frontend() returns dict with version, old_version, date."""
        mock_registry.side_effect = lambda name, interface=None: f"test_{name}"
        result = self.service.frontend()
        self.assertIsInstance(result, dict)
        self.assertIn("version", result)
        self.assertIn("old_version", result)
        self.assertIn("date", result)

    @patch("eea.api.controlpanel.restapi.get.get_registry_record")
    def test_frontend_uses_frontend_interface(self, mock_registry):
        """Test that frontend() queries with IEEAVersionsFrontend."""
        mock_registry.side_effect = lambda name, interface=None: f"test_{name}"
        self.service.frontend()
        for call in mock_registry.call_args_list:
            args, kwargs = call
            iface = kwargs.get("interface") or (args[1] if len(args) > 1 else None)
            self.assertEqual(iface, IEEAVersionsFrontend)

    @patch("eea.api.controlpanel.restapi.get.get_registry_record")
    def test_frontend_values_from_registry(self, mock_registry):
        """Test that frontend() returns values from registry."""
        mock_registry.side_effect = lambda name, interface=None: f"val_{name}"
        result = self.service.frontend()
        self.assertEqual(result["version"], "val_version")
        self.assertEqual(result["old_version"], "val_old_version")
        self.assertEqual(result["date"], "val_date")


class TestSystemGetBackend(unittest.TestCase):
    """Test SystemGet.backend()."""

    def setUp(self):
        self.service = SystemGet.__new__(SystemGet)
        self.service.context = MagicMock()
        self.service.request = MagicMock()
        self.service.request._rest_cors_preflight = False

    @patch("eea.api.controlpanel.restapi.get.get_registry_record")
    def test_backend_returns_dict_with_keys(self, mock_registry):
        """Test that backend() returns dict with version, old_version, date."""
        mock_registry.side_effect = lambda name, interface=None: f"test_{name}"
        result = self.service.backend()
        self.assertIsInstance(result, dict)
        self.assertIn("version", result)
        self.assertIn("old_version", result)
        self.assertIn("date", result)

    @patch("eea.api.controlpanel.restapi.get.get_registry_record")
    def test_backend_uses_backend_interface(self, mock_registry):
        """Test that backend() queries with IEEAVersionsBackend."""
        mock_registry.side_effect = lambda name, interface=None: f"test_{name}"
        self.service.backend()
        for call in mock_registry.call_args_list:
            args, kwargs = call
            iface = kwargs.get("interface") or (args[1] if len(args) > 1 else None)
            self.assertEqual(iface, IEEAVersionsBackend)

    @patch("eea.api.controlpanel.restapi.get.get_registry_record")
    def test_backend_values_from_registry(self, mock_registry):
        """Test that backend() returns values from registry."""
        mock_registry.side_effect = lambda name, interface=None: f"val_{name}"
        result = self.service.backend()
        self.assertEqual(result["version"], "val_version")
        self.assertEqual(result["old_version"], "val_old_version")
        self.assertEqual(result["date"], "val_date")


def test_suite():
    """Test suite."""
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
