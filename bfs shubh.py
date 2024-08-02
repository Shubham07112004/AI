import tkinter as tk
from tkinter import messagebox
from collections import deque

class BFSApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BFS Visualization")

        # Canvas setup
        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack()

        # Graph setup with specific node positions
        self.nodes = {
            1: (100, 100),  # Top node
            2: (300, 100),  # Node to the right of node 1
            3: (500, 100),  # Node to the right of node 2
            4: (200, 300),  # Node below node 1
            5: (400, 300),  # Node below node 2
            6: (600, 300),  # Node below node 3
            7: (200, 500),  # Node below node 4
            8: (400, 500)   # Node below node 5
        }

        self.edges = {
            (1, 2): None, (1, 4): None,
            (2, 3): None, (2, 5): None,
            (3, 6): None,
            (4, 7): None,
            (5, 8): None
        }

        # Draw nodes and edges
        self.draw_nodes()
        self.draw_edges()

        # BFS setup
        self.visited = set()
        self.queue = deque()
        self.path = []
        self.step_index = 0
        self.delay = 1000  # milliseconds

        # Run BFS button
        self.run_button = tk.Button(root, text="Run BFS", command=self.run_bfs)
        self.run_button.pack()

    def draw_nodes(self):
        self.node_ids = {}
        for node, (x, y) in self.nodes.items():
            self.node_ids[node] = self.canvas.create_oval(
                x - 20, y - 20, x + 20, y + 20, fill="lightblue", outline="black"
            )
            self.canvas.create_text(x, y, text=str(node), tags="node")

    def draw_edges(self):
        for (start, end) in self.edges.keys():
            x1, y1 = self.nodes[start]
            x2, y2 = self.nodes[end]
            edge = self.canvas.create_line(x1, y1, x2, y2, fill="black")
            self.edges[(start, end)] = edge
            self.edges[(end, start)] = edge  # For undirected graph

    def run_bfs(self):
        self.visited.clear()
        self.queue.clear()
        self.path = []
        self.step_index = 0
        self.bfs(1)  # Start BFS from node 1
        self.highlight_path_step_by_step()

    def bfs(self, start_node):
        self.queue.append(start_node)
        self.visited.add(start_node)

        while self.queue:
            node = self.queue.popleft()
            self.path.append(node)
            for neighbor in self.get_neighbors(node):
                if neighbor not in self.visited:
                    self.visited.add(neighbor)
                    self.queue.append(neighbor)

    def get_neighbors(self, node):
        return [end for (start, end) in self.edges.keys() if start == node] + \
               [start for (start, end) in self.edges.keys() if end == node]

    def highlight_path_step_by_step(self):
        if self.step_index < len(self.path):
            node = self.path[self.step_index]
            # Color the node
            self.canvas.itemconfig(self.node_ids[node], fill="lightgreen")
            if self.step_index > 0:
                start = self.path[self.step_index - 1]
                end = self.path[self.step_index]
                edge = self.edges.get((start, end)) or self.edges.get((end, start))
                if edge:
                    self.canvas.itemconfig(edge, fill="red", width=2)
            self.step_index += 1
            self.root.after(self.delay, self.highlight_path_step_by_step)
        else:
            messagebox.showinfo("BFS Complete", "BFS traversal is complete!")

if __name__ == "__main__":
    root = tk.Tk()
    app = BFSApp(root)
    root.mainloop()
