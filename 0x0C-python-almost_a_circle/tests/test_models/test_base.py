#!/usr/bin/python3
"""
test_base module
"""
import unittest
import turtle
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    Test class for Base class
    """

    def test_1(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)

    def test_15(self):
        """
        Test case 15
        """
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(dictionary, {'x': 2, 'width': 10,
                                      'id': 1, 'height': 7, 'y': 8})
        self.assertEqual(type(dictionary), dict)
        self.assertEqual(
            json_dictionary, '[{"x": 2, "width": 10, "id": 1, '
            '"height": 7, "y": 8}]'
        )
        self.assertEqual(type(json_dictionary), str)

    def test_16(self):
        """
        test 16
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(
                file.read(),
                '[{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}, '
                '{"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]'
            )

    def test_17(self):
        """
        test 17
        """
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_input), list)
        self.assertEqual(type(json_list_input), str)
        self.assertEqual(type(list_output), list)
        self.assertEqual(
            list_input,
            [{'height': 4, 'width': 10, 'id': 89},
             {'height': 7, 'width': 1, 'id': 7}]
        )
        self.assertEqual(
            json_list_input,
            '[{"height": 4, "width": 10, "id": 89}, '
            '{"height": 7, "width": 1, "id": 7}]'
            )
        self.assertEqual(list_output, [{'height': 4, 'width': 10,
                                        'id': 89}, {'height': 7,
                                                    'width': 1, 'id': 7}])

    def test_18(self):
        """
        test_18
        """
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), "[Rectangle] (1) 1/0 - 3/5")
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 3/5")
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_19(self):
        """
        test 19
        """
        # Test case for Rectangle class
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        for rect in list_rectangles_input:
            self.assertIn(rect, list_rectangles_output)

        # Test case for square class
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        for square in list_squares_input:
            self.assertIn(square, list_squares_output)

    def test_21(self):
        """
        Test the draw method of Base class
        """
        # Create a list of rectangles
        list_rectangles = [Rectangle(100, 40), Rectangle(90, 110, 30, 10),
                           Rectangle(20, 25, 100, 80)]
        # Create a list of squares
        list_squares = [Square(35), Square(15, 70, 50), Square(80, 30, 70)]
        # Call the draw method of Base class
        Base.draw(list_rectangles, list_squares)
        # Assert that the turtle screen is open
        self.assertTrue(turtle.Screen().isopen())
        # Assert that the correct number of shapes are drawn
        self.assertEqual(len(turtle.getscreen().turtles()),
                         len(list_rectangles) + len(list_squares))
        # Close the turtle screen
        turtle.Screen().bye()


if __name__ == '__main__':
    unittest.main()
