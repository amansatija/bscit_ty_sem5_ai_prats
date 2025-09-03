import tkinter as tk
import random
import os

# Suppress deprecation warning
os.environ['TK_SILENCE_DEPRECATION'] = '1'

print("Starting Number Puzzle application...")

class NumberPuzzle:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Puzzle")
        self.size = 3
        self.tiles = list(range(1, self.size * self.size)) + [0]  # Numbers 1-8 and empty (0)
        random.shuffle(self.tiles)  # Shuffle the tiles

        self.buttons = []
        self.create_buttons()
        self.update_grid()

    def create_buttons(self):
        for i in range(self.size * self.size):
            btn = tk.Button(self.root, text=str(self.tiles[i]) if self.tiles[i] != 0 else "",
                            font=("Helvetica", 24), width=4, height=2,
                            command=lambda i=i: self.move_tile(i))
            btn.grid(row=i // self.size, column=i % self.size)
            self.buttons.append(btn)

    def update_grid(self):
        for i in range(self.size * self.size):
            if self.tiles[i] == 0:
                self.buttons[i].config(text="", bg="gray")  # Empty tile
            else:
                self.buttons[i].config(text=str(self.tiles[i]), bg="lightblue")

    def move_tile(self, index):
        empty_index = self.tiles.index(0)
        if self.is_adjacent(index, empty_index):
            self.tiles[empty_index], self.tiles[index] = self.tiles[index], self.tiles[empty_index]
            self.update_grid()
            if self.is_solved():
                self.display_victory_message()

    def is_adjacent(self, index, empty_index):
        row, col = divmod(index, self.size)
        empty_row, empty_col = divmod(empty_index, self.size)
        return abs(row - empty_row) + abs(col - empty_col) == 1  # Check if adjacent

    def is_solved(self):
        return self.tiles == list(range(1, self.size * self.size)) + [0]

    def display_victory_message(self):
        victory_label = tk.Label(self.root, text="Puzzle Solved!", font=("Helvetica", 24), fg="green")
        victory_label.grid(row=self.size, columnspan=self.size)


if __name__ == "__main__":
    print("Initializing Tkinter...")
    root = tk.Tk()
    
    # Position window in the center of the screen
    window_width = 300
    window_height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width/2 - window_width/2)
    center_y = int(screen_height/2 - window_height/2)
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    
    print("Creating puzzle...")
    puzzle = NumberPuzzle(root)
    
    # Bring window to front
    root.lift()
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)
    
    print("Starting main loop...")
    root.mainloop()
    print("Application closed.")