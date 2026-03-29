import tkinter as tk
from tkinter import messagebox
import random

class VacuumGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Code-a-Bot: Vacuum Challenge")
        
        # Game State
        self.size = 5
        self.grid_size = 100
        self.visited = set()
        self.moves = 0
        self.repeats = 0
        
        # Start at a random position
        self.pos_x = random.randint(0, self.size - 1)
        self.pos_y = random.randint(0, self.size - 1)
        self.visited.add((self.pos_x, self.pos_y))

        # UI Elements
        self.canvas = tk.Canvas(root, width=500, height=500, bg="white")
        self.canvas.pack()
        
        self.stats_label = tk.Label(root, text="Moves: 0 | Repeats: 0 | Cleaned: 1/25", font=("Arial", 14))
        self.stats_label.pack()

        self.draw_grid()
        self.robot = self.draw_robot()

    def draw_grid(self):
        for i in range(self.size):
            for j in range(self.size):
                x1, y1 = i * self.grid_size, j * self.grid_size
                x2, y2 = x1 + self.grid_size, y1 + self.grid_size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="lightgray", fill="#f0f0f0")

    def draw_robot(self):
        x = self.pos_x * self.grid_size + 10
        y = self.pos_y * self.grid_size + 10
        return self.canvas.create_oval(x, y, x+80, y+80, fill="blue", outline="darkblue")

    def update_ui(self):
        # Move the robot on screen
        nx = self.pos_x * self.grid_size + 10
        ny = self.pos_y * self.grid_size + 10
        self.canvas.coords(self.robot, nx, ny, nx+80, ny+80)
        
        # Color the "cleaned" tile
        cx1, cy1 = self.pos_x * self.grid_size, self.pos_y * self.grid_size
        self.canvas.create_rectangle(cx1, cy1, cx1+100, cy1+100, fill="#ccffcc", outline="lightgray")
        self.canvas.tag_raise(self.robot)
        
        # Update Stats
        self.stats_label.config(text=f"Moves: {self.moves} | Repeats: {self.repeats} | Cleaned: {len(self.visited)}/25")

    # --- ROBOT COMMANDS FOR KIDS ---
    
    def move_up(self):
        if self.pos_y > 0: self.pos_y -= 1
        self.process_move()

    def move_down(self):
        if self.pos_y < self.size - 1: self.pos_y += 1
        self.process_move()

    def move_left(self):
        if self.pos_x > 0: self.pos_x -= 1
        self.process_move()

    def move_right(self):
        if self.pos_x < self.size - 1: self.pos_x += 1
        self.process_move()

    def process_move(self):
        self.moves += 1
        if (self.pos_x, self.pos_y) in self.visited:
            self.repeats += 1
        else:
            self.visited.add((self.pos_x, self.pos_y))
        
        self.update_ui()
        self.root.update()
        self.root.after(200) # Small delay so kids can see the movement

# --- THE KID'S PROGRAMMING AREA ---

def run_robot_program(bot):
    """
    KIDS: Write your code here! 
    Available commands:
    bot.move_up()
    bot.move_down()
    bot.move_left()
    bot.move_right()
    """
    
    # Example: Simple zigzag pattern
    for i in range(5):
        for j in range(4):
            bot.move_right()
        bot.move_down()
        for j in range(4):
            bot.move_left()
        bot.move_down()

# Setup Game
if __name__ == "__main__":
    window = tk.Tk()
    game = VacuumGame(window)
    
    # Button to start the kid's code
    start_btn = tk.Button(window, text="START CLEANING", command=lambda: run_robot_program(game))
    start_btn.pack(pady=10)
    
    window.mainloop()
