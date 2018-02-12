import unittest
from tree import Tree
#Create a suite object

suite_obj = unittest.TestSuite()
suite_obj.addTest(Tree('add_employee'))
suite_obj.addTest(Tree('_find'))

