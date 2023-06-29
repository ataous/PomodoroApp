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
SECOND_IN_MINUTE = 60

timer = ""
reps = 0
big_marks = ""
small_marks = ""


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global timer, reps, big_marks, small_marks
    window.after_cancel(timer)
    reps = 0
    big_marks = ""
    small_marks = ""

    canvas.itemconfig(timer_text, text="00:00")
    lbl_checkmark.config(text="")
    lbl_title.config(text="Let's Start", fg=GREEN)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps, big_marks, small_marks
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * SECOND_IN_MINUTE)
        lbl_title.config(text="Long Break", fg=RED)
        big_marks += "✅"
        lbl_checkmark.config(text=big_marks)
        small_marks = ""
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * SECOND_IN_MINUTE)
        lbl_title.config(text="Short Break", fg=PINK)
        small_marks += "✓"
        lbl_checkmark.config(text=big_marks + small_marks)
    else:
        count_down(WORK_MIN * SECOND_IN_MINUTE)
        lbl_title.config(text="Working Now", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    second = round(count % 60)
    minute = round((count - second) / 60)

    minute = str(minute) if minute > 9 else f"0{minute}"
    second = str(second) if second > 9 else f"0{second}"

    canvas.itemconfig(timer_text, text=f"{minute}:{second}")
    if count == 0:
        start_timer()
    else:
        global timer
        timer = window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

lbl_title = Label(text="Let's Start", width=12, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
lbl_title.grid(column=1, row=0)

lbl_checkmark = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 12, "bold"))
lbl_checkmark.grid(column=1, row=3)

btn_start = Button(text="Start", bg=GREEN, font=(FONT_NAME, 10, "bold"), width=9, relief="flat", command=start_timer)
btn_start.grid(column=0, row=2)

btn_reset = Button(text="Reset", bg=GREEN, font=(FONT_NAME, 10, "bold"), width=9, relief="flat", command=reset)
btn_reset.grid(column=3, row=2)

window.mainloop()
