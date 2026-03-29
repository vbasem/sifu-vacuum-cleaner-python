import tkinter as tk
import random

class VacuumGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Code-a-Bot: Vacuum Challenge")
        
        # Game Constants
        self.size = 5
        self.grid_size = 100
        
        # Setup UI
        self.canvas = tk.Canvas(root, width=500, height=500, bg="white")
        self.canvas.pack()
        
        self.stats_label = tk.Label(root, text="", font=("Arial", 14))
        self.stats_label.pack()

        # Control Buttons
        self.btn_frame = tk.Frame(root)
        self.btn_frame.pack(pady=10)

        self.start_btn = tk.Button(self.btn_frame, text="START PROGRAM", fg="green", command=self.run_code)
        self.start_btn.pack(side="left", padx=5)

        self.reset_btn = tk.Button(self.btn_frame, text="RESET / RANDOMIZE", fg="red", command=self.reset_game)
        self.reset_btn.pack(side="left", padx=5)

        # Initialize the game state for the first time
        self.robot_id = None
        self.reset_game()

    def reset_game(self):
        """Clears the board and picks a new random starting position."""
        self.canvas.delete("all")  # Clear all drawings
        self.visited = set()
        self.moves = 0
        self.repeats = 0
        
        # New random position
        self.pos_x = random.randint(0, self.size - 1)
        self.pos_y = random.randint(0, self.size - 1)
        self.visited.add((self.pos_x, self.pos_y))

        # Re-draw the background grid
        for i in range(self.size):
            for j in range(self.size):
                x1, y1 = i * self.grid_size, j * self.grid_size
                x2, y2 = x1 + self.grid_size, y1 + self.grid_size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="lightgray", fill="#f0f0f0")

        # Create the robot (Round Vacuum)
        self.robot_id = self.draw_robot()
        self.update_ui()

    def draw_robot(self):
        x = self.pos_x * self.grid_size + 15
        y = self.pos_y * self.grid_size + 15
        return self.canvas.create_oval(x, y, x+70, y+70, fill="blue", outline="black", width=2)

    def update_ui(self):
        # Update the visual position of the robot
        nx = self.pos_x * self.grid_size + 15
        ny = self.pos_y * self.grid_size + 15
        self.canvas.coords(self.robot_id, nx, ny, nx+70, ny+70)
        
        # Leave a "clean" trail (Green tile)
        cx1, cy1 = self.pos_x * self.grid_size, self.pos_y * self.grid_size
        self.canvas.create_rectangle(cx1, cy1, cx1+100, cy1+100, fill="#d1ffd1", outline="lightgray")
        self.canvas.tag_raise(self.robot_id) # Keep robot on top of the green tile
        
        self.stats_label.config(text=f"Moves: {self.moves} | Repeats: {self.repeats} | Cleaned: {len(self.visited)}/25")

    # --- ROBOT COMMANDS FOR KIDS ---
    def move_up(self):
        if self.pos_y > 0: self.pos_y -= 1
        self.process_step()

    def move_down(self):
        if self.pos_y < self.size - 1: self.pos_y += 1
        self.process_step()

    def move_left(self):
        if self.pos_x > 0: self.pos_x -= 1
        self.process_step()

    def move_right(self):
        if self.pos_x < self.size - 1: self.pos_x += 1
        self.process_step()

    def process_step(self):
        self.moves += 1
        if (self.pos_x, self.pos_y) in self.visited:
            self.repeats += 1
        else:
            self.visited.add((self.pos_x, self.pos_y))
        
        self.update_ui()
        self.root.update()
        self.root.after(150) # Speed of animation

    def run_code(self):
        # This calls the external function where kids write code
        run_robot_program(self)

# --- TEACHING AREA: THE KID'S PROGRAM ---

def run_robot_program(bot):
    """
    KIDS: Write your instructions below!
    Example: 
    bot.move_right()
    bot.move_down()
    """
    # Simple loop to show off the robot's movement
    for i in range(4):
        bot.move_right()
    for i in range(4):
        bot.move_down()

if __name__ == "__main__":
    root = tk.Tk()
    game = VacuumGame(root)
    root.mainloop()
