import secrets
import tkinter as tk
import tkinter.messagebox

from variables import characters
import os


def generate_pasword() -> None:
    '''Генерация пароля на основе алфавита characters'''
    MAX_PASSWORD_LENGTH = 200 # Ограничение по длине символов
    try:
        pas_len = int(entry_field_1.get()) #считывание значения из поля ввода
    except ValueError:
        tkinter.messagebox.showerror(title="Error", message="Input a integer value!")
        return
    if pas_len <= 0 or pas_len > MAX_PASSWORD_LENGTH: #валидация поля на количество символов
        tkinter.messagebox.showwarning(title="Warning", message='Invalid length of password!')
        return
    password = ''

    for i in range(0, pas_len):
        password += secrets.choice(characters) #сама генерация
    entry_field_2.delete(0, tk.END)
    entry_field_2.config(width=pas_len)
    entry_field_2.insert(0, password)


def save_password():
    '''Сохранение пароля в файл'''
    data = entry_field_2.get()
    if data == '':
        tkinter.messagebox.showwarning(title="Warning", message="Password was not saved!")
        return
    with open("pswd.txt", 'w+') as f:
        f.write(data)
        tkinter.messagebox.showinfo(title="Info", message="Password has been successfully saved!")


def open_file():
    '''Открытие файла с паролем'''
    os.startfile("pswd.txt")
    root.destroy()


root = tk.Tk()
root.title("Password generator")

label = tk.Label(root, text="Enter a length of password:")
label.grid(row=0, column=0, padx=5, pady=5)  # Размещаем в первой строке, первом столбце

# Создаем поле ввода
entry_field_1 = tk.Entry(root)
entry_field_1.grid(row=0, column=1, padx=5, pady=5)  # Размещаем в первой строке, втором столбце

button_generate = tk.Button(root, text="Generate", width=20, height=1, bg="black", fg="white", command=generate_pasword)
button_generate.grid(row=0, column=2, padx=5, pady=5)

result_label = tk.Label(root, text="Your password:")
result_label.grid(row=1, column=0, padx=5, pady=5)

entry_field_2 = tk.Entry(root)
entry_field_2.grid(row=1, column=1, padx=5, pady=5)

button_save = tk.Button(root, text="Save", width=20, height=1, bg="black", fg="white", command=save_password)
button_save.grid(row=1, column=2, padx=5, pady=5)

open_button = tk.Button(root, text="Open file", width=20, height=1, bg="black", fg="white", command=open_file)
open_button.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()



