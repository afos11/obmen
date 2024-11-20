from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
from tkinter.ttk import Combobox

import requests
import json



def update_c_label(event):
    code=t_combobox.get()
    name=cur[code]
    c_label.config(text=name)




def exchange():
    t_code=t_combobox.get().upper() #Целевая валюта
    b_code=b_combobox.get().upper() #базовая валюта


    if t_code and b_code:
        try:
            response=requests.get(f'https://open.er-api.com/v6/latest/{b_code}')#адрес сайта
            response.raise_for_status()
            data=response.json()#словарь в  data

            if t_code in data ['rates']: #сущ та валюта которую ввел пользователь
                exchange_rate=data['rates'][t_code] #курс обмена exchange_rate выбираем словарь data['rates'] значение по ключу [code]
                t_name=cur[t_code]
                b_name=cur[b_code]
                mb.showinfo('Курс обмена',
                            f'Курс к доллару: {exchange_rate:.2f} {t_name} за 1 {b_name}.')
            else:
                mb.showerror('Ошибка', f'Такая валюта  {t_code}не найдена')

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
    "UZS": "Узбекский сум",
    "USD": "Американский доллар"
}

window=Tk()
window.title('Курсы обмена валют! ')
window.geometry('500x500')

Label(text='Базовая валюта: ').pack(padx=10,pady=10)

#cur=["EUR", "JPY", "GBP", "AUD", "CAD", "CHF", "CNY", "RUB", "KZT","UZS"]

b_combobox=ttk.Combobox(values=list(cur.keys()))
b_combobox.pack(padx=10,pady=10)
b_combobox.bind('<<ComboboxSelected>>',update_c_label)



Label(text='Целевая валюта: ').pack(padx=10,pady=10)

#cur=["EUR", "JPY", "GBP", "AUD", "CAD", "CHF", "CNY", "RUB", "KZT","UZS"]

t_combobox=ttk.Combobox(values=list(cur.keys()))
t_combobox.pack(padx=10,pady=10)
t_combobox.bind('<<ComboboxSelected>>',update_c_label)


#создаем метку чтобы вывести название валюты
c_label=ttk.Label()
c_label.pack(padx=10,pady=10)


Button(text='Получить курс обмена!', command=exchange).pack()


window.mainloop()

