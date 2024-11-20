import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Tests for the Base class."""

    def test_id_assignment(self):
        b1 = Base()
        b2 = Base(5)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 5)
        self.assertEqual(b3.id, 2)


if __name__ == "__main__":
    unittest.main()
