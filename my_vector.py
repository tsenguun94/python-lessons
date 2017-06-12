class vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        msg = "(" + str(self.x) + "," + str(self.y) + ")"
        return msg
    def __add__(self, other):
        return vec2(self.x + other.x, self.y + other.y)
