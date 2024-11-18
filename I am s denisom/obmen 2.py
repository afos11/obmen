from tkinter import *
from tkinter import messagebox as mb
import requests
import json


def exchange():
    code=entry.get().upper()

    if code:
        try:
            response=requests.get('https://open.er-api.com/v6/latest/USD')#адрес сайта
            response.raise_for_status()
            data=response.json()#словарь в  data

            if code in data ['rates']: #сущ та валюта которую ввел пользователь
                exchange_rate=data['rates'][code] #курс обмена exchange_rate выбираем словарь data['rates'] значение по ключу [code]
                mb.showinfo('Курс обмена',
                            f'Курс к доллару: {exchange_rate} {code} за 1 доллар.')
            else:
                mb.showerror('Ошибка', f'Такая валюта  {code}не найдена')

        except Exception as e:
            mb.showerror('Ошибка', f'Произошла ошибка {e}')
    else:
        mb.showwarning('Внимание!','Вы не ввели код валюты!')# предупреждение



window=Tk()
window.title('Курсы обмена валют! ')
window.geometry('500x500')


Label(text='Введите код валюты: ').pack(padx=10,pady=10)

entry=Entry()
entry.pack(padx=10,pady=10)


Button(text='Получить курс обмена к доллару!', command=exchange).pack()


window.mainloop()

