#!/usr/bin/python3
'''
Module
'''
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import models
import os


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = FileStorage._FileStorage__file_path
        self.storage = FileStorage()
        self.base_model = BaseModel()
        self.user = User()
        self.objects = {
            "BaseModel.{}".format(self.base_model.id): self.base_model,
            "User.{}".format(self.user.id): self.user
        }

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        self.assertEqual(self.storage.all(), {})
        self.storage._FileStorage__objects = self.objects
        self.assertEqual(self.storage.all(), self.objects)

    def test_new(self):
        self.assertNotIn("BaseModel.{}".format(self.base_model.id), self.storage.all())
        self.storage.new(self.base_model)
        self.assertIn("BaseModel.{}".format(self.base_model.id), self.storage.all())

    def test_save_and_reload(self):
        with self.assertRaises(FileNotFoundError):
            self.storage.reload()

        self.storage._FileStorage__objects = self.objects
        self.storage.save()
        self.storage.reload()

        self.assertEqual(self.storage.all(), self.objects)

if __name__ == "__main__":
    unittest.main()
