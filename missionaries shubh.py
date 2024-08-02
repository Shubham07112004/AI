import tkinter as tk
from tkinter import messagebox
from collections import deque

class MissionariesCannibalsSolverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Missionaries and Cannibals Solver")

        # Initialize state
        self.initial_state = (3, 3, 0, 0, 'left')  # (m_left, c_left, m_right, c_right, boat)
        self.reset_game()

        # Create the canvas for drawing
        self.canvas = tk.Canvas(root, width=600, height=400, bg='white')
        self.canvas.pack()

        # Control buttons
        self.solve_button = tk.Button(root, text="Solve", command=self.solve)
        self.solve_button.pack(side=tk.LEFT, padx=10)

        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack(side=tk.LEFT, padx=10)

        # Draw the initial game state
        self.draw_game()

    def reset_game(self):
        self.m_left, self.c_left, self.m_right, self.c_right, self.boat = self.initial_state
        self.history = []
        self.solution = []
        self.solving = False

    def draw_game(self):
        self.canvas.delete("all")  # Clear the canvas

        # Draw river
        self.canvas.create_rectangle(50, 200, 550, 220, fill="blue")

        # Draw boat
        boat_x = 50 if self.boat == 'left' else 500
        self.canvas.create_rectangle(boat_x, 180, boat_x + 40, 200, fill="brown")
        self.canvas.create_text(boat_x + 20, 190, text="Boat", fill="white")

        # Draw missionaries and cannibals on the left side
        self.draw_people(100, 150, self.m_left, self.c_left, "left")

        # Draw missionaries and cannibals on the right side
        self.draw_people(400, 150, self.m_right, self.c_right, "right")

        # Check for win condition
        if self.m_right == 3 and self.c_right == 3:
            messagebox.showinfo("Congratulations", "You won the game!")

    def draw_people(self, x, y, missionaries, cannibals, side):
        for i in range(missionaries):
            self.canvas.create_oval(x, y - i * 30, x + 20, y - i * 30 + 20, fill="white", outline="black")
            self.canvas.create_text(x + 10, y - i * 30 + 10, text="M", fill="black")

        for i in range(cannibals):
            self.canvas.create_oval(x + 30, y - i * 30, x + 50, y - i * 30 + 20, fill="green", outline="black")
            self.canvas.create_text(x + 40, y - i * 30 + 10, text="C", fill="black")

        # Draw labels
        if side == "left":
            self.canvas.create_text(x + 10, y + 20, text=f"{missionaries} Missionaries", fill="black")
            self.canvas.create_text(x + 40, y + 20, text=f"{cannibals} Cannibals", fill="black")
        else:
            self.canvas.create_text(x + 10, y + 20, text=f"{missionaries} Missionaries", fill="black")
            self.canvas.create_text(x + 40, y + 20, text=f"{cannibals} Cannibals", fill="black")

    def solve(self):
        self.reset_game()
        self.solving = True
        self.solution = self.bfs_solve()
        if not self.solution:
            messagebox.showinfo("No Solution", "No solution found.")
        else:
            self.show_solution()

    def show_solution(self):
        if not self.solving or not self.solution:
            return

        for state in self.solution:
            self.m_left, self.c_left, self.m_right, self.c_right, self.boat = state
            self.draw_game()
            self.root.update()
            self.root.after(1000)  # Wait 1 second between moves

    def bfs_solve(self):
        """ Solve the Missionaries and Cannibals problem using Breadth-First Search (BFS). """
        initial_state = self.initial_state
        goal_state = (0, 0, 3, 3, 'right')
        queue = deque([(initial_state, [])])
        visited = set()
        visited.add(initial_state)

        while queue:
            (m_left, c_left, m_right, c_right, boat), path = queue.popleft()

            if (m_left, c_left, m_right, c_right, boat) == goal_state:
                return path

            # Generate all possible moves
            for m_move in range(3):
                for c_move in range(3):
                    if (m_move + c_move) == 0 or (m_move + c_move) > 2:
                        continue

                    new_m_left, new_c_left, new_m_right, new_c_right = m_left, c_left, m_right, c_right
                    if boat == 'left':
                        new_m_left -= m_move
                        new_c_left -= c_move
                        new_m_right += m_move
                        new_c_right += c_move
                        new_boat = 'right'
                    else:
                        new_m_left += m_move
                        new_c_left += c_move
                        new_m_right -= m_move
                        new_c_right -= c_move
                        new_boat = 'left'

                    if self.is_valid_state(new_m_left, new_c_left, new_m_right, new_c_right):
                        new_state = (new_m_left, new_c_left, new_m_right, new_c_right, new_boat)
                        if new_state not in visited:
                            visited.add(new_state)
                            queue.append((new_state, path + [new_state]))

        return None

    def is_valid_state(self, m_left, c_left, m_right, c_right):
        """
        Check if the current state is valid.
        No side should ever have more cannibals than missionaries.
        """
        if (m_left < 0 or m_left > 3 or c_left < 0 or c_left > 3 or 
            m_right < 0 or m_right > 3 or c_right < 0 or c_right > 3):
            return False
        
        if (m_left > 0 and m_left < c_left) or (m_right > 0 and m_right < c_right):
            return False
        
        return True

if __name__ == "__main__":
    root = tk.Tk()
    app = MissionariesCannibalsSolverGUI(root)
    root.mainloop()
