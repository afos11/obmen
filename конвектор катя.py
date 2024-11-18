from cProfile import label
from tkinter import *
from tkinter import messagebox as mb
import requests
from Scripts.блокнот import window
from bottle import response


def exchange():
    code=e.get().upper()

    if code:
        try:
            response=requests.get('https://open.er-api.com/v6/latest/USD')
            data=response.json()#словарь в  data

            if code in data



window=Tk()
window.title('Курс обмена валют! ')
window.geometry('500x500')


Label(text='Введите код валюты: ').pack(pady=10)

e=Entry()
e.pack()


Button(text='Получить курс обмена!', command=exchange).pack()








window.mainloop()

