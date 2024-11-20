import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for the Rectangle class."""

    def test_initialization(self):
        r = Rectangle(10, 20)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)

    def test_area(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)


if __name__ == "__main__":
    unittest.main()
