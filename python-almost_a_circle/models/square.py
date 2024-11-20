from models.rectangle import Rectangle


class Square(Rectangle):
    """A square class inheriting from Rectangle."""

    def __init__(self, size, id=None):
        super().__init__(size, size, id)
        self.size = size
