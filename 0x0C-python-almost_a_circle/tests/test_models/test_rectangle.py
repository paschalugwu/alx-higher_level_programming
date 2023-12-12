#!/usr/bin/python3
"""Test Rectangle module"""
import unittest
from io import StringIO
import sys
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Test class for Rectangle class
    """

    def test_2(self):
        """
        Test for test_2
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10)
        self.asserEqual(r2.id, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_3(self):
        """
        Test for test_3
        """
        with self.assertRaises(TypeError) as e:
            r = Rectangle(10, "2")
        self.assertEqual(str(e.exception), "height must be an integer")

        with self.assertRaises(ValueError) as e:
            r = Rectangle(10, 2)
            r.width = -10
        self.assertEqual(str(e.exception), "width must be > 0")

        with self.assertRaises(TypeError) as e:
            r = Rectangle(10, 2)
            r.x = {}
        self.assertEqual(str(e.exception), "x must be an integer")

        with self.assertRaises(ValueError) as e:
            r = Rectangle(10, 2, 3, -1)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_4(self):
        """
        Testing for test_4
        """
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_5(self):
        """
        test 5
        """
        r1 = Rectangle(4, 6)
        r1.display()
        print("---")
        r2 = Rectangle(2, 2)
        r2.display()

    def test_6(self):
        """
        test_6
        """
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")

    def test_7(self):
        """
        test_7
        """
        r1 = Rectangle(2, 3, 2, 2)
        captured_output = StringIO()
        sys.stdout = captured_output
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "\n\n ##\n ##\n ##\n")

        captured_output = StringIO()
        sys.stdout = captured_output
        r2 = Rectangle(3, 2, 1, 0)
        r2.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "\n ###\n ###\n")

    def test_8(self):
        """
        Test 8
        """
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")

        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")

        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")

        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")

        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

    def test_9(self):
        """
        test_9
        """
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")

        r1.update(height=1)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/1")

        r1.update(width=1, x=2)
        self.assertEqual(str(r1), "[Rectangle] (1) 2/10 - 1/1")

        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/1")

        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/3 - 4/2")

    def test_13(self):
        """
        test_13
        """
        r1 = Rectangle(10, 2, 1, 9)
        expected_dict = {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        self.assertEqual(r1.to_dictionary(), expected_dict)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(r2, r1)


if __name__ == '__main__':
    unittest.main()
