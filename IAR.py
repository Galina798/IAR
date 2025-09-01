import requests
import json
import pprint
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


# изменение метки криптовалюты при выборе из комбобокса
def update_t_label(event):
    cr_code = cr_combobox.get()
    cr_name = cr_cur[cr_code]
    cr_label.config(text = cr_name)


# Зашить неотображаемую функцию перевода USD в 10 любых базовых валют
# изменение метки валюты при выборе из комбобокса
def update_t_label(event):
    t_code = t_combobox.get()
    t_name = t_cur[t_code]
    t_label.config(text = t_name)


# функция курса валют по отношению к доллару
# для возможности определения стоимости криптовалюты в других валютах
def hidden_exchange_rate():
    t_code = t_combobox.get()

    if t_code:
        try:
            response = requests.get('https://open.er-api.com/v6/latest/USD')
            response.raise_for_status()
            data = response.json()
            if t_code in data['hidden_rates']:
                exchange_rate = data['hidden_rates'][t_code]
                t_name = t_cur[t_code]
                print("Курс обмена", f"Курс: {exchange_rate} {t_name} за 1 USD")
            else:
                mb.showerror("Ошибка!", f"Валюта {t_code} не найдена")

        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}")
    else:
        mb.showwarning("Внимание", "Введите код валюты!")


 # переменная для определения курса валют по отношению к доллару
t_cur = {
    'RUB': 'Российиский рубль',
    'USD': 'Американский доллар',
    'EUR': 'Евро',
    'GBP': 'Британский фунт стерлингов',
    'JPY': 'Японская йена',
    'CNY': 'Китайский юань',
    'KZT': 'Казахский тенге',
    'UZS': 'Узбекский сум',
    'CHF': 'Швейцарский франк',
    'AED': 'Дирхам ОАЭ',
    'CAD': 'Канадский доллар',
}


# def exchange():
#     hidden_exchange_rate()





# Интерфейс
root = Tk()
root.title(text="Курсы криптовалют")
root.geometry("400x350")

# выбор криптовалюты, курс которой требуется узнать
ttk.Label(text = "Криптовалюта").pack(padx=10, pady=5)

cr_combobox = ttk.Combobox(values = list(cr_cur.keys()))
cr_combobox.pack(padx=10, pady=5)
cr_combobox.bind("<<ComboboxSelected>>", update_cr_label)

cr_label = ttk.Label()
cr_label.pack(padx=10, pady=5)

# выбор валюты для определения стоимости криптовалюты
ttk.Label(text = "Целевая валюта").pack(padx=10, pady=5)

t_combobox = ttk.Combobox(values = list(t_cur.keys()))
t_combobox.pack(padx=10, pady=5)
t_combobox.bind("<<ComboboxSelected>>", update_t_label)

t_label = ttk.Label()
t_label.pack(padx=10, pady=5)

# кнопка "получить курс обмена"
ttk.Button(text = "Получить курс обмена криптовалюты", command=exchange).pack(padx=10, pady=5)

root.mainloop()







