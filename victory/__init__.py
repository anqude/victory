from argparse import Namespace

import tkinter as tk
from tkinter import Pack, filedialog
from tkinter import messagebox
from tkinter import ttk

import random

class App:
    def __init__(self, args:Namespace) -> None:
        self.args = args
        self.root = root = tk.Tk()
        self.get_file()
        self.get_questions_count()
        self.qu = None
        self.state = 0
        self.root.title("Victory")
        self.childs = []

    def end(self):
        if self.ent.get() == self.q[self.qc-1][1]:
            self.state += 1
        else:
            self.state -= 1
        self.lb.destroy()
        self.ent.destroy()
        self.btn.destroy()

        tk.Label(text=f"Ваш результат: {self.state}").pack(anchor="nw")
        tk.Label(text=f"Правильные ответы: ").pack(anchor="center")
        for i in self.q:
            tk.Label(text=f"{i[0]}: {i[1]}").pack(anchor="nw")
        

    def next_q(self, n):
        if self.qu:
            if self.ent.get() == self.q[n-1][1]:
                self.state += 1
            else:
                self.state -= 0
        try:
            self.lb.destroy()
            self.ent.destroy()
            self.btn.destroy()
        except:
            ...
        self.qu = self.q[n]
        self.lb = tk.Label(text=self.qu[0])
        self.lb.pack()
        self.ent = tk.Entry()
        self.ent.pack()
        self.btn = tk.Button(text="Ответить", command=lambda: self.next_q(n+1) if n+2 <= len(self.q) else self.end())
        self.btn.pack()
    
    def start(self):
        self.next_q(0)
            

    def get_questions(self):
        try:
            with open(self.victory_file, "r") as file:
                    txt = file.read().split("\n")
                    self.qc = min(self.qc, len(txt))
                    random.shuffle(txt)
            
            q = txt[:self.qc]
            self.q = list(map(lambda qu: qu.split("|"), q))
            
        except:
                messagebox.showerror("Неправильный формат файла")

        self.start()

    def get_count(self):
        self.qc = int(self.count.get())
        self.quest.destroy()
        self.count.destroy()
        self.ok.destroy()
        self.get_questions()

    def get_questions_count(self):
        if not self.args.count:
            self.quest = tk.Label(text="Сколько вопросов?")
            self.count = ttk.Spinbox(from_=1, to=100)
            self.ok = tk.Button(text="Enter", command=self.get_count)
            self.quest.pack()
            self.count.pack()
            self.ok.pack()
        else:
            self.qc = self.args.count

    def get_file(self):
        if not self.args.file:
            file = filedialog.askopenfile()
            if file:
                self.victory_file = file.name
                file.close()
            else:
                messagebox.showerror("Нет Файла", "Файл не выбран")
                exit(1)
        else:
            self.file = self.args.file
        


    def run(self):
        self.root.mainloop()