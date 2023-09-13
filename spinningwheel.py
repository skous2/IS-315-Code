import tkinter as tk
import random
import time

# Define the prizes
prizes = ["Prize 1", "Prize 2", "Prize 3", "Prize 4", "Prize 5"]

# Function to spin the wheel
def spin_wheel():
    spin_button.config(state=tk.DISABLED)  # Disable the spin button during spinning
    for _ in range(10):
        random_prize = random.choice(prizes)
        wheel_label.config(text=random_prize)
        root.update()
        time.sleep(.1)  # Adjust the sleep duration to control the spinning speed
    spin_button.config(state=tk.NORMAL)  # Re-enable the spin button after spinning

# Create the main window
root = tk.Tk()
root.title("Spinning Wheel")

# Create a label for the wheel
wheel_label = tk.Label(root, text="", font=("Helvetica", 16))
wheel_label.pack(pady=20)

# Create a spin button
spin_button = tk.Button(root, text="Spin the Wheel", command=spin_wheel)
spin_button.pack()

# Start the GUI main loop
root.mainloop()
