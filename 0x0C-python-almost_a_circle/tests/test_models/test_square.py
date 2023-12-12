#!/usr/bin/python3
"""
test_square module
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    test_10A
    """
    def test_10A(self):
        """
        test_10A
        """
        s1 = Square(5)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)

        s2 = Square(2, 2)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 0)
        self.assertEqual(s2.width, 3)
        self.assertEqual(s2.height, 2)

        s3 = Square(3, 1, 3)
        self.assertEqual(s2.id, 3)
        self.assertEqual(s3.x, 1)
        self.assertEqual(s3.y, 3)
        self.assertEqual(s3.width, 3)
        self.assertEqual(s3.height, 3)

    def test_10B(self):
        """
        test_10B
        """
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")

        s2 = Square(2, 2)
        self.assertEqual(str(s2), "[Sqare] (2) 2/0 - 2")

        s3 = Square(3, 1, 3)
        self.assertEqual(str(s3), "[Square] (3) 1/3 - 3")

    def test_10C(self):
        """
        test_10C
        """
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

        s2 = Square(2)
        self.assertEqual(s2.area(), 4)

        s3 = Square(3, 1, 3)
        self.assertEqual(s3.area(), 9)

    def test_10D(self):
        """
        test_10D
        """
        s1 = Square(5)
        s1.display()

        s2 = Square(2)
        s2.display()

        s3 = Square(3, 1, 3)
        s3.display()

    def test_11(self):
        """
        test_11
        """
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        s1.size = 10
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)

        s2 = Square(2)
        self.assertEqual(s2.size, 2)
        s2.size = 4
        self.assertEqual(s2.size, 4)
        self.assertEqual(s2.width, 4)
        self.assertEqual(s2.height, 4)

        s3 = Square(3, 1, 3)
        self.assertEqual(s3.size, 3)
        s3.size = 6
        self.assertEqual(s3.size, 6)
        self.assertEqual(s3.width, 6)
        self.assertEqual(s3.height, 6)

        try:
            s1.size = "9"
        except Exception as e:
            self.assertEqual(str(e), "width must be an integer")

    def test_12(self):
        """
        test 12
        """
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")

        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")

        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")

        s1.update(1, 2, 3)
        self.assertEqual(str(s1), "[Square] (1) 3/0 - 2")

        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")

        s1.update(x=12)
        self.assertEqual(str(s1), "[Square] (1) 12/4 - 2")

        s1.update(size=7, y=1)
        self.assertEqual(str(s1), "[Square] (1) 12/1 - 7")

        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1), "[Square] (89) 12/1 - 7")

    def test_14(self):
        """
        test 14
        """
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary, {'id': 1, 'x': 2, 'size': 10, 'y': 1})
        self.assertEqual(type(s1_dictionary), dict)

        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        self.assertEqual(str(s1), "[Square] (1) 2/1 - 10")
        self.assertEqual(str(s2), "[Square] (1) 2/1 - 10")
        self.assertFalse(s1 == s2)


if __name__ == '__main__':
    unittest.main()
