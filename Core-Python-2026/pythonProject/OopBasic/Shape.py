class Shape:

    def __init__(self):
        self.color = ''
        self.borderWidth = 0

    def set_color(self, c):
        self.color = c

    def get_color(self):
        return self.color

    def set_borderWidth(self, bw):
        self.borderWidth = bw

    def get_borderwidth(self):
        return self.borderWidth


s = Shape()
s.set_color("Red")
s.set_borderWidth(5)

print(s.get_color())
print(s.get_borderwidth())
