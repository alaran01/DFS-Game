import pyxel


class Node:
    def __init__(self, value, x, y):
        self.left = None
        self.right = None
        self.value = value
        self.x = x
        self.y = y
        self.radius = 8
        self.selected = False

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

    def set_selected(self, selected):
        self.selected = selected

    def get_selected(self):
        return self.selected

    def inside(self, x, y):
        right = self.x + self.radius
        left = self.x - self.radius
        up = self.y - self.radius
        down = self.y + self.radius
        if left < x < right and up < y < down:
            return True
        else:
            return False


class App:
    def __init__(self):
        pyxel.init(256, 180)
        pyxel.mouse(True)
        pyxel.load("assets/sound_and_images.pyxres")
        pyxel.image(1).load(0, 0, "assets/game_over.png")
        self.nodes = []
        self.mode_pre_order = False
        self.mode_in_order = False
        self.mode_post_order = False
        self.list_of_orders = []
        self.index_to_check = 0
        self.num_of_lives = 3

        # tree
        n1 = Node(35, 128, 30)
        self.root = n1
        n2 = Node(15, 70, 65)
        n3 = Node(45, 186, 65)
        n4 = Node(13, 35, 100)
        n5 = Node(19, 100, 100)
        n6 = Node(42, 156, 100)
        n7 = Node(55, 221, 100)
        n8 = Node(10, 10, 135)
        n9 = Node(14, 70, 135)
        n10 = Node(39, 128, 135)
        n11 = Node(50, 186, 135)
        n12 = Node(59, 246, 135)

        n1.set_left(n2)
        n1.set_right(n3)
        n2.set_left(n4)
        n2.set_right(n5)
        n3.set_left(n6)
        n3.set_right(n7)
        n4.set_left(n8)
        n4.set_right(n9)
        n6.set_left(n10)
        n7.set_left(n11)
        n7.set_right(n12)

        self.nodes.append(n1)
        self.nodes.append(n2)
        self.nodes.append(n3)
        self.nodes.append(n4)
        self.nodes.append(n5)
        self.nodes.append(n6)
        self.nodes.append(n7)
        self.nodes.append(n8)
        self.nodes.append(n9)
        self.nodes.append(n10)
        self.nodes.append(n11)
        self.nodes.append(n12)

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            x = pyxel.mouse_x
            y = pyxel.mouse_y

            # clicked pre-order button
            if x < 85 and y < 15:
                self.list_of_orders.clear()
                self.index_to_check = 0
                self.mode_pre_order = True
                self.mode_post_order = False
                self.mode_in_order = False
                self.pre_order(self.root)
                pyxel.play(0, 3)

                for node in self.nodes:
                    node.set_selected(False)

            # clicked in-order button
            elif 85 < x < 170 and y < 15:
                self.list_of_orders.clear()
                self.index_to_check = 0
                self.mode_in_order = True
                self.mode_post_order = False
                self.mode_pre_order = False
                self.in_order(self.root)
                pyxel.play(0, 3)

                for node in self.nodes:
                    node.set_selected(False)

            # clicked post-order button
            elif 170 < x and y < 15:
                self.list_of_orders.clear()
                self.index_to_check = 0
                self.mode_post_order = True
                self.mode_pre_order = False
                self.mode_in_order = False
                self.post_order(self.root)
                pyxel.play(0, 3)

                for node in self.nodes:
                    node.set_selected(False)

            # check if clicked on a node
            for node in self.nodes:
                if node.inside(x, y) and len(self.list_of_orders) != 0 and self.index_to_check < len(self.list_of_orders):
                    if node == self.list_of_orders[self.index_to_check]:
                        node.set_selected(True)
                        self.index_to_check += 1
                        pyxel.play(0, 4)

                    else:
                        pyxel.play(0, 0)
                        self.num_of_lives -= 1

    def draw(self):
        pyxel.cls(7)

        # Menu to pick an order
        if self.mode_pre_order:
            pyxel.rect(0, 0, 85, 15, 8)
            pyxel.text(20, 5, "Pre-order", 7)
        else:
            pyxel.rectb(0, 0, 85, 15, 8)
            pyxel.text(20, 5, "Pre-order", 8)

        if self.mode_in_order:
            pyxel.rect(85, 0, 85, 15, 8)
            pyxel.text(110, 5, "In-order", 7)
        else:
            pyxel.rectb(85, 0, 85, 15, 8)
            pyxel.text(110, 5, "In-order", 8)

        if self.mode_post_order:
            pyxel.rect(170, 0, 85, 15, 8)
            pyxel.text(190, 5, "Post-order", 7)
        else:
            pyxel.rectb(170, 0, 85, 15, 8)
            pyxel.text(190, 5, "Post-order", 8)

        # drawing the nodes
        for node in self.nodes:
            if node.get_left() is not None:
                left_child = node.get_left()
                pyxel.line(node.get_x(), node.get_y(), left_child.get_x(), left_child.get_y(), 8)

            if node.get_right() is not None:
                right_child = node.get_right()
                pyxel.line(node.get_x(), node.get_y(), right_child.get_x(), right_child.get_y(), 8)

            if node.get_selected():
                pyxel.circ(node.get_x(), node.get_y(), node.get_radius(), 8)
                pyxel.text(node.get_x() - 3, node.get_y() - 2, str(node.get_value()), 7)

            else:
                pyxel.circ(node.get_x(), node.get_y(), node.get_radius(), 7)
                pyxel.circb(node.get_x(), node.get_y(), node.get_radius(), 8)
                pyxel.text(node.get_x() - 3, node.get_y() - 2, str(node.get_value()), 8)

        # Line at the bottom so I can print the text inside
        pyxel.line(0, 160, 256, 160, 8)

        #  print the node value at the bottom when it is correct
        x = 5
        y = 168
        for n in self.list_of_orders:
            if n.get_selected():
                pyxel.text(x, y, str(n.get_value()), 8)
                x += 15
        if self.index_to_check == len(self.list_of_orders) and len(self.list_of_orders) != 0:
            pyxel.text(x, y, "Well done! ", 8)

        # print instructions
        if self.mode_in_order or self.mode_post_order or self.mode_pre_order:
            if self.index_to_check == len(self.list_of_orders):
                pyxel.text(5, 20, "Finished !!", 8)
                pyxel.text(5, 30, "you won ! ", 8)
            else:
                pyxel.text(5, 20, "Click on the nodes", 8)
                pyxel.text(5, 30, "in the correct order ", 8)
        else:
            pyxel.text(5, 20, "Select one of ", 8)
            pyxel.text(5, 30, "the above options", 8)

        # drawing hearts for lives
        if self.num_of_lives == 0:
            # pyxel.text(190, 30, "Game Over! ", 8)
            pyxel.blt(100, 50, 1, 0, 0, 100, 53)
        else:
            pyxel.text(190, 20, "Lives remaining: ", 8)
            for i in range(self.num_of_lives):
                pyxel.blt(200 + i * 18, 30, 0, 0, 0, 20, 20, 0)


    def pre_order(self, node):
        if node is not None:
            self.list_of_orders.append(node)
            self.pre_order(node.get_left())
            self.pre_order(node.get_right())

    def post_order(self, node):
        if node is not None:
            self.post_order(node.get_left())
            self.post_order(node.get_right())
            self.list_of_orders.append(node)

    def in_order(self, node):
        if node is not None:
            self.in_order(node.get_left())
            self.list_of_orders.append(node)
            self.in_order(node.get_right())


App()

