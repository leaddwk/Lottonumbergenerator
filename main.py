import tkinter as tk
import random

root = tk.Tk()


def randum():
    b = []
    for i in range(6):
        b.append(random.randint(1, 46))
    a = tk.Label(root, text=f"{b[0]} {b[1]} {b[2]} {b[3]} {b[4]} {b[5]}")
    a.pack()


d = tk.Button(root, text="번호 추첨", command=randum)
d.pack()

root.mainloop()
