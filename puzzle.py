import tkinter as tk
from tkinter import messagebox
import random

class PuzzleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Shifting Puzzle")

        self.grid_size = 4
        self.tile_size = 100
        self.blank_tile = self.grid_size * self.grid_size - 1
        self.tiles = list(range(self.grid_size * self.grid_size))
        self.shuffle_tiles()

        self.canvas = tk.Canvas(root, width=self.grid_size * self.tile_size, height=self.grid_size * self.tile_size, bg="white")
        self.canvas.pack()

        self.draw_tiles()
        self.canvas.bind("<Button-1>", self.handle_click)

    def shuffle_tiles(self):
        random.shuffle(self.tiles)
        # Ensure the puzzle is solvable
        while not self.is_solvable():
            random.shuffle(self.tiles)

    def draw_tiles(self):
        self.canvas.delete("all")
        for i, tile in enumerate(self.tiles):
            x = (i % self.grid_size) * self.tile_size
            y = (i // self.grid_size) * self.tile_size
            if tile != self.blank_tile:
                self.canvas.create_rectangle(x, y, x + self.tile_size, y + self.tile_size, fill="lightblue", outline="black")
                self.canvas.create_text(x + self.tile_size / 2, y + self.tile_size / 2, text=str(tile + 1), font=("Arial", 24))
            else:
                self.canvas.create_rectangle(x, y, x + self.tile_size, y + self.tile_size, fill="white", outline="black")

    def handle_click(self, event):
        x = event.x // self.tile_size
        y = event.y // self.tile_size
        clicked_tile_index = y * self.grid_size + x
        if self.is_adjacent(clicked_tile_index, self.tiles.index(self.blank_tile)):
            self.tiles[self.tiles.index(self.blank_tile)], self.tiles[clicked_tile_index] = self.tiles[clicked_tile_index], self.tiles[self.tiles.index(self.blank_tile)]
            self.draw_tiles()
            if self.is_solved():
                messagebox.showinfo("Puzzle Solved", "Congratulations! You've solved the puzzle!")

    def is_adjacent(self, index1, index2):
        x1, y1 = index1 % self.grid_size, index1 // self.grid_size
        x2, y2 = index2 % self.grid_size, index2 // self.grid_size
        return (abs(x1 - x2) == 1 and y1 == y2) or (abs(y1 - y2) == 1 and x1 == x2)

    def is_solvable(self):
        inversions = 0
        flat_tiles = [tile for tile in self.tiles if tile != self.blank_tile]
        for i in range(len(flat_tiles)):
            for j in range(i + 1, len(flat_tiles)):
                if flat_tiles[i] > flat_tiles[j]:
                    inversions += 1
        return inversions % 2 == 0

    def is_solved(self):
        return self.tiles == list(range(self.grid_size * self.grid_size))

if __name__ == "__main__":
    root = tk.Tk()
    app = PuzzleApp(root)
    root.mainloop()
