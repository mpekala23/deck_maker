from PIL import Image, ImageDraw, ImageFont

WIDTH = 900
HEIGHT = 1340

# Helper function for dealing with transparent stuff
def put_white_background(img):
    for x in range(img.width):
        for y in range(img.height):
            if img.getpixel((x, y)) == (0, 0, 0, 0):
                img.putpixel((x, y), (255, 255, 255, 255))

# Preprocessing on all the suit images
SMALL_SUIT_SIZE= 104
SUIT_SIZE = 144
clubs = Image.open('clubs.png')
clubs = clubs.resize((SUIT_SIZE, SUIT_SIZE))
put_white_background(clubs)
diamonds = Image.open('diamonds.png')
diamonds = diamonds.resize((SUIT_SIZE, SUIT_SIZE))
put_white_background(diamonds)
hearts = Image.open('hearts.png')
hearts = hearts.resize((SUIT_SIZE, SUIT_SIZE))
put_white_background(hearts)
spades = Image.open('spades.png')
spades = spades.resize((SUIT_SIZE, SUIT_SIZE))
put_white_background(spades)

class Pastement:
    def __init__(self, x, y, o, size=SUIT_SIZE):
        self.x = int(round(x - size / 2))
        self.y = int(round(y - size / 2))
        self.o = o
        self.size = size

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.img = Image.new('RGBA', (WIDTH, HEIGHT), color = 'white')
    
    # Returns the pastements for the center of the card
    def get_center_pastements(self):
        if self.value == "A":
            return [
                Pastement(WIDTH / 2, HEIGHT / 2, False),
            ]
        if self.value == "2":
            return [
                Pastement(WIDTH / 2, HEIGHT * 0.25, False),
                Pastement(WIDTH / 2, HEIGHT * 0.75, True),
            ]
        if self.value == "3":
            return [
                Pastement(WIDTH / 2, HEIGHT * 0.25, False),
                Pastement(WIDTH / 2, HEIGHT * 0.5, False),
                Pastement(WIDTH / 2, HEIGHT * 0.75, True),
            ]
        if self.value == "4":
            return [
                Pastement(WIDTH / 3, HEIGHT * 0.25, False),
                Pastement(WIDTH / 3, HEIGHT * 0.75, True),
                Pastement(2 * WIDTH / 3, HEIGHT * 0.25, False),
                Pastement(2 * WIDTH / 3, HEIGHT * 0.75, True),
            ]
        if self.value == "5":
            return [
                Pastement(WIDTH / 3, HEIGHT * 0.25, False),
                Pastement(WIDTH / 3, HEIGHT * 0.75, True),
                Pastement(WIDTH / 2, HEIGHT * 0.5, False),
                Pastement(2 * WIDTH / 3, HEIGHT * 0.25, False),
                Pastement(2 * WIDTH / 3, HEIGHT * 0.75, True),
            ]
        if self.value == "6":
            return [
                Pastement(WIDTH / 3, HEIGHT * 0.25, False),
                Pastement(WIDTH / 3, HEIGHT * 0.75, True),
                Pastement(WIDTH / 3, HEIGHT * 0.5, False),
                Pastement(2 * WIDTH / 3, HEIGHT * 0.5, False),
                Pastement(2 * WIDTH / 3, HEIGHT * 0.25, False),
                Pastement(2 * WIDTH / 3, HEIGHT * 0.75, True),
            ]
        if self.value == "7":
            return [
                Pastement(WIDTH / 3, HEIGHT * 0.25, False),
                Pastement(WIDTH / 3, HEIGHT * 0.75, True),
                Pastement(WIDTH / 3, HEIGHT * 0.5, False),
                Pastement(2 * WIDTH / 3, HEIGHT * 0.5, False),
                Pastement(WIDTH / 2, HEIGHT * 0.375, False),
                Pastement(2 * WIDTH / 3, HEIGHT * 0.25, False),
                Pastement(2 * WIDTH / 3, HEIGHT * 0.75, True),
            ]
        if self.value == "8":
            return [
                Pastement(WIDTH / 3, HEIGHT * 0.25, False),
                Pastement(WIDTH / 3, HEIGHT * 0.415, False),
                Pastement(WIDTH / 3, HEIGHT * 0.58, True),
                Pastement(WIDTH / 3, HEIGHT * 0.75, True),
                Pastement(2 * WIDTH / 3, HEIGHT * 0.25, False),
                Pastement(2 * WIDTH / 3, HEIGHT * 0.415, False),
                Pastement(2 * WIDTH / 3, HEIGHT * 0.58, True),
                Pastement(2 * WIDTH / 3, HEIGHT * 0.75, True),
            ]
        if self.value == "9":
            return [
                Pastement(WIDTH / 3, HEIGHT * 0.25, False),
                Pastement(WIDTH / 3, HEIGHT * 0.415, False),
                Pastement(WIDTH / 3, HEIGHT * 0.58, True),
                Pastement(WIDTH / 3, HEIGHT * 0.75, True),
                Pastement(WIDTH / 2, HEIGHT * 0.5, False),
                Pastement(2 * WIDTH / 3, HEIGHT * 0.25, False),
                Pastement(2 * WIDTH / 3, HEIGHT * 0.415, False),
                Pastement(2 * WIDTH / 3, HEIGHT * 0.58, True),
                Pastement(2 * WIDTH / 3, HEIGHT * 0.75, True),
            ]
        if self.value == "10":
            return [
                Pastement(WIDTH / 3, HEIGHT * 0.25, False),
                Pastement(WIDTH / 3, HEIGHT * 0.415, False),
                Pastement(WIDTH / 3, HEIGHT * 0.58, True),
                Pastement(WIDTH / 3, HEIGHT * 0.75, True),
                Pastement(WIDTH / 2, HEIGHT * 0.3325, False),
                Pastement(WIDTH / 2, HEIGHT * 0.6675, True),
                Pastement(2 * WIDTH / 3, HEIGHT * 0.25, False),
                Pastement(2 * WIDTH / 3, HEIGHT * 0.415, False),
                Pastement(2 * WIDTH / 3, HEIGHT * 0.58, True),
                Pastement(2 * WIDTH / 3, HEIGHT * 0.75, True),
            ]
        return []
    
    # Returns the pastements for the corners of the card
    def get_corner_pastements(self):
        return [
            Pastement(SMALL_SUIT_SIZE, SMALL_SUIT_SIZE * 2.5, False, SMALL_SUIT_SIZE),
            Pastement(WIDTH - SMALL_SUIT_SIZE, HEIGHT - SMALL_SUIT_SIZE * 2.5, True, SMALL_SUIT_SIZE),
        ]

    # Returns all the pastements
    def get_pastements(self):
        return self.get_center_pastements() + self.get_corner_pastements()

    # Helper function for pasting images, takes care of flipping
    def helper_paste(self, pastement):
        paste_img = self.suit.resize((pastement.size, pastement.size))
        if pastement.o:
            paste_img = paste_img.transpose(Image.FLIP_TOP_BOTTOM)
        self.img.paste(
            paste_img, 
            (pastement.x, pastement.y)
        )
    
    # Draws the value of the card
    def draw_value(self):
        letter = Image.new('RGBA', (SMALL_SUIT_SIZE * 2, SMALL_SUIT_SIZE * 2), color = 'white')
        draw = ImageDraw.Draw(letter)
        font = ImageFont.truetype('pixeloid-sans/PixeloidSans-Bold.ttf', 136)
        (width, height) = draw.textsize(self.value, font=font)
        fill = '#EC1D24' if self.suit == hearts or self.suit == diamonds else 'black'
        draw.text(
            (SMALL_SUIT_SIZE - width / 2 , SMALL_SUIT_SIZE - height / 2),
            self.value,
            fill=fill,
            font=font
        )
        extra_x = 0 if len(self.value) == 1 else 16
        self.img.paste(letter, (extra_x, 0))
        letter = letter.rotate(180)
        self.img.paste(letter, (round(WIDTH - SMALL_SUIT_SIZE * 2 - extra_x), round(HEIGHT - SMALL_SUIT_SIZE * 2)))
    
    def make_image(self):
        # Place the suits
        for pastement in self.get_pastements():
            self.helper_paste(pastement)
        # Draw the value
        self.draw_value()
        return self.img

            
aceSpades = Card(hearts, "9")
aceSpades.make_image().save("card.png")