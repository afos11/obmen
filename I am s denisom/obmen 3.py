from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
from tkinter.ttk import Combobox

import requests
import json



def update_c_label(event):
    code=combobox.get()
    name=cur[code]
    c_label.config(text=name)




def exchange():
    code=combobox.get().upper()

    if code:
        try:
            response=requests.get('https://open.er-api.com/v6/latest/USD')#адрес сайта
            response.raise_for_status()
            data=response.json()#словарь в  data

            if code in data ['rates']: #сущ та валюта которую ввел пользователь
                exchange_rate=data['rates'][code] #курс обмена exchange_rate выбираем словарь data['rates'] значение по ключу [code]
                c_name=cur[code]
                mb.showinfo('Курс обмена',
                            f'Курс к доллару: {exchange_rate:.2f} {c_name} за 1 доллар.')
            else:
                mb.showerror('Ошибка', f'Такая валюта  {code}не найдена')

        except Exception as e:
            mb.showerror('Ошибка', f'Произошла ошибка {e}')
    else:
        mb.showwarning('Внимание!','Вы не ввели код валюты!')# предупреждение

cur = {
    "EUR": "Евро","JPY": "Японская йена",
    "GBP": "Британский фунт стерлингов",
    "AUD": "Австралийский доллар",
    "CAD": "Канадский доллар",
    "CHF": "Швейцарский франк",
    "CNY": "Китайский юань",
    "RUB": "Российский рубль",
    "KZT": "Казахстанский тенге",
    "UZS": "Узбекский сум"
}

window=Tk()
window.title('Курсы обмена валют! ')
window.geometry('500x500')


Label(text='Выберете код валюты: ').pack(padx=10,pady=10)

#cur=["EUR", "JPY", "GBP", "AUD", "CAD", "CHF", "CNY", "RUB", "KZT","UZS"]

combobox=ttk.Combobox(values=list(cur.keys()))
combobox.pack(padx=10,pady=10)
combobox.bind('<<ComboboxSelected>>',update_c_label)


#создаем метку чтобы вывести название валюты
c_label=ttk.Label()
c_label.pack(padx=10,pady=10)


Button(text='Получить курс обмена к доллару!', command=exchange).pack()


window.mainloop()

