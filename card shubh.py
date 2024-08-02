import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk

class CardShufflerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Card Shuffler")

        # Load card images
        self.card_images = {}
        self.load_card_images()

        # Create a canvas for displaying cards
        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack()

        # Shuffle button
        self.shuffle_button = tk.Button(root, text="Shuffle Deck", command=self.shuffle_deck)
        self.shuffle_button.pack()

        # Create deck of cards
        self.create_deck()
        self.draw_deck()

    def load_card_images(self):
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        for suit in suits:
            for rank in ranks:
                image_path = f'cards/{rank}_of_{suit}.png'  # Path to card images
                image = Image.open(image_path)
                image = image.resize((100, 140), Image.ANTIALIAS)
                self.card_images[f'{rank}_of_{suit}'] = ImageTk.PhotoImage(image)

    def create_deck(self):
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.deck = [f'{rank}_of_{suit}' for suit in suits for rank in ranks]

    def shuffle_deck(self):
        random.shuffle(self.deck)
        self.draw_deck()

    def draw_deck(self):
        self.canvas.delete("all")
        x = 10
        y = 10
        for card in self.deck:
            if x + 110 > 800:
                x = 10
                y += 150
            if y + 150 > 600:
                break
            self.canvas.create_image(x, y, anchor="nw", image=self.card_images[card])
            x += 110

if __name__ == "__main__":
    root = tk.Tk()
    app = CardShufflerApp(root)
    root.mainloop()
