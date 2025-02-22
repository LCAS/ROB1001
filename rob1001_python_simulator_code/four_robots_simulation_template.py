import tkinter as tk

class FourRobotsAnimation:
    def __init__(self, root):
        self.root = root
        self.root.title("Four Robots Simulator")

        self.is_running = False

        self.frame = tk.Frame(root)
        self.frame.pack(side=tk.LEFT, fill=tk.Y)

        self.start_stop_button = tk.Button(self.frame, text="Start", command=self.toggle_animation)
        self.start_stop_button.pack(pady=20)

        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack(side=tk.RIGHT)

        self.red_square = self.canvas.create_rectangle(10, 10, 50, 50, fill="red")
        self.blue_square = self.canvas.create_rectangle(350, 10, 390, 50, fill="blue")
        self.green_square = self.canvas.create_rectangle(10, 350, 50, 390, fill="green")
        self.yellow_square = self.canvas.create_rectangle(350, 350, 390, 390, fill="yellow")

        # Add circles
        self.canvas.create_oval(190, 190, 210, 210, fill="red")  # Red circle in the middle
        self.canvas.create_oval(0, 0, 20, 20, fill="red")  # Red circle in top-left corner
        self.canvas.create_oval(380, 0, 400, 20, fill="blue")  # Blue circle in top-right corner
        self.canvas.create_oval(0, 380, 20, 400, fill="green")  # Green circle in bottom-left corner
        self.canvas.create_oval(380, 380, 400, 400, fill="yellow")  # Yellow circle in bottom-right corner

        self.red_dx = 2  # Change in x-coordinate for red square
        self.red_dy = 2  # Change in y-coordinate for red square
        self.blue_dx = -2  # Change in x-coordinate for blue square
        self.blue_dy = 2  # Change in y-coordinate for blue square
        self.green_dx = 2  # Change in x-coordinate for green square
        self.green_dy = -2  # Change in y-coordinate for green square
        self.yellow_dx = -2  # Change in x-coordinate for yellow square
        self.yellow_dy = -2  # Change in y-coordinate for yellow square

    def toggle_animation(self):
        self.is_running = not self.is_running
        if self.is_running:
            self.start_stop_button.config(text="Stop")
            self.animate()
        else:
            self.start_stop_button.config(text="Start")

    def animate(self):
        if self.is_running:
            self.canvas.move(self.red_square, self.red_dx, self.red_dy)
            self.canvas.move(self.blue_square, self.blue_dx, self.blue_dy)
            self.canvas.move(self.green_square, self.green_dx, self.green_dy)
            self.canvas.move(self.yellow_square, self.yellow_dx, self.yellow_dy)

            red_pos = self.canvas.coords(self.red_square)
            blue_pos = self.canvas.coords(self.blue_square)
            green_pos = self.canvas.coords(self.green_square)
            yellow_pos = self.canvas.coords(self.yellow_square)

            # Check if the squares reach the center or the corners
            if (red_pos[0] <= 10 and red_pos[1] <= 10) or (red_pos[2] >= 190 and red_pos[3] >= 190):
                self.red_dx = -self.red_dx
                self.red_dy = -self.red_dy
            if (blue_pos[0] >= 350 and blue_pos[1] <= 10) or (blue_pos[2] <= 250 and blue_pos[3] >= 190):
                self.blue_dx = -self.blue_dx
                self.blue_dy = -self.blue_dy
            if (green_pos[0] <= 10 and green_pos[1] >= 350) or (green_pos[2] >= 190 and green_pos[3] <= 250):
                self.green_dx = -self.green_dx
                self.green_dy = -self.green_dy
            if (yellow_pos[0] >= 350 and yellow_pos[1] >= 350) or (yellow_pos[2] <= 250 and yellow_pos[3] <= 250):
                self.yellow_dx = -self.yellow_dx
                self.yellow_dy = -self.yellow_dy
            self.root.after(20, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    app = FourRobotsAnimation(root)
    root.mainloop()
