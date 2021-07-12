class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __gt__(self, other):
        if self.x > other.x:
            return True
        elif self.x == other.x and self.y > other.y:
            return True
        return False

    def __le__(self, other):
        if self.x < other.x:
            return True
        elif self.x == other.x and self.y < other.y:
            return True
        elif self.x == other.x and self.y == other.y:
            return True
        else:
            return False