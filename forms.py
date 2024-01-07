import tkinter as tk
from tkinter import ttk
from typing import List, Optional, Tuple, Callable
import functools
from models import *
from exeptions import InputError, InputPar
import hashlib

class Forms(tk.Frame):
    win = None
    but = None
    entry = None
    entry1 = None
    label1 = None
    label = None
    login = 0
    parol = 0
    btn_submit = None
    frm_form = None
    frm_buttons = None
    butt = []
    label3 = [
        "Дата:",
        "Время:",
        "Кабинет:",
        "Врач:"
    ]

    label_r = [
        "Полис пациента:",
        "Дата:",
        "Время:",
        "Кабинет:",
        "Врач:"
    ]

    dict_r = {
        "Полис пациента:":"",
        "Дата:": "",
        "Время:": "",
        "Кабинет:": "",
        "Врач:": ""
    }

    label_d = [
        "Время:",
        "Дни недели:",
        "Кабинет:"
    ]

    dict3 = {
        "Дата:": "",
        "Время:": "",
        "Кабинет:": "",
        "Врач:": ""
    }

    label4 = [
        "Дата:",
        "Время:",
        "Врач:",
        "Кабинет:",
    ]
    label5 = [
        "Дата:",
        "Рекомендации и назначенные лекарства:",
    ]
    dict5 = {
        "Дата:": '',
        "Рекомендации и назначенные лекарства:": '',
    }

    label_s = [
        "Код специальности:",
        "Название:",
    ]
    dict_s = {
        "Код специальности:": '',
        "Название:": '',
    }

    label7 = [
        "Врач:",
        "Дата:",
        "Рекомендации и назначенные лекарства:",
    ]
    labelp = ["Полис пациента:"]
    dictp = {"Полис пациента:": ""}
    label2 = [
        "Фамилия:",
        "Имя:",
        "Отчество:",
        "Адрес:",
        "Телефон:",
        "Пароль:",
        "Полис:",
    ]
    dict2 = {
        "Фамилия:": "",
        "Имя:": "",
        "Отчество:": "",
        "Адрес:": "",
        "Телефон:": "",
        "Пароль:": "",
        "Полис:": "",
    }

    label22 = [
        "Фамилия:",
        "Имя:",
        "Отчество:",
        "Адрес:",
        "Телефон:",
        "Полис:",
    ]
    dict22 = {
        "Фамилия:": "",
        "Имя:": "",
        "Отчество:": "",
        "Адрес:": "",
        "Телефон:": "",
        "Полис:": "",
    }

    labeld = [
        "Фамилия:",
        "Имя:",
        "Отчество:",
        "Адрес:",
        "Телефон:",
        "Пароль:",
        "Полис:",
        "Код специальности:"
    ]
    dictd = {
        "Имя:": "",
        "Фамилия:": "",
        "Отчество:": "",
        "Адрес:": "",
        "Телефон:": "",
        "Пароль:": "",
        "Полис:": "",
        "Код специальности:": "",
    }

    labels = [
        "Дата:",
        "Диагноз:",
        "Заключение:",
    ]
    dicts = {
        "День:": "",
        "Диагноз:": "",
        "Заключение:": "",
    }

    label_sc = [
        "Доктор:",
        "День:",
        "Начало работы:",
        "Конец работы:",
        "Кабинет:",

    ]
    dict_sc = {
        "Доктор:": "",
        "День:": "",
        "Начало работы:": "",
        "Конец работы:": "",
        "Кабинет:": "",
    }

    entrybut = []
    label6 = []
    """Главный экран графического приложения"""
    def __init__(self, root):
        super().__init__(root)
        self.__root = root
        self.tree: Optional[ttk.Treeview] = None

    def rgb_hack(self, rgb):
        return "#%02x%02x%02x" % rgb

    def close(self, event):
        for i, k in enumerate(self.label6):
            self.label6[i].destroy()
        for i, k in enumerate(self.entrybut):
            self.entrybut[i].destroy()
        if self.btn_submit != None:
            self.btn_submit.destroy()
        self.label6.clear()
        self.entrybut.clear()
        self.frm_form.destroy()
        if self.frm_buttons != None:
            self.frm_buttons.destroy()

    def exit_(self, event):
        self.win.destroy()

    def clear(self, event):
        for idx, text in enumerate(self.entrybut):
            self.entrybut[idx].delete(0, tk.END)

#############################################doctor
    def send_talon(self, event, pat):
        try:
            for idx, text in enumerate(self.label3):
                if self.entrybut[idx].get() != '':
                    self.dict3[text] = self.entrybut[idx].get()
                    print(self.dict3[text])
                else:
                    raise InputError("Invalid input", "Check the input fields!")
            create_talon(pat, self.dict3['Дата:'], self.dict3['Время:'], self.dict3['Кабинет:'], self.dict3['Врач:'])
            self.entrybut.clear()
            self.frm_form.destroy()
            self.frm_buttons.destroy()
        except InputError as e:
            e.subscribe()

    def add_talon(self, event, pat):
        self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=20, bg=self.rgb_hack((0, 159, 166)))
        self.frm_form.grid(row=8)
        for idx, text in enumerate(self.label3):
            # Создает ярлык с текстом из списка ярлыков.
            label = tk.Label(master=self.frm_form, text=text, bg=self.rgb_hack((0, 159, 166)))
            # Создает текстовое поле которая соответствует ярлыку.
            entry = tk.Entry(master=self.frm_form, width=50)
            self.entrybut.append(tk.Entry(master=self.frm_form, width=50, bg=self.rgb_hack((187, 255, 255))))
            # Использует менеджер геометрии grid для размещения ярлыков и
            # текстовых полей в строку, чей индекс равен idx.
            label.grid(row=idx, column=0, sticky="e")
            entry.grid(row=idx, column=1)
            self.entrybut[idx].grid(row=idx, column=1)
        self.frm_buttons = tk.Frame(borderwidth=3, bg=self.rgb_hack((0, 159, 166)))
        self.frm_buttons.grid(row=9, column=0, ipadx=5, ipady=5)

        btn_submit = tk.Button(master=self.frm_buttons, text="Отправить", bg=self.rgb_hack((187, 255, 255)))
        btn_submit.bind("<Button-1>", functools.partial(self.send_talon, pat=pat))
        btn_submit.grid(row=8, column=0, padx=10, ipadx=10)

        btn_clear = tk.Button(master=self.frm_buttons, text="Очистить", bg=self.rgb_hack((187, 255, 255)))
        btn_clear.bind("<Button-1>", self.clear)
        btn_clear.grid(row=8, column=1, ipadx=10)

    def add_receipt(self, event, pat, doc):
        self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=20, bg=self.rgb_hack((0, 159, 166)))
        self.frm_form.grid(row=8)
        for idx, text in enumerate(self.label5):
            # Создает ярлык с текстом из списка ярлыков.
            label = tk.Label(master=self.frm_form, text=text, bg=self.rgb_hack((0, 159, 166)))
            # Создает текстовое поле которая соответствует ярлыку.
            entry = tk.Entry(master=self.frm_form, width=50)
            self.entrybut.append(tk.Entry(master=self.frm_form, width=50, bg=self.rgb_hack((187, 255, 255))))
            # Использует менеджер геометрии grid для размещения ярлыков и
            # текстовых полей в строку, чей индекс равен idx.
            label.grid(row=idx, column=0, sticky="e")
            entry.grid(row=idx, column=1)
            self.entrybut[idx].grid(row=idx, column=1)
        self.frm_buttons = tk.Frame(borderwidth=3, bg=self.rgb_hack((0, 159, 166)))
        self.frm_buttons.grid(row=9, column=0, ipadx=5, ipady=5)

        btn_submit = tk.Button(master=self.frm_buttons, text="Отправить", bg=self.rgb_hack((187, 255, 255)))
        btn_submit.bind("<Button-1>", functools.partial(self.send_receipt, pat=pat, doc=doc))
        btn_submit.grid(row=8, column=0, padx=10, ipadx=10)

        btn_clear = tk.Button(master=self.frm_buttons, text="Очистить", bg=self.rgb_hack((187, 255, 255)))
        btn_clear.bind("<Button-1>", self.clear)
        btn_clear.grid(row=8, column=1, ipadx=10)

    def send_receipt(self, event, pat, doc):
        try:
            for idx, text in enumerate(self.label5):
                if self.entrybut[idx].get() != '':
                    self.dict5[text] = self.entrybut[idx].get()
                    print(self.dict5[text])
                else:
                    raise InputError("Invalid input", "Check the input fields!")
            create_receipt(pat, doc, self.dict5['Рекомендации и назначенные лекарства:'], self.dict5['Дата:'])
            self.entrybut.clear()
            self.frm_form.destroy()
            self.frm_buttons.destroy()
        except InputError as e:
            e.subscribe()

    def send_seek_hisory(self, event, doc, pat):
        try:
            for idx, text in enumerate(self.labels):
                if self.entrybut[idx].get() != '':
                    self.dicts[text] = self.entrybut[idx].get()
                    print(self.dicts[text])
                else:
                    raise InputError("Invalid input", "Check the input fields!")
            create_seek_history(pat, doc, self.dicts['Диагноз:'], self.dicts['Дата:'], self.dicts['Заключение:'])
            self.entrybut.clear()
            self.frm_form.destroy()
            self.frm_buttons.destroy()
        except InputError as e:
            e.subscribe()

    def seek_history(self, event, doc, pat):
        self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=20, bg=self.rgb_hack((0, 159, 166)))
        self.frm_form.grid(row=8)
        for idx, text in enumerate(self.labels):
            # Создает ярлык с текстом из списка ярлыков.
            label = tk.Label(master=self.frm_form, text=text, bg=self.rgb_hack((0, 159, 166)))
            # Создает текстовое поле которая соответствует ярлыку.
            entry = tk.Entry(master=self.frm_form, width=50)
            self.entrybut.append(tk.Entry(master=self.frm_form, width=50, bg=self.rgb_hack((187, 255, 255))))
            # Использует менеджер геометрии grid для размещения ярлыков и
            # текстовых полей в строку, чей индекс равен idx.
            label.grid(row=idx, column=0, sticky="e")
            entry.grid(row=idx, column=1)
            self.entrybut[idx].grid(row=idx, column=1)
        self.frm_buttons = tk.Frame(borderwidth=3, bg=self.rgb_hack((0, 159, 166)))
        self.frm_buttons.grid(row=9, column=0, ipadx=5, ipady=5)

        btn_submit = tk.Button(master=self.frm_buttons, text="Отправить", bg=self.rgb_hack((187, 255, 255)))
        btn_submit.bind("<Button-1>", functools.partial(self.send_seek_hisory, doc=doc, pat=pat))
        btn_submit.grid(row=8, column=0, padx=10, ipadx=10)

        btn_clear = tk.Button(master=self.frm_buttons, text="Очистить", bg=self.rgb_hack((187, 255, 255)))
        btn_clear.bind("<Button-1>", self.clear)
        btn_clear.grid(row=8, column=1, ipadx=10)

    def doctor(self, event, key):
        try:
            pat_id = self.entry1.get()
            if is_patient(pat_id):
                self.entry1.delete(0, tk.END)
                self.frm_form.destroy()
                self.but.destroy()
                self.entry1.destroy()
                self.label1.destroy()
                self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=20, bg=self.rgb_hack((0, 159, 166)))
                self.frm_form.grid()
                self.butt.append(tk.Button(self.frm_form, text="Посмотреть карту пациента", bg=self.rgb_hack((187, 255, 255))))
                self.butt[len(self.butt)-1].config(width=35)
                self.butt[len(self.butt)-1].bind("<Button-1>", functools.partial(self.see_patient, key=pat_id))
                self.butt[len(self.butt)-1].grid(column=1)

                self.butt.append(tk.Button(self.frm_form, text="Добавить запись в историю болезни", bg=self.rgb_hack((187, 255, 255))))
                self.butt[len(self.butt) - 1].config(width=35)
                self.butt[len(self.butt) - 1].bind("<Button-1>", functools.partial(self.seek_history, pat=pat_id, doc=key))
                self.butt[len(self.butt) - 1].grid(column=1)

                self.butt.append(tk.Button(self.frm_form, text="Выписать рецепт", bg=self.rgb_hack((187, 255, 255))))
                self.butt[len(self.butt) - 1].config(width=35)
                self.butt[len(self.butt)-1].bind("<Button-1>", functools.partial(self.add_receipt, pat=pat_id, doc=key))
                self.butt[len(self.butt)-1].grid(column=1)

                self.butt.append(tk.Button(self.frm_form, text="Выписать талон", bg=self.rgb_hack((187, 255, 255))))
                self.butt[len(self.butt) - 1].config(width=35)
                self.butt[len(self.butt)-1].bind("<Button-1>", functools.partial(self.add_talon, pat=pat_id))
                self.butt[len(self.butt)-1].grid(column=1)

                self.butt.append(tk.Button(self.frm_form, text="Выход", bg=self.rgb_hack((187, 255, 255))))
                self.butt[len(self.butt) - 1].config(width=15)
                self.butt[len(self.butt)-1].bind("<Button-1>", self.exit_)
                self.butt[len(self.butt)-1].grid(row=5, column=1)

                self.butt.append(tk.Button(self.frm_form, text="Назад", bg=self.rgb_hack((187, 255, 255))))
                self.butt[len(self.butt) - 1].config(width=15)
                self.butt[len(self.butt)-1].bind("<Button-1>", functools.partial(self.doc_back, doc=key))
                self.butt[len(self.butt)-1].grid(row=6,column=1)
            else:
                raise InputError("Invalid input", "Check the patient id!")
        except InputError as e:
            e.subscribe()

    def doc_back(self, event, doc):
        for index, t in enumerate(self.butt):
            self.butt[index].destroy()
        self.butt.clear()
        self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=20, bg=self.rgb_hack((0, 159, 166)))
        self.frm_form.grid()
        self.label1 = tk.Label(text="Полис пациента", bg=self.rgb_hack((0, 159, 166)))
        self.entry1 = tk.Entry(bg=self.rgb_hack((187, 255, 255)))
        self.label1.config(width=20)
        self.label1.grid(column=2, row=1)
        self.entry1.grid(column=2, row=2)
        self.but = tk.Button(self.win, text="Ok", bg=self.rgb_hack((187, 255, 255)))
        self.but.bind("<Button-1>", functools.partial(self.doctor, key=doc))
        self.but.grid(column=2, row=3)
        self.but.pack()

    def doctor1(self, key):
        self.win = tk.Tk()
        self.win.title("Главная Доктора")
        self.win.config(bg=self.rgb_hack((0, 159, 166)))
        self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=20, bg=self.rgb_hack((0, 159, 166)))
        self.frm_form.grid()
        self.label1 = tk.Label(text="Полис пациента", bg=self.rgb_hack((0, 159, 166)))
        self.entry1 = tk.Entry(bg=self.rgb_hack((187, 255, 255)))
        self.label1.config(width=20)
        self.label1.grid(column=2, row=1)
        self.entry1.grid(column=2, row=2)
        self.but = tk.Button(self.win, text="Ok", bg=self.rgb_hack((187, 255, 255)))
        self.but.bind("<Button-1>", functools.partial(self.doctor, key=key))
        self.but.grid(column=2, row=3)
        self.win.mainloop()
######################################################

##############################################patient

    def op_talon(self, event, day, time, pat):
        for i, k in enumerate(self.butt):
            self.butt[i].destroy()
        self.frm_buttons.destroy()
        self.frm_form.destroy()
        self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=20, bg=self.rgb_hack((0, 159, 166)))
        self.frm_form.grid()
        for idx, text in enumerate(self.label4):
            self.label6.append(tk.Label(master=self.frm_form, text=text, bg=self.rgb_hack((0, 159, 166))))
            self.entrybut.append(tk.Entry(master=self.frm_form, width=50, bg=self.rgb_hack((187, 255, 255))))
            self.label6[idx].grid(row=idx, column=0, sticky="e")
            self.entrybut[idx].grid(row=idx, column=1)
        pat = find_talon(pat, day, time)
        for idx, text in enumerate(self.label4):
            self.entrybut[idx].insert(0, pat[0][text])
        self.frm_buttons = tk.Frame(borderwidth=3, bg=self.rgb_hack((0, 159, 166)))
        self.frm_buttons.grid(ipadx=5, ipady=5)
        self.btn_submit = tk.Button(master=self.frm_buttons, text="Закрыть", bg=self.rgb_hack((187, 255, 255)))
        self.btn_submit.bind("<Button-1>", self.close)
        self.btn_submit.grid(padx=10, ipadx=10)

    def choose_time(self, event, day, pat):
        print(day)
        for i, k in enumerate(self.butt):
            self.butt[i].destroy()
        self.frm_buttons.destroy()
        self.frm_form.destroy()
        self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
        self.frm_form.pack()
        self.frm_buttons = tk.Frame()
        self.frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)
        pat = find_time(pat, day)
        for c, d in enumerate(pat):
            print(c)
            print(d)
            self.butt.append(tk.Frame())
            self.butt[c] = tk.Button(master=self.frm_buttons, text=d)
            self.butt[c].bind("<Button-1>", functools.partial(self.op_talon, day=day, time=d, pat=pat))
            self.butt[c].pack(side=tk.BOTTOM, ipadx=5, ipady=5)

    def op_receipt(self, event, day, key):
        for i, k in enumerate(self.butt):
            self.butt[i].destroy()
        self.frm_buttons.destroy()
        self.frm_form.destroy()
        self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=20, bg=self.rgb_hack((0, 159, 166)))
        self.frm_form.grid()
        for idx, text in enumerate(self.label7):
            self.label6.append(tk.Label(master=self.frm_form, text=text, bg=self.rgb_hack((0, 159, 166))))
            self.entrybut.append(tk.Entry(master=self.frm_form, width=50, bg=self.rgb_hack((187, 255, 255))))
            self.label6[idx].grid(row=idx, column=0, sticky="e")
            self.entrybut[idx].grid(row=idx, column=1)
        pat = find_receipt(key, day)
        for idx, text in enumerate(self.label7):
            self.entrybut[idx].insert(0, pat[0][text])
        self.frm_buttons = tk.Frame(borderwidth=3, bg=self.rgb_hack((0, 159, 166)))
        self.frm_buttons.grid(ipadx=5, ipady=5)
        self.btn_submit = tk.Button(master=self.frm_buttons, text="Закрыть", bg=self.rgb_hack((187, 255, 255)))
        self.btn_submit.bind("<Button-1>", self.close)
        self.btn_submit.grid(padx=10, ipadx=10)

    def see_schedule(self, event):
        self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=5, bg=self.rgb_hack((0, 159, 166)))
        self.frm_form.grid()
        pat = get_all_doc()
        print(pat)
        self.frm_buttons = tk.Frame(borderwidth=3, bg=self.rgb_hack((0, 159, 166)))
        self.frm_buttons.grid(ipadx=5, ipady=5)
        for c, d in enumerate(pat):
            print(c)
            print(d)
            self.butt.append(tk.Frame(borderwidth=3, bg=self.rgb_hack((0, 159, 166))))
            self.butt[c] = tk.Button(master=self.frm_buttons, text=d, bg=self.rgb_hack((187, 255, 255)))
            self.butt[c].bind("<Button-1>", functools.partial(self.see_schedule_doc, doc=d[0]))
            self.butt[c].config(width=20)
            self.butt[c].grid(row=c)

    def see_schedule_doc(self, event, doc):
        for i, k in enumerate(self.butt):
            self.butt[i].destroy()
        self.frm_buttons.destroy()
        self.frm_form.destroy()
        self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=20, bg=self.rgb_hack((0, 159, 166)))
        self.frm_form.grid()
        for idx, text in enumerate(self.label_d):
            self.label6.append(tk.Label(master=self.frm_form, text=text, bg=self.rgb_hack((0, 159, 166))))
            self.entrybut.append(tk.Entry(master=self.frm_form, width=50, bg=self.rgb_hack((187, 255, 255))))
            self.label6[idx].grid(row=idx, column=0, sticky="e")
            self.entrybut[idx].grid(row=idx, column=1)
        pat = get_schedule(doc)
        for idx, text in enumerate(self.label_d):
            self.entrybut[idx].insert(0, pat[0][text])
        self.frm_buttons = tk.Frame(borderwidth=3, bg=self.rgb_hack((0, 159, 166)))
        self.frm_buttons.grid(ipadx=5, ipady=5)
        self.btn_submit = tk.Button(master=self.frm_buttons, text="Закрыть", bg=self.rgb_hack((187, 255, 255)))
        self.btn_submit.bind("<Button-1>", self.close)
        self.btn_submit.grid(padx=10, ipadx=10)

    def see_talon(self, event, key):
        self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=5, bg=self.rgb_hack((0, 159, 166)))
        self.frm_form.grid()
        pat = find_date(key)
        print(pat)
        self.frm_buttons = tk.Frame(borderwidth=3, bg=self.rgb_hack((0, 159, 166)))
        self.frm_buttons.grid(ipadx=5, ipady=5)
        for c, d in enumerate(pat):
            print(c)
            print(d)
            self.butt.append(tk.Frame(borderwidth=3, bg=self.rgb_hack((0, 159, 166))))
            self.butt[c] = tk.Button(master=self.frm_buttons, text=d, bg=self.rgb_hack((187, 255, 255)))
            self.butt[c].bind("<Button-1>", functools.partial(self.op_talon, day=d, key=key))
            self.butt[c].config(width=20)
            self.butt[c].grid(row=c)

    def see_receipt(self, event, key):
        self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=5, bg=self.rgb_hack((0, 159, 166)))
        self.frm_form.grid()
        self.frm_buttons = tk.Frame(borderwidth=3, bg=self.rgb_hack((0, 159, 166)))
        self.frm_buttons.grid(ipadx=5, ipady=5)
        pat = find_date_r(key)
        for c, d in enumerate(pat):
            self.butt.append(tk.Frame(borderwidth=3, bg=self.rgb_hack((0, 159, 166))))
            self.butt[c] = tk.Button(master=self.frm_buttons, text=d, bg=self.rgb_hack((187, 255, 255)))
            self.butt[c].bind("<Button-1>", functools.partial(self.op_receipt, day=d, key=key))
            self.butt[c].config(width=20)
            self.butt[c].grid(row=c)

    def see_patient(self, event, key):
        self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=20, bg=self.rgb_hack((0, 159, 166)))
        self.frm_form.grid(row=8)
        for idx, text in enumerate(self.label22):
            # Создает ярлык с текстом из списка ярлыков.
            label = tk.Label(master=self.frm_form, text=text, bg=self.rgb_hack((0, 159, 166)))
            # Создает текстовое поле которая соответствует ярлыку.
            entry = tk.Entry(master=self.frm_form, width=50)
            self.entrybut.append(tk.Entry(master=self.frm_form, width=50, bg=self.rgb_hack((187, 255, 255))))
            # Использует менеджер геометрии grid для размещения ярлыков и
            # текстовых полей в строку, чей индекс равен idx.
            label.grid(row=idx, column=0, sticky="e")
            entry.grid(row=idx, column=1)
            self.entrybut[idx].grid(row=idx, column=1)
        self.frm_buttons = tk.Frame(borderwidth=3, bg=self.rgb_hack((0, 159, 166)))
        self.frm_buttons.grid(row=9, column=0, ipadx=5, ipady=5)
        pat = find_patient(key)
        for idx, text in enumerate(self.label22):
            self.entrybut[idx].insert(0, pat[0][text])
        btn_submit = tk.Button(master=self.frm_buttons, text="Закрыть", bg=self.rgb_hack((187, 255, 255)))
        btn_submit.bind("<Button-1>", self.close)
        btn_submit.grid(row=8, column=0, padx=10, ipadx=10)

    def op_seek_his(self, event, day, key):
        for i, k in enumerate(self.butt):
            self.butt[i].destroy()
        self.frm_buttons.destroy()
        self.frm_form.destroy()
        self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=20, bg=self.rgb_hack((0, 159, 166)))
        self.frm_form.grid()
        for idx, text in enumerate(self.labels):
            self.label6.append(tk.Label(master=self.frm_form, text=text, bg=self.rgb_hack((0, 159, 166))))
            self.entrybut.append(tk.Entry(master=self.frm_form, width=50, bg=self.rgb_hack((187, 255, 255))))
            self.label6[idx].grid(row=idx, column=0, sticky="e")
            self.entrybut[idx].grid(row=idx, column=1)
        pat = find_seek_his(key, day)
        for idx, text in enumerate(self.labels):
            self.entrybut[idx].insert(0, pat[0][text])
        self.frm_buttons = tk.Frame(borderwidth=3, bg=self.rgb_hack((0, 159, 166)))
        self.frm_buttons.grid(ipadx=5, ipady=5)
        self.btn_submit = tk.Button(master=self.frm_buttons, text="Закрыть", bg=self.rgb_hack((187, 255, 255)))
        self.btn_submit.bind("<Button-1>", self.close)
        self.btn_submit.grid(padx=10, ipadx=10)

    def see_seek_his(self, even, pat):
        self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=5, bg=self.rgb_hack((0, 159, 166)))
        self.frm_form.grid()
        self.frm_buttons = tk.Frame(borderwidth=3, bg=self.rgb_hack((0, 159, 166)))
        self.frm_buttons.grid(ipadx=5, ipady=5)
        pat = find_date_sh(pat)
        for c, d in enumerate(pat):
            self.butt.append(tk.Frame(borderwidth=3, bg=self.rgb_hack((0, 159, 166))))
            self.butt[c] = tk.Button(master=self.frm_buttons, text=d, bg=self.rgb_hack((187, 255, 255)))
            self.butt[c].bind("<Button-1>", functools.partial(self.op_seek_his, day=d, key=pat))
            self.butt[c].config(width=20)
            self.butt[c].grid(row=c)

    def patient(self, key):
        self.win = tk.Tk()
        self.win.title("Главная Пациента")
        self.win.config(bg=self.rgb_hack((0, 159, 166)))
        frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=20, bg=self.rgb_hack((0, 159, 166)))
        # Помещает рамку на окно приложения.
        frm_form.grid()
        but1 = tk.Button(frm_form, bg=self.rgb_hack((187, 255, 255)))
        but1["text"] = "Посмотреть мою карту"
        but1.config(width=35)
        but1.bind("<Button-1>", functools.partial(self.see_patient, key=key))
        but1.grid()

        but4 = tk.Button(frm_form, bg=self.rgb_hack((187, 255, 255)))
        but4["text"] = "Посмотреть рецепт"
        but4.config(width=35)
        but4.bind("<Button-1>", functools.partial(self.see_receipt, key=key))
        but4.grid()

        but2 = tk.Button(frm_form, bg=self.rgb_hack((187, 255, 255)))
        but2["text"] = "Посмотреть талон"
        but2.config(width=35)
        but2.bind("<Button-1>", functools.partial(self.see_talon, key=key))
        but2.grid()

        but6 = tk.Button(frm_form, bg=self.rgb_hack((187, 255, 255)))
        but6["text"] = "Посмотреть график работы врачей"
        but6.config(width=35)
        but6.bind("<Button-1>", functools.partial(self.see_schedule))
        but6.grid()

        but5 = tk.Button(frm_form, bg=self.rgb_hack((187, 255, 255)))
        but5["text"] = "Посмотреть историю болезни"
        but5.config(width=35)
        but5.bind("<Button-1>", functools.partial(self.see_seek_his, pat=key))
        but5.grid()

        but3 = tk.Button(frm_form, bg=self.rgb_hack((187, 255, 255)))
        but3["text"] = "Выход"
        but3.config(width=15)
        but3.bind("<Button-1>", self.exit_)
        but3.grid()
        self.win.mainloop()

##########################################################

############################################registrator
    def delete_patient(self, event):
        try:
            id = self.entry1.get()
            if is_patient(id):
                delete_patient_(self.dictp['Полис пациента:'])
                self.entrybut.clear()
                self.frm_form.destroy()
                self.frm_buttons.destroy()
            else:
                raise InputError("Invalid input", "Check polis!")
        except InputError as e:
            e.subscribe()

    def delete_talon(self, event):
        try:
            for idx, text in enumerate(self.label_r):
                if self.entrybut[idx].get() != '':
                    self.dict3[text] = self.entrybut[idx].get()
                    print(self.dict3[text])
                else:
                    raise InputError("Invalid input", "Check the input fields!")
            delete_talon(self.dict3['Полис пациента:'], self.dict3['Дата:'], self.dict3['Время:'], self.dict3['Кабинет:'], self.dict3['Врач:'])
            self.entrybut.clear()
            self.frm_form.destroy()
            self.frm_buttons.destroy()
        except InputError as e:
            e.subscribe()

    def send_talon_r(self, event):
        try:
            for idx, text in enumerate(self.label_r):
                if self.entrybut[idx].get() != '':
                    self.dict_r[text] = self.entrybut[idx].get()
                    print(self.dict_r[text])
                else:
                    raise InputError("Invalid input", "Check the input fields!")
            create_talon(self.dict_r['Полис пациента:'], self.dict_r['Дата:'], self.dict_r['Время:'], self.dict_r['Кабинет:'], self.dict_r['Врач:'])
            self.entrybut.clear()
            self.frm_form.destroy()
            self.frm_buttons.destroy()
        except InputError as e:
            e.subscribe()

    def add_talon_r(self, event):
        self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=20, bg=self.rgb_hack((0, 159, 166)))
        self.frm_form.grid(row=8)
        for idx, text in enumerate(self.label_r):
            # Создает ярлык с текстом из списка ярлыков.
            label = tk.Label(master=self.frm_form, text=text, bg=self.rgb_hack((0, 159, 166)))
            # Создает текстовое поле которая соответствует ярлыку.
            entry = tk.Entry(master=self.frm_form, width=50)
            self.entrybut.append(tk.Entry(master=self.frm_form, width=50, bg=self.rgb_hack((187, 255, 255))))
            # Использует менеджер геометрии grid для размещения ярлыков и
            # текстовых полей в строку, чей индекс равен idx.
            label.grid(row=idx, column=0, sticky="e")
            entry.grid(row=idx, column=1)
            self.entrybut[idx].grid(row=idx, column=1)
        self.frm_buttons = tk.Frame(borderwidth=3, bg=self.rgb_hack((0, 159, 166)))
        self.frm_buttons.grid(row=9, column=0, ipadx=5, ipady=5)

        btn_submit = tk.Button(master=self.frm_buttons, text="Отправить", bg=self.rgb_hack((187, 255, 255)))
        btn_submit.bind("<Button-1>", self.send_talon_r)
        btn_submit.grid(row=8, column=0, padx=10, ipadx=10)

        btn_clear = tk.Button(master=self.frm_buttons, text="Очистить", bg=self.rgb_hack((187, 255, 255)))
        btn_clear.bind("<Button-1>", self.clear)
        btn_clear.grid(row=8, column=1, ipadx=10)

    def del_talon(self, event):
        self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=20, bg=self.rgb_hack((0, 159, 166)))
        self.frm_form.grid(row=8)
        for idx, text in enumerate(self.label_r):
            # Создает ярлык с текстом из списка ярлыков.
            label = tk.Label(master=self.frm_form, text=text, bg=self.rgb_hack((0, 159, 166)))
            # Создает текстовое поле которая соответствует ярлыку.
            entry = tk.Entry(master=self.frm_form, width=50)
            self.entrybut.append(tk.Entry(master=self.frm_form, width=50, bg=self.rgb_hack((187, 255, 255))))
            # Использует менеджер геометрии grid для размещения ярлыков и
            # текстовых полей в строку, чей индекс равен idx.
            label.grid(row=idx, column=0, sticky="e")
            entry.grid(row=idx, column=1)
            self.entrybut[idx].grid(row=idx, column=1)
        self.frm_buttons = tk.Frame(borderwidth=3, bg=self.rgb_hack((0, 159, 166)))
        self.frm_buttons.grid(row=9, column=0, ipadx=5, ipady=5)

        btn_submit = tk.Button(master=self.frm_buttons, text="Отправить", bg=self.rgb_hack((187, 255, 255)))
        btn_submit.bind("<Button-1>", self.delete_talon)
        btn_submit.grid(row=8, column=0, padx=10, ipadx=10)

        btn_clear = tk.Button(master=self.frm_buttons, text="Очистить", bg=self.rgb_hack((187, 255, 255)))
        btn_clear.bind("<Button-1>", self.clear)
        btn_clear.grid(row=8, column=1, ipadx=10)

    def del_patient(self, event):
        self.label1 = tk.Label(text="Полис пациента", bg=self.rgb_hack((0, 159, 166)))
        self.entry1 = tk.Entry(bg=self.rgb_hack((187, 255, 255)))
        self.label1.grid()
        self.entry1.grid()
        self.but = tk.Button(self.win, text="Ok", bg=self.rgb_hack((187, 255, 255)))
        self.but.bind("<Button-1>", self.delete_patient)
        self.but.grid()


    def add_patient(self, event):
        self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=20, bg=self.rgb_hack((0, 159, 166)))
        self.frm_form.grid(row=8)
        for idx, text in enumerate(self.label2):
            # Создает ярлык с текстом из списка ярлыков.
            label = tk.Label(master=self.frm_form, text=text, bg=self.rgb_hack((0, 159, 166)))
            # Создает текстовое поле которая соответствует ярлыку.
            entry = tk.Entry(master=self.frm_form, width=50)
            self.entrybut.append(tk.Entry(master=self.frm_form, width=50, bg=self.rgb_hack((187, 255, 255))))
            # Использует менеджер геометрии grid для размещения ярлыков и
            # текстовых полей в строку, чей индекс равен idx.
            label.grid(row=idx, column=0, sticky="e")
            entry.grid(row=idx, column=1)
            self.entrybut[idx].grid(row=idx, column=1)
        self.frm_buttons = tk.Frame(borderwidth=3, bg=self.rgb_hack((0, 159, 166)))
        self.frm_buttons.grid(row=9, column=0, ipadx=5, ipady=5)

        btn_submit = tk.Button(master=self.frm_buttons, text="Отправить", bg=self.rgb_hack((187, 255, 255)))
        btn_submit.bind("<Button-1>", self.send_patient)
        btn_submit.grid(row=8, column=0, padx=10, ipadx=10)

        btn_clear = tk.Button(master=self.frm_buttons, text="Очистить", bg=self.rgb_hack((187, 255, 255)))
        btn_clear.bind("<Button-1>", self.clear)
        btn_clear.grid(row=8, column=1, ipadx=10)

    def send_patient(self, event):
        try:
            for idx, text in enumerate(self.label2):
                if self.entrybut[idx].get() != '':
                    self.dict2[text] = self.entrybut[idx].get()
                    print(self.dict2[text])
                else:
                    raise InputError("Invalid input", "Check the input fields!")
            parol1 = hashlib.md5(self.dict2['Пароль:'].encode()).hexdigest()
            create_patient(self.dict2['Имя:'], self.dict2['Фамилия:'], self.dict2['Отчество:'], self.dict2['Адрес:'],
                           self.dict2['Телефон:'], parol1, self.dict2['Полис:'])
            self.entrybut.clear()
            self.frm_form.destroy()
            self.frm_buttons.destroy()
        except InputError as e:
            e.subscribe()

    def registrator(self):
        self.win = tk.Tk()
        self.win.title("Главная Администратора")
        self.win.config(bg=self.rgb_hack((0, 159, 166)))
        frm_form1 = tk.Frame(relief=tk.SUNKEN, borderwidth=20, bg=self.rgb_hack((0, 159, 166)))
        frm_form1.grid()
        but1 = tk.Button(frm_form1, bg=self.rgb_hack((187, 255, 255)))
        but1["text"] = "Добавить карту пациента"
        but1.config(width=20)
        but1.bind("<Button-1>", self.add_patient)
        but1.grid(row=1, column=1)

        but4 = tk.Button(frm_form1, bg=self.rgb_hack((187, 255, 255)))
        but4["text"] = "Удалить карту пациента"
        but4.config(width=20)
        but4.bind("<Button-1>", self.del_patient)
        but4.grid(row=1, column=2)

        but10 = tk.Button(frm_form1, bg=self.rgb_hack((187, 255, 255)))
        but10["text"] = "Изменить данные пациента"
        but10.config(width=20)
        but10.bind("<Button-1>", self.pat_id)
        but10.grid(row=2, column=1)

        but2 = tk.Button(frm_form1, bg=self.rgb_hack((187, 255, 255)))
        but2["text"] = "Добавить талон"
        but2.config(width=20)
        but2.bind("<Button-1>", self.add_talon_r)
        but2.grid(row=2, column=2)

        but5 = tk.Button(frm_form1, bg=self.rgb_hack((187, 255, 255)))
        but5["text"] = "Удалить талон"
        but5.config(width=20)
        but5.bind("<Button-1>", self.del_talon)
        but5.grid(row=3, column=1)

        but3 = tk.Button(frm_form1, bg=self.rgb_hack((187, 255, 255)))
        but3["text"] = "Выход"
        but3.config(width=20)
        but3.bind("<Button-1>", self.exit_)
        but3.grid(row=3, column=2)
        self.win.mainloop()
    ####################################################################################
    def init(self, event):
        self.login = self.entry.get()
        print(self.login)
        parol = self.entry1.get()
        print(parol)
        self.parol = hashlib.md5(parol.encode()).hexdigest()
        try:
            if self.login != '' and self.parol != '':
                if is_doctor(self.login):
                    if true_parol_d(self.login, self.parol):
                        self.__root.destroy()
                        self.doctor1(self.login)
                    else:
                        raise InputPar("Invalid input", "Incorrect parol!")
                elif is_patient(self.login):
                    if true_parol_p(self.login, self.parol):
                        self.__root.destroy()
                        self.patient(self.login)
                    else:
                        raise InputPar("Invalid input", "Incorrect parol!")
                elif is_registrator(self.login):
                    if true_parol_r(self.login, self.parol):
                        self.__root.destroy()
                        self.registrator()
                    else:
                        raise InputPar("Invalid input", "Incorrect parol!")
                elif is_admin(self.login):
                    if true_parol_a(self.login, self.parol):
                        self.__root.destroy()
                        self.admin()
                    else:
                        raise InputPar("Invalid input", "Incorrect parol!")
                else:
                    raise InputPar("Invalid input", "Incorrect login!")
            else:
                raise InputError("Invalid input", "Input login or parol!")
        except (InputError, InputPar) as e:
            e.subscribe()
            self.entry.delete(0, tk.END)
            self.entry1.delete(0, tk.END)

###################################################################################админ
    def send_doc(self, event):
        try:
            for idx, text in enumerate(self.labeld):
                if self.entrybut[idx].get() != '':
                    self.dictd[text] = self.entrybut[idx].get()
                else:
                    raise InputError("Invalid input", "Check the input fields!")
            parol1 = hashlib.md5(self.dictd['Пароль:'].encode()).hexdigest()
            create_doctor(self.dictd['Имя:'], self.dictd['Фамилия:'], self.dictd['Отчество:'], self.dictd['Адрес:'],
                           self.dictd['Телефон:'], parol1, self.dictd['Полис:'], self.dictd['Код специальности:'])
            self.entrybut.clear()
            self.frm_form.destroy()
            self.frm_buttons.destroy()
        except InputError as e:
            e.subscribe()

    def add_doc(self, event):
        self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=20, bg=self.rgb_hack((0, 159, 166)))
        self.frm_form.grid(row=8)
        for idx, text in enumerate(self.labeld):
            # Создает ярлык с текстом из списка ярлыков.
            label = tk.Label(master=self.frm_form, text=text, bg=self.rgb_hack((0, 159, 166)))
            # Создает текстовое поле которая соответствует ярлыку.
            entry = tk.Entry(master=self.frm_form, width=50)
            self.entrybut.append(tk.Entry(master=self.frm_form, width=50, bg=self.rgb_hack((187, 255, 255))))
            # Использует менеджер геометрии grid для размещения ярлыков и
            # текстовых полей в строку, чей индекс равен idx.
            label.grid(row=idx, column=0, sticky="e")
            entry.grid(row=idx, column=1)
            self.entrybut[idx].grid(row=idx, column=1)
        self.frm_buttons = tk.Frame(borderwidth=3, bg=self.rgb_hack((0, 159, 166)))
        self.frm_buttons.grid(row=9, column=0, ipadx=5, ipady=5)

        btn_submit = tk.Button(master=self.frm_buttons, text="Отправить", bg=self.rgb_hack((187, 255, 255)))
        btn_submit.bind("<Button-1>", self.send_doc)
        btn_submit.grid(row=8, column=0, padx=10, ipadx=10)

        btn_clear = tk.Button(master=self.frm_buttons, text="Очистить", bg=self.rgb_hack((187, 255, 255)))
        btn_clear.bind("<Button-1>", self.clear)
        btn_clear.grid(row=8, column=1, ipadx=10)

    def send_spec(self, event):
        try:
            for idx, text in enumerate(self.label_s):
                if self.entrybut[idx].get() != '':
                    self.dict_s[text] = self.entrybut[idx].get()
                else:
                    raise InputError("Invalid input", "Check the input fields!")
            create_spec(self.dict_s['Код специальности:'], self.dict_s['Название:'])
            self.entrybut.clear()
            self.frm_form.destroy()
            self.frm_buttons.destroy()
        except InputError as e:
            e.subscribe()

    def add_spec(self, event):
        self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=20, bg=self.rgb_hack((0, 159, 166)))
        self.frm_form.grid(row=8)
        for idx, text in enumerate(self.label_s):
            # Создает ярлык с текстом из списка ярлыков.
            label = tk.Label(master=self.frm_form, text=text, bg=self.rgb_hack((0, 159, 166)))
            # Создает текстовое поле которая соответствует ярлыку.
            entry = tk.Entry(master=self.frm_form, width=50)
            self.entrybut.append(tk.Entry(master=self.frm_form, width=50, bg=self.rgb_hack((187, 255, 255))))
            # Использует менеджер геометрии grid для размещения ярлыков и
            # текстовых полей в строку, чей индекс равен idx.
            label.grid(row=idx, column=0, sticky="e")
            entry.grid(row=idx, column=1)
            self.entrybut[idx].grid(row=idx, column=1)
        self.frm_buttons = tk.Frame(borderwidth=3, bg=self.rgb_hack((0, 159, 166)))
        self.frm_buttons.grid(row=9, column=0, ipadx=5, ipady=5)

        btn_submit = tk.Button(master=self.frm_buttons, text="Отправить", bg=self.rgb_hack((187, 255, 255)))
        btn_submit.bind("<Button-1>", self.send_spec)
        btn_submit.grid(row=8, column=0, padx=10, ipadx=10)

        btn_clear = tk.Button(master=self.frm_buttons, text="Очистить", bg=self.rgb_hack((187, 255, 255)))
        btn_clear.bind("<Button-1>", self.clear)
        btn_clear.grid(row=8, column=1, ipadx=10)


    def add_reg(self, event):
        self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=20, bg=self.rgb_hack((0, 159, 166)))
        self.frm_form.grid(row=8)
        for idx, text in enumerate(self.label2):
            # Создает ярлык с текстом из списка ярлыков.
            label = tk.Label(master=self.frm_form, text=text, bg=self.rgb_hack((0, 159, 166)))
            # Создает текстовое поле которая соответствует ярлыку.
            entry = tk.Entry(master=self.frm_form, width=50)
            self.entrybut.append(tk.Entry(master=self.frm_form, width=50, bg=self.rgb_hack((187, 255, 255))))
            # Использует менеджер геометрии grid для размещения ярлыков и
            # текстовых полей в строку, чей индекс равен idx.
            label.grid(row=idx, column=0, sticky="e")
            entry.grid(row=idx, column=1)
            self.entrybut[idx].grid(row=idx, column=1)
        self.frm_buttons = tk.Frame(borderwidth=3, bg=self.rgb_hack((0, 159, 166)))
        self.frm_buttons.grid(row=9, column=0, ipadx=5, ipady=5)

        btn_submit = tk.Button(master=self.frm_buttons, text="Отправить", bg=self.rgb_hack((187, 255, 255)))
        btn_submit.bind("<Button-1>", self.send_reg)
        btn_submit.grid(row=8, column=0, padx=10, ipadx=10)

        btn_clear = tk.Button(master=self.frm_buttons, text="Очистить", bg=self.rgb_hack((187, 255, 255)))
        btn_clear.bind("<Button-1>", self.clear)
        btn_clear.grid(row=8, column=1, ipadx=10)

    def send_reg(self, event):
        try:
            for idx, text in enumerate(self.label2):
                if self.entrybut[idx].get() != '':
                    self.dict2[text] = self.entrybut[idx].get()
                    print(self.dict2[text])
                else:
                    raise InputError("Invalid input", "Check the input fields!")
            parol1 = hashlib.md5(self.dict2['Пароль:'].encode()).hexdigest()
            create_registrator(self.dict2['Имя:'], self.dict2['Фамилия:'], self.dict2['Отчество:'], self.dict2['Адрес:'],
                           self.dict2['Телефон:'], parol1, self.dict2['Полис:'])
            self.entrybut.clear()
            self.frm_form.destroy()
            self.frm_buttons.destroy()
        except InputError as e:
            e.subscribe()

    def add_sc(self, event):
        self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=20, bg=self.rgb_hack((0, 159, 166)))
        self.frm_form.grid(row=8)
        for idx, text in enumerate(self.label_sc):
            # Создает ярлык с текстом из списка ярлыков.
            label = tk.Label(master=self.frm_form, text=text, bg=self.rgb_hack((0, 159, 166)))
            # Создает текстовое поле которая соответствует ярлыку.
            entry = tk.Entry(master=self.frm_form, width=50)
            self.entrybut.append(tk.Entry(master=self.frm_form, width=50, bg=self.rgb_hack((187, 255, 255))))
            # Использует менеджер геометрии grid для размещения ярлыков и
            # текстовых полей в строку, чей индекс равен idx.
            label.grid(row=idx, column=0, sticky="e")
            entry.grid(row=idx, column=1)
            self.entrybut[idx].grid(row=idx, column=1)
        self.frm_buttons = tk.Frame(borderwidth=3, bg=self.rgb_hack((0, 159, 166)))
        self.frm_buttons.grid(row=9, column=0, ipadx=5, ipady=5)

        btn_submit = tk.Button(master=self.frm_buttons, text="Отправить", bg=self.rgb_hack((187, 255, 255)))
        btn_submit.bind("<Button-1>", self.send_sc)
        btn_submit.grid(row=8, column=0, padx=10, ipadx=10)

        btn_clear = tk.Button(master=self.frm_buttons, text="Очистить", bg=self.rgb_hack((187, 255, 255)))
        btn_clear.bind("<Button-1>", self.clear)
        btn_clear.grid(row=8, column=1, ipadx=10)

    def send_sc(self, event):
        try:
            for idx, text in enumerate(self.label_sc):
                if self.entrybut[idx].get() != '':
                    self.dict_sc[text] = self.entrybut[idx].get()
                    print(self.dict_sc[text])
                else:
                    raise InputError("Invalid input", "Check the input fields!")
            create_schedule(self.dict_sc['Доктор:'], self.dict_sc['День:'], self.dict_sc['Начало работы:'], self.dict_sc['Конец работы:'],
                           self.dict_sc['Кабинет:'])
            self.entrybut.clear()
            self.frm_form.destroy()
            self.frm_buttons.destroy()
        except InputError as e:
            e.subscribe()

    def doc_id(self, event):
        self.label1 = tk.Label(text="Полис доктора", bg=self.rgb_hack((0, 159, 166)))
        self.entry1 = tk.Entry(bg=self.rgb_hack((187, 255, 255)))
        self.label1.grid()
        self.entry1.grid()
        self.but = tk.Button(self.win, text="Ok", bg=self.rgb_hack((187, 255, 255)))
        self.but.bind("<Button-1>", self.doc_up)
        self.but.grid()

    def send_doc_up(self, event, key):
        for idx, text in enumerate(self.labeld):
            self.dictd[text] = self.entrybut[idx].get()
        parol1 = hashlib.md5(self.dictd['Пароль:'].encode()).hexdigest()
        self.dictd['Пароль:'] = parol1
        update_doctor(key, self.dictd['Полис:'], self.dictd['Имя:'], self.dictd['Фамилия:'], self.dictd['Отчество:'], self.dictd['Телефон:'], self.dictd['Пароль:'], self.dictd['Адрес:'], self.dictd['Код специальности:'])
        self.entrybut.clear()
        self.frm_form.destroy()
        self.frm_buttons.destroy()

    def doc_up(self, event):
        try:
            id = self.entry1.get()
            if is_doctor(id):
                self.entry1.delete(0, tk.END)
                self.but.destroy()
                self.entry1.destroy()
                self.label1.destroy()
                self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=20, bg=self.rgb_hack((0, 159, 166)))
                self.frm_form.grid(row=8)
                for idx, text in enumerate(self.labeld):
                    # Создает ярлык с текстом из списка ярлыков.
                    label = tk.Label(master=self.frm_form, text=text, bg=self.rgb_hack((0, 159, 166)))
                    # Создает текстовое поле которая соответствует ярлыку.
                    entry = tk.Entry(master=self.frm_form, width=50)
                    self.entrybut.append(tk.Entry(master=self.frm_form, width=50, bg=self.rgb_hack((187, 255, 255))))
                    # Использует менеджер геометрии grid для размещения ярлыков и
                    # текстовых полей в строку, чей индекс равен idx.
                    label.grid(row=idx, column=0, sticky="e")
                    entry.grid(row=idx, column=1)
                    self.entrybut[idx].grid(row=idx, column=1)
                self.frm_buttons = tk.Frame(borderwidth=3, bg=self.rgb_hack((0, 159, 166)))
                self.frm_buttons.grid(row=9, column=0, ipadx=5, ipady=5)

                btn_submit = tk.Button(master=self.frm_buttons, text="Отправить", bg=self.rgb_hack((187, 255, 255)))
                btn_submit.bind("<Button-1>", self.send_doc_up)
                btn_submit.grid(row=8, column=0, padx=10, ipadx=10)

                btn_clear = tk.Button(master=self.frm_buttons, text="Очистить", bg=self.rgb_hack((187, 255, 255)))
                btn_clear.bind("<Button-1>", self.clear)
                btn_clear.grid(row=8, column=1, ipadx=10)
            else:
                raise InputError("Invalid input", "Check the doc id!")
        except InputError as e:
            e.subscribe()

    def sc_id(self, event):
        self.label1 = tk.Label(text="ID расписания", bg=self.rgb_hack((0, 159, 166)))
        self.entry1 = tk.Entry(bg=self.rgb_hack((187, 255, 255)))
        self.label1.grid()
        self.entry1.grid()
        self.but = tk.Button(self.win, text="Ok", bg=self.rgb_hack((187, 255, 255)))
        self.but.bind("<Button-1>", self.sc_up)
        self.but.grid()

    def send_sc_up(self, event, key):
        for idx, text in enumerate(self.label_sc):
            self.dict_sc[text] = self.entrybut[idx].get()
        update_schedule(key, self.dict_sc['Доктор:'], self.dict_sc['День:'], self.dict_sc['Начало работы:'], self.dict_sc['Конец работы:'],
                       self.dict_sc['Кабинет:'])
        self.entrybut.clear()
        self.frm_form.destroy()
        self.frm_buttons.destroy()

    def sc_up(self, event):
        try:
            id = self.entry1.get()
            if is_sc(id):
                self.entry1.delete(0, tk.END)
                self.but.destroy()
                self.entry1.destroy()
                self.label1.destroy()
                self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=20, bg=self.rgb_hack((0, 159, 166)))
                self.frm_form.grid(row=8)
                for idx, text in enumerate(self.label_sc):
                    # Создает ярлык с текстом из списка ярлыков.
                    label = tk.Label(master=self.frm_form, text=text, bg=self.rgb_hack((0, 159, 166)))
                    # Создает текстовое поле которая соответствует ярлыку.
                    entry = tk.Entry(master=self.frm_form, width=50)
                    self.entrybut.append(tk.Entry(master=self.frm_form, width=50, bg=self.rgb_hack((187, 255, 255))))
                    # Использует менеджер геометрии grid для размещения ярлыков и
                    # текстовых полей в строку, чей индекс равен idx.
                    label.grid(row=idx, column=0, sticky="e")
                    entry.grid(row=idx, column=1)
                    self.entrybut[idx].grid(row=idx, column=1)
                self.frm_buttons = tk.Frame(borderwidth=3, bg=self.rgb_hack((0, 159, 166)))
                self.frm_buttons.grid(row=9, column=0, ipadx=5, ipady=5)

                btn_submit = tk.Button(master=self.frm_buttons, text="Отправить", bg=self.rgb_hack((187, 255, 255)))
                btn_submit.bind("<Button-1>", self.send_sc_up)
                btn_submit.grid(row=8, column=0, padx=10, ipadx=10)

                btn_clear = tk.Button(master=self.frm_buttons, text="Очистить", bg=self.rgb_hack((187, 255, 255)))
                btn_clear.bind("<Button-1>", self.clear)
                btn_clear.grid(row=8, column=1, ipadx=10)

            else:
                    raise InputError("Invalid input", "Check the schedule id!")
        except InputError as e:
            e.subscribe()

    def reg_id(self, event):
        self.label1 = tk.Label(text="Полис регистратора", bg=self.rgb_hack((0, 159, 166)))
        self.entry1 = tk.Entry(bg=self.rgb_hack((187, 255, 255)))
        self.label1.grid()
        self.entry1.grid()
        self.but = tk.Button(self.win, text="Ok", bg=self.rgb_hack((187, 255, 255)))
        self.but.bind("<Button-1>", self.reg_up)
        self.but.grid()

    def send_reg_up(self, event, key):
        for idx, text in enumerate(self.label2):
            self.dict2[text] = self.entrybut[idx].get()
        parol1 = hashlib.md5(self.dict2['Пароль:'].encode()).hexdigest()
        self.dict2['Пароль:'] = parol1
        update_registrator(key, self.dict2['Имя:'], self.dict2['Фамилия:'], self.dict2['Отчество:'], self.dict2['Адрес:'],
                       self.dict2['Телефон:'], parol1, self.dict2['Полис:'])
        self.entrybut.clear()
        self.frm_form.destroy()
        self.frm_buttons.destroy()


    def reg_up(self, event):
        try:
            id = self.entry1.get()
            if is_registrator(id):
                self.entry1.delete(0, tk.END)
                self.but.destroy()
                self.entry1.destroy()
                self.label1.destroy()
                self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=20, bg=self.rgb_hack((0, 159, 166)))
                self.frm_form.grid(row=8)
                for idx, text in enumerate(self.label2):
                    # Создает ярлык с текстом из списка ярлыков.
                    label = tk.Label(master=self.frm_form, text=text, bg=self.rgb_hack((0, 159, 166)))
                    # Создает текстовое поле которая соответствует ярлыку.
                    entry = tk.Entry(master=self.frm_form, width=50)
                    self.entrybut.append(tk.Entry(master=self.frm_form, width=50, bg=self.rgb_hack((187, 255, 255))))
                    # Использует менеджер геометрии grid для размещения ярлыков и
                    # текстовых полей в строку, чей индекс равен idx.
                    label.grid(row=idx, column=0, sticky="e")
                    entry.grid(row=idx, column=1)
                    self.entrybut[idx].grid(row=idx, column=1)
                self.frm_buttons = tk.Frame(borderwidth=3, bg=self.rgb_hack((0, 159, 166)))
                self.frm_buttons.grid(row=9, column=0, ipadx=5, ipady=5)

                btn_submit = tk.Button(master=self.frm_buttons, text="Отправить", bg=self.rgb_hack((187, 255, 255)))
                btn_submit.bind("<Button-1>", self.send_reg_up)
                btn_submit.grid(row=8, column=0, padx=10, ipadx=10)

                btn_clear = tk.Button(master=self.frm_buttons, text="Очистить", bg=self.rgb_hack((187, 255, 255)))
                btn_clear.bind("<Button-1>", self.clear)
                btn_clear.grid(row=8, column=1, ipadx=10)
            else:
                raise InputError("Invalid input", "Check the registrator id!")
        except InputError as e:
            e.subscribe()

    def pat_id(self, event):
        self.label1 = tk.Label(text="Полис пациента", bg=self.rgb_hack((0, 159, 166)))
        self.entry1 = tk.Entry(bg=self.rgb_hack((187, 255, 255)))
        self.label1.grid()
        self.entry1.grid()
        self.but = tk.Button(self.win, text="Ok", bg=self.rgb_hack((187, 255, 255)))
        self.but.bind("<Button-1>", self.pat_up)
        self.but.grid()

    def send_pat_up(self, event, key):
        for idx, text in enumerate(self.label2):
            self.dict2[text] = self.entrybut[idx].get()
        parol1 = hashlib.md5(self.dict2['Пароль:'].encode()).hexdigest()
        self.dict2['Пароль:'] = parol1
        update_patient(key, self.dict2['Имя:'], self.dict2['Фамилия:'], self.dict2['Отчество:'],
                           self.dict2['Адрес:'],
                           self.dict2['Телефон:'], parol1, self.dict2['Полис:'])
        self.entrybut.clear()
        self.frm_form.destroy()
        self.frm_buttons.destroy()

    def pat_up(self, event):
        try:
            id = self.entry1.get()
            if is_patient(id):
                self.entry1.delete(0, tk.END)
                self.but.destroy()
                self.entry1.destroy()
                self.label1.destroy()
                self.frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=20, bg=self.rgb_hack((0, 159, 166)))
                self.frm_form.grid(row=8)
                for idx, text in enumerate(self.label2):
                    # Создает ярлык с текстом из списка ярлыков.
                    label = tk.Label(master=self.frm_form, text=text, bg=self.rgb_hack((0, 159, 166)))
                    # Создает текстовое поле которая соответствует ярлыку.
                    entry = tk.Entry(master=self.frm_form, width=50)
                    self.entrybut.append(tk.Entry(master=self.frm_form, width=50, bg=self.rgb_hack((187, 255, 255))))
                    # Использует менеджер геометрии grid для размещения ярлыков и
                    # текстовых полей в строку, чей индекс равен idx.
                    label.grid(row=idx, column=0, sticky="e")
                    entry.grid(row=idx, column=1)
                    self.entrybut[idx].grid(row=idx, column=1)
                self.frm_buttons = tk.Frame(borderwidth=3, bg=self.rgb_hack((0, 159, 166)))
                self.frm_buttons.grid(row=9, column=0, ipadx=5, ipady=5)

                btn_submit = tk.Button(master=self.frm_buttons, text="Отправить", bg=self.rgb_hack((187, 255, 255)))
                btn_submit.bind("<Button-1>", self.send_pat_up)
                btn_submit.grid(row=8, column=0, padx=10, ipadx=10)

                btn_clear = tk.Button(master=self.frm_buttons, text="Очистить", bg=self.rgb_hack((187, 255, 255)))
                btn_clear.bind("<Button-1>", self.clear)
                btn_clear.grid(row=8, column=1, ipadx=10)
            else:
                raise InputError("Invalid input", "Check the pat id!")
        except InputError as e:
            e.subscribe()


    def admin(self):
        self.win = tk.Tk()
        self.win.title("Главная Администратора")
        self.win.config(bg=self.rgb_hack((0, 159, 166)))
        frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=20, bg=self.rgb_hack((0, 159, 166)))
        frm_form.grid()
        but1 = tk.Button(frm_form, bg=self.rgb_hack((187, 255, 255)))
        but1["text"] = "Добавить карту пациента"
        but1.config(width=20)
        but1.bind("<Button-1>", self.add_patient)
        but1.grid(row=1, column=1)

        but4 = tk.Button(frm_form, bg=self.rgb_hack((187, 255, 255)))
        but4["text"] = "Добавить регистратора"
        but4.config(width=20)
        but4.bind("<Button-1>", self.add_reg)
        but4.grid(row=1, column=2)

        but2 = tk.Button(frm_form, bg=self.rgb_hack((187, 255, 255)))
        but2["text"] = "Добавить доктора"
        but2.config(width=20)
        but2.bind("<Button-1>", self.add_doc)
        but2.grid(row=1, column=3)

        but5 = tk.Button(frm_form, bg=self.rgb_hack((187, 255, 255)))
        but5["text"] = "Добавить специальности"
        but5.config(width=20)
        but5.bind("<Button-1>", self.add_spec)
        but5.grid(row=2, column=1)

        but6 = tk.Button(frm_form, bg=self.rgb_hack((187, 255, 255)))
        but6["text"] = "Добавить расписание"
        but6.config(width=20)
        but6.bind("<Button-1>", self.add_sc)
        but6.grid(row=2, column=2)

        but7 = tk.Button(frm_form, bg=self.rgb_hack((187, 255, 255)))
        but7["text"] = "Изменить расписание"
        but7.config(width=20)
        but7.bind("<Button-1>", self.sc_id)
        but7.grid(row=2, column=3)

        but8 = tk.Button(frm_form, bg=self.rgb_hack((187, 255, 255)))
        but8["text"] = "Изменить регистратора"
        but8.config(width=20)
        but8.bind("<Button-1>", self.reg_id)
        but8.grid(row=3, column=1)

        but9 = tk.Button(frm_form, bg=self.rgb_hack((187, 255, 255)))
        but9["text"] = "Изменить доктора"
        but9.config(width=20)
        but9.bind("<Button-1>", self.doc_id)
        but9.grid(row=3, column=2)

        but10 = tk.Button(frm_form, bg=self.rgb_hack((187, 255, 255)))
        but10["text"] = "Изменить пациента"
        but10.config(width=20)
        but10.bind("<Button-1>", self.pat_id)
        but10.grid(row=3, column=3)

        but3 = tk.Button(frm_form, bg=self.rgb_hack((187, 255, 255)))
        but3["text"] = "Выход"
        but3.config(width=20)
        but3.bind("<Button-1>", self.exit_)
        but3.grid(row=4, column=2)
        self.win.mainloop()
#######################################################################################
    def createPanelWithButton(self):
        self.label = tk.Label(text="Логин", bg=self.rgb_hack((0, 159, 166)))
        self.entry = tk.Entry(bg=self.rgb_hack((187, 255, 255)))
        self.label.pack()
        self.entry.pack()

        self.label1 = tk.Label(text="Пароль", bg=self.rgb_hack((0, 159, 166)))
        self.entry1 = tk.Entry(show='*', bg=self.rgb_hack((187, 255, 255)))
        self.label1.pack()
        self.entry1.pack()
        but1 = tk.Button(self.__root, text="Ok", bg=self.rgb_hack((187, 255, 255)))
        but1.bind("<Button-1>", self.init)
        but1.pack()
