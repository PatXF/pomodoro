from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reset = False
reps = 0
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reset
    global reps
    reset = True
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    sbutton.configure(state="active")

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reset
    global reps
    reps += 1
    if reset:
        reset = False
    if reps % 2 == 1:
        countdoUwUn(60*WORK_MIN)
    elif reps % 2 == 0:
        countdoUwUn(60*SHORT_BREAK_MIN)
    elif reps % 8 == 0:
        countdoUwUn(60*LONG_BREAK_MIN)
    sbutton.configure(state=DISABLED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdoUwUn(count):
    global reset
    sec = count % 60
    minu = int((count - count % 60) / 60)
    if reset:
        count = -2
    if count > 0:
        window.after(1000, countdoUwUn, count - 1)
        if sec >= 10:
            if minu >= 10:
                canvas.itemconfig(timer_text, text=f"{minu}:{sec}")
            else:
                canvas.itemconfig(timer_text, text=f"0{minu}:{sec}")
        else:
            if minu >= 10:
                canvas.itemconfig(timer_text, text=f"{minu}:0{sec}")
            else:
                canvas.itemconfig(timer_text, text=f"0{minu}:0{sec}")
    elif count == 0:
        window.after(1000, countdoUwUn, count - 1)
        canvas.itemconfig(timer_text, text=f"0{minu}:0{sec}")
    elif count == -1:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
timer_label = Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, highlightthickness=0, bg=YELLOW)
rbutton = Button(text="reset", width=10, command=reset_timer)
sbutton = Button(text="start", width=10, command=start_timer)
rbutton.grid(row=2, column=0)
sbutton.grid(row=2, column=2)
check = Label(text="✓", fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 10, "bold"))
check.grid(row=2, column=1)
timer_label.grid(row=0, column=1)
canvas = Canvas(width=250, height=250, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(125, 125, image=tomato)
timer_text = canvas.create_text(125, 140, text="00:00", fill=YELLOW, font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

window.mainloop()

