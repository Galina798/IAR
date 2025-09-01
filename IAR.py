from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


# Зашить неотображаемую функцию перевода USD в 9 любых базовых валют




# Интерфейс
root = Tk()
root.title(text="Курсы криптовалют")
root.geometry("400x350")

# выбор криптовалюты, курс которой требуется узнать
ttk.Label(text = "Криптовалюта").pack(padx=10, pady=5)

cr_combobox = ttk.Combobox(values = list(cur.keys()))
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







