#Write tests for the Vector class (Homework 6) using the 'unittest' or 'pytest' module.

import unittest
import math

# Import the Vector class
import sys
sys.path.append(r"C:\Users\joann\OneDrive\Dokumenty\python programowanie\homework6")
from ex61 import Vector  

class VectorTest(unittest.TestCase):

    def test_vector_eq(self):
        v1 = Vector(2, 1, -1)
        v2 = Vector(2, 1, -1)
        self.assertEqual(v1, v2)

    def test_vector_ne(self):
        v1 = Vector(2, 1, -1)
        v2 = Vector(3, 1, 2)
        self.assertNotEqual(v1, v2)

    def test_vector_add(self):
        v1 = Vector(2, 1, -1)
        v2 = Vector(3, 1, 2)
        result = v1 + v2
        self.assertEqual(result, Vector(5, 2, 1))

    def test_vector_sub(self):
        v1 = Vector(2, 1, -1)
        v2 = Vector(3, 1, 2)
        result = v1 - v2
        self.assertEqual(result, Vector(-1, 0, -3))

    def test_vector_mul(self):
        v1 = Vector(2, 1, -1)
        v2 = Vector(3, 1, 2)
        result = v1 * v2
        self.assertEqual(result, 5)

    def test_vector_cross(self):
        v1 = Vector(2, 1, -1)
        v2 = Vector(3, 1, 2)
        result = v1.cross(v2)
        self.assertEqual(result, Vector(3, -5, -1))

    def test_vector_length(self):
        v = Vector(2, 1, -1)
        result = v.length()
        self.assertEqual(result, math.sqrt(6))

    def test_vector_hash(self):
        v1 = Vector(2, 1, -1)
        v2 = Vector(2, 1, -1)
        self.assertEqual(hash(v1), hash(v2))

if __name__ == '__main__':
    unittest.main()
