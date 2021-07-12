class queue_item:
    def __init__(self, type, p1, p2):
        self.type = type
        self.p1 = p1
        self.p2 = p2

    def get_line_format(self):
        line = [self.type, self.p1.get_x(), self.p2.get_x(), self.p1.get_y(), self.p2.get_y()]
        return line