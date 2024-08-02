import tkinter as tk
from tkinter import messagebox
import random

class SlidingPuzzleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sliding Tile Puzzle")

        self.size = 4  # Size of the grid (4x4 for 15-puzzle)
        self.buttons = {}
        self.empty_pos = (self.size - 1, self.size - 1)
        self.puzzle = self.create_puzzle()
        self.create_widgets()
        self.update_buttons()

    def create_puzzle(self):
        numbers = list(range(1, self.size**2)) + [0]  # 0 represents the empty space
        random.shuffle(numbers)  # Shuffle to start with a random configuration
        return [numbers[i * self.size:(i + 1) * self.size] for i in range(self.size)]

    def create_widgets(self):
        for row in range(self.size):
            for col in range(self.size):
                button = tk.Button(self.root, width=5, height=2, font=('Arial', 24), command=lambda r=row, c=col: self.move_tile(r, c))
                button.grid(row=row, column=col)
                self.buttons[(row, col)] = button

    def update_buttons(self):
        for row in range(self.size):
            for col in range(self.size):
                value = self.puzzle[row][col]
                if value == 0:
                    self.buttons[(row, col)].config(text='', bg='white')
                else:
                    self.buttons[(row, col)].config(text=str(value), bg='lightgray')

    def move_tile(self, row, col):
        if (row, col) == self.empty_pos:
            return

        empty_row, empty_col = self.empty_pos
        if (abs(row - empty_row) == 1 and col == empty_col) or (abs(col - empty_col) == 1 and row == empty_row):
            self.puzzle[empty_row][empty_col], self.puzzle[row][col] = self.puzzle[row][col], self.puzzle[empty_row][empty_col]
            self.empty_pos = (row, col)
            self.update_buttons()
            if self.is_solved():
                messagebox.showinfo("Congratulations!", "You have solved the puzzle!")

    def is_solved(self):
        expected = list(range(1, self.size**2)) + [0]
        current = [self.puzzle[r][c] for r in range(self.size) for c in range(self.size)]
        return current == expected

if __name__ == "__main__":
    root = tk.Tk()
    app = SlidingPuzzleApp(root)
    root.mainloop()
