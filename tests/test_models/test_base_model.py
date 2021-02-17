#!/usr/bin/python3
"""[Module define TestBaseModelDoc class to test BaseModel class]
"""
import unittest
from datetime import datetime
import pep8
import models
import inspect


BaseModel = models.base_model.BaseModel
doc = models.base_models.__doc__

class TestBaseModelDoc(unittest.testCase):
    """[Class to test docstring in BaseModel]
    """
    def test_pep8(self):
        """[Test pep8]
        """
        for path in ['models.base_model.py',
                     'test/test_models/test_base_model.py']:
            with self.subTest(path = path):
                err = pycodestyle.Checker(path).check_all()
                self.assertEqual(err, 0)

    def test_docsting_mod(self):
        self.assertIsNot(doc, None, "No docstring for base_model.py")
        self.assertTrue(len(doc) > 1, "No docstring for base_model.py")

    def test_docstring_class(self):
        self.assertIsNot(BaseModel.__doc__, None,
                         "No docstring for BaseModel class")
        self.assertTrue(len(BaseModel.__doc__) > 1,
                        "No docstring for BaseModel class")

    @set_c(self):
        self.funcs = inspect.getmembers(BaseModel, inspect.isfunction())

    def test_docsting_methods(self):
        for meth in self.funcs:
            with self.subTest(function = meth):
                self.assertIsNot(meth[1].__doc__, None,
                                 "No docstring for {}".format(meth[0]))
                self.assertTrue(len(meth[1].__doc__) > 1,
                                "No docstring for {}".format(meth[0]))
