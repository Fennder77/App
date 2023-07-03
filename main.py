import customtkinter
from tkinter import *
from PIL import ImageTk
from tkinter import END

customtkinter.set_appearance_mode("dark")  # смена темы...
customtkinter.set_default_color_theme("dark-blue")  # цвета виджетов...

checked_tasks = []
def add(task_data):
    f = customtkinter.CTkFrame(root)

    customtkinter.CTkCheckBox(f, text=task_data["task"], var=task_data["completed"]).pack(anchor=NW, side=LEFT)
    customtkinter.CTkButton(f, image=img_del, text='', width=30, command=lambda: remove_task(f, task_data)).pack(anchor=NW, side=LEFT, padx=10)
    f.pack(anchor=NW, padx=5, pady=5)

    if task_data["completed"]:
        checked_tasks.append(f)
def move_checked_tasks_down():  # перемещение отмеченных задач вниз
    for task_frame in checked_tasks:
        task_frame.pack_forget()

    for task_frame in checked_tasks:
        task_frame.pack(anchor=NW, padx=5, pady=5)

    checked_tasks.clear()
def remove_task(frame, task_data):  # удаление задачи
    if task_data["completed"]:
        checked_tasks.remove(frame)
    frame.pack_forget()


def add(task):
    f = customtkinter.CTkFrame(root)

    customtkinter.CTkCheckBox(f, text=task).pack(anchor=NW, side=LEFT)  # виджет
    customtkinter.CTkButton(f, image=img_del, text='', width=30, command=lambda: f.pack_forget()).pack(anchor=NW, side=LEFT, padx=10)  # кнопка для удаления задачи
    f.pack(anchor=NW, padx=5, pady=5)  # отображение виджета


def add_task():
    window = customtkinter.CTkToplevel(root)  # дочернее окно
    window.title('Добавить задачу')  # заголовок
    window.geometry('300x80')  # разрешение

    task_text = customtkinter.CTkEntry(window, width=250)  # текстовое поле
    task_text.pack(pady=5)  # отступ

    def clear_entry():
        task_text.delete(0, END)  # очистка после ввода

    task_text.bind("<Return>", lambda event: [add(task_text.get()), clear_entry()])  # связываем нажатие клавиши Enter с добавлением задачи и очисткой поля ввода

    customtkinter.CTkButton(window, text='Добавить', font=('Times', 13), command=lambda: [add(task_text.get()), clear_entry()]).pack()  # кнопка на дочернее окно

    window.mainloop()

root = customtkinter.CTk()  # Создание класса
root.title("Планировщик задач")  # заголовок
root.geometry('700x300')  # разрешение окна

img_del = ImageTk.PhotoImage(file='del.png')  # отметка


btn_add_task = customtkinter.CTkButton(root, text='Добавить задачу', font=('Times', 13), command=add_task)  # добавить кнопку
btn_add_task.pack(anchor=S, side=BOTTOM, pady=5)  # расположение кнопки

btn_move_down = customtkinter.CTkButton(root, text='Cортировать', font=('Times', 13), command=move_checked_tasks_down)  # добавить кнопку
btn_move_down.pack(anchor=S, side=BOTTOM, pady=5)  # расположение кнопки
root.mainloop()