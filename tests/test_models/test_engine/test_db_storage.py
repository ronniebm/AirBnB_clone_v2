#!/usr/bin/python3

import unittest
from os import getenv
import os.path
from datetime import datetime
from models.engine.db_storage import DBStorage
from models import *


@unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db',
                 'Storage type is not database')
class test_DBStorage(unittest.TestCase):
    """
    Test database storage
    """

    @classmethod
    def setUpClass(self):
        storage._DBStorage__session.close()
        self.store = DBStorage()
        self.store.reload()

    @classmethod
    def tearDownClass(self):
        self.store._DBStorage__session.close()
        storage.reload()

    def test_all(self):
        self.assertEqual(len(self.store.all()), 0)
        new_obj = State()
        new_obj.name = 'California'
        self.store.new(new_obj)
        self.assertEqual(len(self.store.all()), 1)
        # Make all('classname') work without console

    def test_new(self):
        new_obj = State()
        new_obj.name = "Texas"
        new_obj.save()
        self.assertTrue(len(self.store.all()), 1)

    def test_save(self):
        self.store.reload()
        new_obj = State()
        new_obj.name = 'Washington'
        self.store.new(new_obj)
        self.store.save()
        self.assertEqual(len(self.store.all()), 4)

    def test_delete(self):
        new_obj = State()
        new_obj.name = "Michigan"
        self.store.new(new_obj)
        self.store.save()
        self.store.delete(new_obj)
        self.assertFalse(new_obj in self.store.all())

    def test_reload(self):
        new_obj = City()
        self.store.new(new_obj)
        self.store.reload()
        test_len = len(self.store.all())
        self.assertEqual(test_len, 3)
        self.store.reload()
        for value in self.store.all().values():
            self.assertIsInstance(value.created_at, datetime)
