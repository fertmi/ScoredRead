import tkinter as tk
from text import book as bk
import random
from time import time

def text_book(book):
    txt_book = []
    book = book.split()
    br = 0
    start = random.randint(0,1700)
    for i in range(start, start+20):
        txt_book.append(book[i])
        if len(book[i])>2:
            br += 1
        if br == 10: break
    return txt_book

def key_handler_function(event):
    import difflib
    stop = time()
    human_txt = answer_entry.get()
    time_human = round(stop - start, 2)
    ratio_human = round(difflib.SequenceMatcher(None, random_txt, human_txt).ratio() * 100, 0)
    answer_entry.config(state = 'disabled')
    text2.config(text=f'Вы набрали текст за время {time_human} секунд, с точностью {ratio_human}%')

def start_game():
    global start
    global random_txt
    answer_entry.config(state='normal')
    answer_entry.delete(0, 'end')
    text2.config(text="Здесь будет результат")
    start = 0
    answer_entry.focus_set()
    start = time()
    random_txt = ' '.join(text_book(bk))
    text1.config(text=random_txt)

window = tk.Tk()
window.title('Повтори текст')
window.geometry("700x150")
window.resizable(False, False)
button_add = tk.Button(window, text="Старт", width=10, height=2, command=start_game)
button_add.place(x=100, y=60)
text1 = tk.Label(window, text="Здесь будет текст, который надо повторить")
text1.place(x=50, y=30)
text2 = tk.Label(window, text="Здесь будет результат")
text2.place(x=50, y=7)
answer_entry = tk.Entry(window, width=90)
answer_entry.place(x=50, y=125)
answer = tk.Label(window, text="Проверьте Ru/En, после старта повторите с точностью текст и нажмите Enter:")
answer.place(x=50, y=100)
human_txt = answer_entry.bind('<Return>', key_handler_function)
window.mainloop()