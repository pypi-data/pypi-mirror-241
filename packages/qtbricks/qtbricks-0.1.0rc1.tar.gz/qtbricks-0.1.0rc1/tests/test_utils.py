import os
import unittest

import PySide6

from qtbricks import utils


class TestImagePath(unittest.TestCase):
    def setUp(self):
        self.basedir = os.path.join(
            os.path.split(os.path.dirname(__file__))[0], "qtbricks"
        )

    def test_image_path_with_defaults(self):
        image_name = "foo.svg"
        expected = os.path.join(self.basedir, "images", image_name)
        actual = utils.image_path(name=image_name)
        self.assertEqual(expected, actual)

    def test_image_path_with_image_dir(self):
        image_name = "foo.svg"
        image_path = "icons"
        expected = os.path.join(self.basedir, image_path, image_name)
        actual = utils.image_path(name=image_name, image_dir=image_path)
        self.assertEqual(expected, actual)

    def test_image_path_with_base_dir(self):
        image_name = "foo.svg"
        base_dir = os.path.dirname(__file__)
        expected = os.path.join(base_dir, "images", image_name)
        actual = utils.image_path(name=image_name, base_dir=base_dir)
        self.assertEqual(expected, actual)


class TestCreateButton(unittest.TestCase):
    @unittest.skip
    def test_create_button_returns_button(self):
        button = utils.create_button()
        self.assertIsInstance(button, PySide6.QtWidgets.QPushButton)
