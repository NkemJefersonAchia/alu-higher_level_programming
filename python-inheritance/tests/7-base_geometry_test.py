#!/usr/bin/python3
"""Test cases for BaseGeometry class"""
import unittest
from 7-base_geometry import BaseGeometry

class TestBaseGeometry(unittest.TestCase):
    def setUp(self):
        self.bg = BaseGeometry()
    
    def test_area(self):
        with self.assertRaises(Exception) as context:
            self.bg.area()
        self.assertEqual(str(context.exception), "area() is not implemented")
    
    def test_integer_validator_valid(self):
        try:
            self.bg.integer_validator("age", 1)
        except Exception as e:
            self.fail(f"integer_validator raised {type(e).__name__} unexpectedly!")
    
    def test_integer_validator_zero(self):
        with self.assertRaises(ValueError) as context:
            self.bg.integer_validator("age", 0)
        self.assertEqual(str(context.exception), "age must be greater than 0")
    
    def test_integer_validator_negative(self):
        with self.assertRaises(ValueError) as context:
            self.bg.integer_validator("age", -4)
        self.assertEqual(str(context.exception), "age must be greater than 0")
    
    def test_integer_validator_string(self):
        with self.assertRaises(TypeError) as context:
            self.bg.integer_validator("age", "4")
        self.assertEqual(str(context.exception), "age must be an integer")
    
    def test_integer_validator_tuple(self):
        with self.assertRaises(TypeError) as context:
            self.bg.integer_validator("age", (4,))
        self.assertEqual(str(context.exception), "age must be an integer")
    
    def test_integer_validator_list(self):
        with self.assertRaises(TypeError) as context:
            self.bg.integer_validator("age", [3])
        self.assertEqual(str(context.exception), "age must be an integer")
    
    def test_integer_validator_bool(self):
        with self.assertRaises(TypeError) as context:
            self.bg.integer_validator("age", True)
        self.assertEqual(str(context.exception), "age must be an integer")
    
    def test_integer_validator_set(self):
        with self.assertRaises(TypeError) as context:
            self.bg.integer_validator("age", {3, 4})
        self.assertEqual(str(context.exception), "age must be an integer")
    
    def test_integer_validator_none(self):
        with self.assertRaises(TypeError) as context:
            self.bg.integer_validator("age", None)
        self.assertEqual(str(context.exception), "age must be an integer")

if __name__ == "__main__":
    unittest.main()
