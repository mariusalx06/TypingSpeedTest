import tkinter as tk
import random
import time

words = ["member","coat","nut","quote","stir","alcohol","conflict","pie","forestry","technology","mercy","staff","practice","timetable","battle","course","dictionary","episode","facade","conscience","quit","rage","colorful","explode","humor","pull","run","issue","profession","ratio","suppress","liver","bake","dinner","job","trait","year","exemption","screen","weed","finished","graze","elite","recovery","dynamic","terminal","presentation","advice","relate","exempt"]

window = tk.Tk()
window.title("Typing Speed Test")
window.geometry("450x250")

word_list = random.sample(words, len(words))
current_word_index = 0
start_time = None
score = 0
timer_running = False

def start_test(event):
    global start_time, timer_running
    if start_time is None:
        start_time = time.time()
        timer_running = True
        update_timer()

def update_timer():
    if timer_running:
        elapsed_time = time.time() - start_time
        remaining_time = 60 - int(elapsed_time)

        if remaining_time > 0:
            timer_label.config(text=f"Time left: {remaining_time} seconds")
            window.after(1000, update_timer)
        else:
            end_test()

def check_typing(event):
    global current_word_index, score
    typed_word = entry.get().strip()
    entry.delete(0, tk.END)

    if typed_word == word_list[current_word_index]:
        score += 1
        current_word_index += 1

        if current_word_index < len(word_list):
            word_label.config(text=word_list[current_word_index])
        else:
            result_label.config(text="You've typed all the words!")
    else:
        result_label.config(text="Incorrect. Try the next word.")


def end_test():
    global timer_running
    timer_running = False
    result_label.config(text=f"Test completed! Your score: {score} correct words.")
    entry.config(state='disabled')


label = tk.Label(window, text="Type the following words:")
label.pack(pady=10)

word_label = tk.Label(window, text=word_list[current_word_index], font=('Helvetica', 12))
word_label.pack(pady=10)

entry = tk.Entry(window, width=20)
entry.pack(pady=10)
entry.bind("<FocusIn>", start_test)
entry.bind("<Return>", check_typing)

timer_label = tk.Label(window, text="Time left: 60 seconds")
timer_label.pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

window.mainloop()