import tkinter as tk
from captcha.image import ImageCaptcha
from PIL import Image, ImageTk
import random

class MathCaptcha:
    def __init__(self):
        # Initialize Window
        self.root = tk.Tk()
        self.root.title("Advanced Math CAPTCHA")
        self.root.geometry("400x350")
        self.root.configure(bg="#282c34")  # Default Dark Theme

        self.timer_running = False  # Timer Flag
        self.time_left = 30  # Countdown Timer

        # Header Label
        self.title_label = tk.Label(self.root, text="🔢 Math CAPTCHA", font=("Arial", 16, "bold"), fg="white", bg="#282c34")
        self.title_label.pack(pady=10)

        # CAPTCHA Image Display
        self.captcha_label = tk.Label(self.root, bg="#282c34")
        self.captcha_label.pack()

        # Input Field
        self.entry_var = tk.StringVar()
        self.captcha_input = tk.Entry(self.root, textvariable=self.entry_var, font=("Arial", 14))
        self.captcha_input.pack(pady=5)

        # Buttons (Submit & Refresh)
        self.button_frame = tk.Frame(self.root, bg="#282c34")
        self.button_frame.pack(pady=10)

        self.submit_btn = tk.Button(self.button_frame, text="✅ Submit", command=self.submit, bg="#4caf50", fg="white", font=("Arial", 12, "bold"))
        self.submit_btn.pack(side=tk.LEFT, padx=5)

        self.refresh_btn = tk.Button(self.button_frame, text="🔄 Refresh", command=self.refresh_captcha, bg="#ff9800", fg="white", font=("Arial", 12, "bold"))
        self.refresh_btn.pack(side=tk.LEFT, padx=5)

        # Theme Toggle Button
        self.theme_btn = tk.Button(self.root, text="🌙 Switch Theme", command=self.toggle_theme, bg="#607d8b", fg="white", font=("Arial", 10, "bold"))
        self.theme_btn.pack(pady=5)

        # Timer Label
        self.timer_label = tk.Label(self.root, text="Time left: 30s", font=("Arial", 10, "bold"), fg="white", bg="#282c34")
        self.timer_label.pack()

        self.dark_mode = True  # Default Theme
        self.message_label = None  # Initialize message_label as None

        # Generate Initial CAPTCHA & Start Timer
        self.generate_captcha()
        self.start_timer()

        self.root.mainloop()

    def generate_captcha(self):
        """Generates a new CAPTCHA and updates the display."""
        self.actual = str(random.randint(1, 9)) + self.randOps() + str(random.randint(1, 9))
        print("Generated CAPTCHA:", self.actual)

        # Generate CAPTCHA image
        image = ImageCaptcha()
        image.write(self.actual, "out.png")

        # Update Image in UI
        self.photo = ImageTk.PhotoImage(file="out.png")
        self.captcha_label.config(image=self.photo)

        # Clear input field
        self.entry_var.set("")

    def refresh_captcha(self):
        """Refreshes the CAPTCHA and resets the timer properly."""
        self.generate_captcha()  # Generate new CAPTCHA
        self.reset_timer()  # Reset Timer

    def randOps(self):
        """Returns a random math operator."""
        return random.choice(["+", "-", "*", "/"])

    def submit(self):
        """Validates user input against the correct CAPTCHA answer."""
        try:
            user_input = self.entry_var.get()
            correct_answer = eval(self.actual)  # Evaluate Math Expression

            if float(user_input) == correct_answer:
                self.result_message("✅ Correct! Generating new CAPTCHA...", "green")
                self.refresh_captcha()  # Generate new CAPTCHA on success
            else:
                self.result_message("❌ Incorrect! Try Again.", "red")

        except Exception:
            self.result_message("⚠️ Invalid Input!", "red")

    def result_message(self, message, color):
        """Displays a temporary message below the input field."""
        if self.message_label:
            self.message_label.destroy()  # Remove old message before showing new
        
        self.message_label = tk.Label(self.root, text=message, fg=color, font=("Arial", 10, "bold"), bg=self.root.cget("bg"))
        self.message_label.pack()
        self.root.after(2000, self.message_label.destroy)  # Auto-remove message

    def update_timer(self):
        """Handles the countdown timer for CAPTCHA."""
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time left: {self.time_left}s")
            self.root.after(1000, self.update_timer)
        else:
            self.timer_running = False  # Stop the timer
            self.result_message("⏳ Time's up! Refreshing CAPTCHA.", "orange")
            self.refresh_captcha()  # Reset CAPTCHA

    def start_timer(self):
        """Starts the CAPTCHA countdown timer."""
        if not self.timer_running:
            self.timer_running = True
            self.time_left = 30  # Ensure Timer Starts from 30
            self.update_timer()

    def reset_timer(self):
        """Resets the timer when CAPTCHA is refreshed."""
        self.time_left = 30
        self.timer_label.config(text=f"Time left: {self.time_left}s")
        if not self.timer_running:
            self.start_timer()

    def toggle_theme(self):
        """Toggles between dark and light themes."""
        if self.dark_mode:
            new_bg, new_fg, btn_bg, btn_fg = "white", "black", "#ccc", "black"
            self.theme_btn.config(text="☀️ Light Mode")
        else:
            new_bg, new_fg, btn_bg, btn_fg = "#282c34", "white", "#607d8b", "white"
            self.theme_btn.config(text="🌙 Dark Mode")

        self.root.configure(bg=new_bg)
        self.title_label.config(bg=new_bg, fg=new_fg)
        self.captcha_label.config(bg=new_bg)
        self.timer_label.config(bg=new_bg, fg=new_fg)
        self.theme_btn.config(bg=btn_bg, fg=btn_fg)

        if self.message_label and self.message_label.winfo_exists():
            self.message_label.config(bg=new_bg)  # Only update if it exists

        self.dark_mode = not self.dark_mode  # Toggle mode flag

# Run Application
MathCaptcha()