import tkinter as tk
from tkinter import messagebox
import time

class DFSVisualizer:
    def __init__(self, master):
        self.master = master
        self.master.title("Depth-First Search Visualizer")
        self.canvas = tk.Canvas(self.master, width=600, height=400, bg="white")
        self.canvas.pack()

        self.graph = {
            1: [2, 3],
            2: [4, 5],
            3: [6, 7],
            4: [],
            5: [],
            6: [],
            7: []
        }
        
        self.positions = {
            1: (300, 50),
            2: (150, 150),
            3: (450, 150),
            4: (100, 250),
            5: (200, 250),
            6: (400, 250),
            7: (500, 250)
        }

        self.visited = set()
        self.draw_graph()
        
        self.start_button = tk.Button(self.master, text="Start DFS", command=self.start_dfs)
        self.start_button.pack()

    def draw_graph(self):
        for node, edges in self.graph.items():
            x, y = self.positions[node]
            self.canvas.create_oval(x-20, y-20, x+20, y+20, fill="lightblue", outline="black", width=2)
            self.canvas.create_text(x, y, text=str(node), font=("Arial", 14, "bold"))
            
            for edge in edges:
                ex, ey = self.positions[edge]
                self.canvas.create_line(x, y, ex, ey, fill="black", width=2)
        
    def dfs(self, node):
        stack = [node]
        
        while stack:
            current = stack.pop()
            if current not in self.visited:
                self.visited.add(current)
                self.highlight_node(current)
                self.master.update()
                time.sleep(1)
                
                for neighbor in self.graph[current]:
                    stack.append(neighbor)
                    
    def highlight_node(self, node):
        x, y = self.positions[node]
        self.canvas.create_oval(x-20, y-20, x+20, y+20, fill="yellow", outline="black", width=2)
        self.canvas.create_text(x, y, text=str(node), font=("Arial", 14, "bold"))

    def start_dfs(self):
        self.visited.clear()
        self.canvas.delete("all")
        self.draw_graph()
        self.dfs(1)
        messagebox.showinfo("Completed", "Depth-First Search Completed")

if __name__ == "__main__":
    root = tk.Tk()
    app = DFSVisualizer(root)
    root.mainloop()
