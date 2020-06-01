import pyxel

class Node:
    def __init__(self, value, x, y):
        self.left = None
        self.right = None
        self.value = value
        self.x = x
        self.y = y
        self.radius = 8

    def set_left(self, left):
        self.left = left

    def get_left(self):
        return self.left

    def set_right(self, right):
        self.right = right

    def get_right(self):
        return self.right

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_value(self):
        return self.value

    def get_radius(self):
        return self.radius


class App:
    def __init__(self):
        pyxel.init(256, 180)
        pyxel.mouse(True)
        pyxel.load("assets/sound.pyxres")
        self.nodes = []

        n1 = Node(10, 120, 30)
        n2 = Node(32, 60, 60)
        n3 = Node(15, 30, 90)

        self.nodes.append(n1)
        self.nodes.append(n2)
        self.nodes.append(n3)

        pyxel.run(self.update, self.draw)

    def update(self):
        if(pyxel.btnp(pyxel.KEY_ENTER)):
            pyxel.play(0, 0)
        if (pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON)):
            pyxel.play(0, 1)

    def draw(self):
        pyxel.cls(7)

        # Menu to pick an order
        pyxel.rectb(0, 0, 85, 15, 8)
        pyxel.rectb(85, 0, 85, 15, 8)
        pyxel.rectb(170, 0, 85, 15, 8)
        pyxel.text(20, 5, "Pre-order", 8)
        pyxel.text(110, 5, "In-order", 8)
        pyxel.text(190, 5, "Post-order", 8)

        # Line at the bottom so I can print the text inside
        pyxel.line(0, 160, 256, 160, 8)

        for node in self.nodes:
            pyxel.circb(node.get_x(), node.get_y(), node.get_radius(), 8)
            pyxel.text(node.get_x()-3, node.get_y()-2, str(node.get_value()), 8)


        # Drawing circle with text inside
        # Left hand side
        # pyxel.circb(120, 30, 8, 8)
        # pyxel.text(120, 28, "8", 8)
        #
        # pyxel.circb(60, 60, 8, 8)
        # pyxel.text(60, 58, "3", 8)

        # pyxel.circb(120, 30, 8, 8)
        # pyxel.text(120, 28, "1", 8)
        #
        # pyxel.circb(120, 30, 8, 8)
        # pyxel.text(120, 28, "5", 8)
        #
        # pyxel.circb(120, 30, 8, 8)
        # pyxel.text(120, 28, "7", 8)
        #
        # pyxel.circb(120, 30, 8, 8)
        # pyxel.text(120, 28, "4", 8)

        # Right hand side
        # pyxel.circb(120, 30, 8, 8)
        # pyxel.text(120, 28, "6", 8)
        #
        # pyxel.circb(120, 30, 8, 8)
        # pyxel.text(120, 28, "9", 8)
        #
        # pyxel.circb(120, 30, 8, 8)
        # pyxel.text(120, 28, "2", 8)


App()