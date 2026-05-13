# GNOME-style Pomodoro Timer for Windows
# Features: Work session + Short break, GNOME-like UI feel
# Python 3.x

import tkinter as tk
from tkinter import ttk

WORK_TIME = 25 * 60
SHORT_BREAK = 5 * 60

class PomodoroApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pomodoro")
        self.geometry("420x320")
        self.resizable(False, False)

        # GNOME-like colors
        self.bg_color = "#f6f5f4"
        self.header_color = "#2e3436"
        self.accent_color = "#e01b24"
        self.text_color = "#2e3436"

        self.configure(bg=self.bg_color)

        # Fonts (Cantarell if available, fallback otherwise)
        self.font_title = ("Cantarell", 14)
        self.font_timer = ("Cantarell", 48, "bold")
        self.font_button = ("Cantarell", 12)

        self.time_left = WORK_TIME
        self.running = False
        self.mode = "Work Session"

        self.create_ui()
        self.update_display()

    def create_ui(self):
        header = tk.Frame(self, bg=self.header_color, height=48)
        header.pack(fill="x")

        title = tk.Label(header, text="Pomodoro", fg="white",
                         bg=self.header_color, font=self.font_title)
        title.pack(pady=10)

        self.mode_label = tk.Label(self, text=self.mode,
                                   bg=self.bg_color,
                                   fg=self.text_color,
                                   font=("Cantarell", 16))
        self.mode_label.pack(pady=(30, 10))

        self.timer_label = tk.Label(self, text="00:00",
                                    bg=self.bg_color,
                                    fg=self.text_color,
                                    font=self.font_timer)
        self.timer_label.pack(pady=10)

        self.start_button = tk.Button(self, text="Start",
                                      font=self.font_button,
                                      command=self.toggle_timer,
                                      relief="groove")
        self.start_button.pack(pady=(20, 8))

        self.switch_button = tk.Button(self, text="Switch to Break",
                                       font=self.font_button,
                                       command=self.switch_mode,
                                       relief="groove")
        self.switch_button.pack()

    def toggle_timer(self):
        self.running = not self.running
        self.start_button.config(text="Pause" if self.running else "Start")
        if self.running:
            self.countdown()

    def switch_mode(self):
        self.running = False
        self.start_button.config(text="Start")
        if self.mode == "Work Session":
            self.mode = "Short Break"
            self.time_left = SHORT_BREAK
            self.switch_button.config(text="Switch to Work")
        else:
            self.mode = "Work Session"
            self.time_left = WORK_TIME
            self.switch_button.config(text="Switch to Break")

        self.mode_label.config(text=self.mode)
        self.update_display()

    def countdown(self):
        if self.running and self.time_left > 0:
            self.time_left -= 1
            self.update_display()
            self.after(1000, self.countdown)
        elif self.time_left == 0:
            self.running = False
            self.start_button.config(text="Start")

    def update_display(self):
        minutes = self.time_left // 60
        seconds = self.time_left % 60
        self.timer_label.config(text=f"{minutes:02d}:{seconds:02d}")


if __name__ == "__main__":
    app = PomodoroApp()
    app.mainloop()
