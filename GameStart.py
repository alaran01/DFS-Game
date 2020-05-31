import pyxel

class App:
    def __init__(self):
        pyxel.init(256, 180)
        self.x = 0
        self.y = 0
        pyxel.mouse(True)
        pyxel.load("assets/sound.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        self.x = (self.x + 1) % pyxel.width
        self.y = (self.y + 1) % pyxel.height
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

        # Drawing circle with text inside
        # Left hand side
        pyxel.circb(120, 30, 8, 8)
        pyxel.text(120, 28, "8", 8)

        pyxel.circb(60, 60, 8, 8)
        pyxel.text(60, 58, "3", 8)

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