import unittest
from src.main.lab import Circle, Rectangle,Shape

class TestCircle(unittest.TestCase):
    def test_circle_area_override(self):
        circle = Circle(5)
        self.assertTrue(isinstance(circle, Shape), "Circle class should inherit from Shape class")
        self.assertTrue(hasattr(circle, 'area'), "Circle class should override the area() method")

    def test_circle_area_calculation(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), 78.54, places=2, msg="Incorrect area calculation for circle")

class TestRectangle(unittest.TestCase):
    def test_rectangle_area_override(self):
        rectangle = Rectangle(4, 6)
        self.assertTrue(isinstance(rectangle, Shape), "Rectangle class should inherit from Shape class")
        self.assertTrue(hasattr(rectangle, 'area'), "Rectangle class should override the area() method")

    def test_rectangle_area_calculation(self):
        rectangle = Rectangle(4, 6)
        self.assertEqual(rectangle.area(), 24, "Incorrect area calculation for rectangle")

if __name__ == '__main__':
    unittest.main()
