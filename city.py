class City:
    def __init__(self, name: str, x: float, y: float):
        self.name = name
        self.x = x
        self.y = y
        self.is_visited: bool = False

    def get_position(self):
        return self.x, self.y