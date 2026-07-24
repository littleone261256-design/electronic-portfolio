import math
import tkinter as tk
from tkinter import messagebox

# ---------------------------------------------------------
# Tank class (right circular cylinder)
# ---------------------------------------------------------
class Tank:
    def __init__(self, height, radius):
        self.height = height
        self.radius = radius

    def volume_cubic_feet(self):
        return math.pi * (self.radius ** 2) * self.height

    def volume_gallons(self):
        return self.volume_cubic_feet() * 7.48052

    def water_weight_pounds(self):
        return self.volume_gallons() * 8.34

    def top_area(self):
        return math.pi * (self.radius ** 2)

    def outside_area(self):
        return 2 * math.pi * self.radius * self.height

    def total_paint_area(self):
        return self.top_area() + self.outside_area()


# ---------------------------------------------------------
# GUI Application Class
# ---------------------------------------------------------
class TankApp:
    def __init__(self, root):
        self.root = root
        root.title("Tank Calculator")

        # -----------------------------
        # Input fields
        # -----------------------------
        tk.Label(root, text="Tank Height (feet):").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        tk.Label(root, text="Tank Radius (feet):").grid(row=1, column=0, padx=10, pady=5, sticky="e")

        self.height_entry = tk.Entry(root)
        self.radius_entry = tk.Entry(root)

        self.height_entry.grid(row=0, column=1, padx=10, pady=5)
        self.radius_entry.grid(row=1, column=1, padx=10, pady=5)

        # -----------------------------
        # Calculate button
        # -----------------------------
        tk.Button(root, text="Calculate", command=self.calculate).grid(row=2, column=0, columnspan=2, pady=10)

        # -----------------------------
        # Output labels
        # -----------------------------
        self.output_text = tk.Text(root, width=50, height=12, state="disabled")
        self.output_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    # ---------------------------------------------------------
    # Validate input and calculate tank values
    # ---------------------------------------------------------
    def calculate(self):
        try:
            height = float(self.height_entry.get())
            radius = float(self.radius_entry.get())

            if height <= 0 or radius <= 0:
                raise ValueError

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter positive numeric values.")
            return

        tank = Tank(height, radius)

        # Prepare results
        results = (
            f"Total Volume (cubic feet): {tank.volume_cubic_feet():.2f}\n"
            f"Total Volume (gallons): {tank.volume_gallons():.2f}\n"
            f"Total Weight of Water (pounds): {tank.water_weight_pounds():.2f}\n"
            f"Top Surface Area (sq ft): {tank.top_area():.2f}\n"
            f"Outside Surface Area (sq ft): {tank.outside_area():.2f}\n"
            f"Total Paint Area (sq ft): {tank.total_paint_area():.2f}\n"
        )

        # Display results
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, results)
        self.output_text.config(state="disabled")


# ---------------------------------------------------------
# Main program launcher
# ---------------------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = TankApp(root)
    root.mainloop()
