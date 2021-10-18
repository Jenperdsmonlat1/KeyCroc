from PIL import Image

class Creator:

    def __init__(self, width, height, red, green, blue):

        self.width = width
        self.height = height
        self.r = red
        self.g = green
        self.b = blue

    def create_img(self):

        self.img = Image.new('RGBA', (self.width, self.height))

        for i in range(self.width):
            for j in range(self.height):

                self.img.putpixel((i, j), (self.r, self.g, self.b))

        self.img.show()

    def save_img(self, name):

        self.img.save(f"{name}.png")
