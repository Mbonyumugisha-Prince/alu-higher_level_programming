from models.base import Base


class Rectangle(Base):
    """A rectangle class inheriting from Base."""

    def __init__(self, width, height, id=None):
        super().__init__(id)
        self.width = width
        self.height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height
