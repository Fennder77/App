import customtkinter
from tkinter import *
from PIL import ImageTk

customtkinter.set_appearance_mode("dark")#смена темы...
customtkinter.set_default_color_theme("dark-blue")#цвета виджетов...


def add(task):
    f = customtkinter.CTkFrame(root)

    customtkinter.CTkCheckBox(f, text=task).pack(anchor=NW, side=LEFT)#виджет
    customtkinter.CTkButton(f, image=img_del, text='', width=30, command=lambda: f.pack_forget()).pack(anchor=NW, side=LEFT, padx=10)#конопка для удаления задачи
    f.pack(anchor=NW, padx=5, pady=5)#отображение виджета


def add_task():
    window = customtkinter.CTkToplevel(root)#дочернее окно
    window.title('Добавить задачу')#заголовок
    window.geometry('300x80')#разрешение

    task_text = customtkinter.CTkEntry(window, width=250)#текстовое поле
    task_text.pack(pady=5)#отступ

    customtkinter.CTkButton(window, text='Добавить', font=('Times', 13), command=lambda: add(task_text.get())).pack()#кнопка на дочернее окно

    window.mainloop()


root = customtkinter.CTk()#Создание класса
root.title("Планировщик задач")#заголовок
root.geometry('700x300')#разрешение окна

img_del = ImageTk.PhotoImage(file='del.png')#отметка

btn_add_task = customtkinter.CTkButton(root, text='Добавить задачу', font=('Times', 13), command=add_task)#добаавить кнопку
btn_add_task.pack(anchor=S, side=BOTTOM, pady=5)#росположение кнопки

root.mainloop()