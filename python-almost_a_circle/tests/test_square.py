import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests for the Square class."""

    def test_initialization(self):
        s = Square(10)
        self.assertEqual(s.size, 10)

    def test_area(self):
        s = Square(4)
        self.assertEqual(s.area(), 16)


if __name__ == "__main__":
    unittest.main()
