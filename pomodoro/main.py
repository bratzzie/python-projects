import math
import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- GLOBALS ------------------------------- #
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_session():
    global reps
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    session_amount_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_session():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    remaining_min = math.floor(count / 60)
    remaining_sec = count % 60

    if remaining_sec < 10:
        remaining_sec = f"0{remaining_sec}"

    canvas.itemconfig(timer_text, text=f"{remaining_min}:{remaining_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_session()
        if reps % 2 == 0:
            check_marks = ""
            for _ in range(math.floor(reps / 2)):
                check_marks += "✔️"
            session_amount_label.config(text=check_marks)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = tk.Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

background_image = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=background_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = tk.Button(text="Start", command=start_session, highlightthickness=0)
start_button.grid(column=0, row=2)
reset_button = tk.Button(text="Reset", command=reset_session, highlightthickness=0)
reset_button.grid(column=2, row=2)

session_amount_label = tk.Label(text="", fg=GREEN, bg=YELLOW)
session_amount_label.grid(column=1, row=3)

window.mainloop()
