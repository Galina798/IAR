from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
from pycoingecko import CoinGeckoAPI
from requests import RequestException

# Подключаем API Coigecko.com
cg = CoinGeckoAPI()


# изменение метки криптовалюты при выборе из комбобокса
def update_cr_label(event):
    cr_code = cr_combobox.get()
    cr_name = cr_cur[cr_code]
    cr_label.config(text = cr_name)


# список криптовалют
cr_cur = {
    'BTC': 'Bitcoin',
    'ETH': 'Ethereum',
    'USDT': 'Tether',
    'XRP': 'Ripple',
    'BNB': 'Binancecoin',
    'SOL': 'Solana',
    'USDC': 'Usd-coin',
    'TRX': 'Tron',
    'DOGE': 'Dogecoin',
    'ADA': 'Cardano'
}


# изменение метки валюты при выборе из комбобокса
def update_t_label(event):
    t_code = t_combobox.get()
    t_name = t_cur[t_code]
    t_label.config(text = t_name)


# переменная для выбора валют
t_cur = {
    'RUB': 'Российиский рубль',
    'USD': 'Американский доллар',
    'EUR': 'Евро',
    'GBP': 'Британский фунт стерлингов',
    'JPY': 'Японская йена',
    'CNY': 'Китайский юань',
    'CHF': 'Швейцарский франк',
    'AED': 'Дирхам ОАЭ',
    'CAD': 'Канадский доллар',
}


def exchange():
    cr_code = cr_combobox.get()  # получаю данные о выбранной в комбобоксе криптовалюте
    t_code = t_combobox.get()   # получаю данные о выбранной в комбобоксе валюте

    if not cr_code or not t_code:
        mb.showwarning("Предупреждение", "Выберите криптовалюту и целевую валюту")
        return

    # получаю полное название выбранных валют
    cr_name = cr_cur.get(cr_code)
    t_name = t_cur.get(t_code)

    if not cr_name:
        mb.showerror("Ошибка", f"Монета {cr_code} не поддерживается")
        return

    try:
        price_dict = cg.get_price(ids=cr_name.lower(), vs_currencies=t_code.lower())
        price = price_dict[cr_name.lower()][t_code.lower()]
        mb.showinfo("Курс обмена", f"1 {cr_name} ({cr_code}) = {price} {t_name} ({t_code})")

    # обработка возможных ошибок API запроса
    except ValueError:
        mb.showerror("Ошибка!", "Произошла ошибка API(неверный ключ, лимиты)")
    except TypeError:
        mb.showerror("Ошибка!", "Введенная валюта не найдена")
    except ConnectionError:
        mb.showerror("Ошибка!", "Отсутствует интернет")
    except TimeoutError:
        mb.showerror("Ошибка!", "Долгий ответ сервера")
    except RequestException as req_e:
        mb.showerror("Ошибка!", f"Сетевая ошибка {req_e}")
    except Exception as e:
        mb.showerror("Ошибка!", f"Произошла ошибка: {e}")


# Интерфейс
root = Tk()
root.title("Курсы криптовалют")
root.geometry("400x250")
root.configure(bg = "#F5DEB3")

# выбор криптовалюты, курс которой требуется узнать
ttk.Label(root, text = "Криптовалюта", foreground='#800000', background='#F5DEB3').pack(padx=10, pady=10)

cr_combobox = ttk.Combobox(values = list(cr_cur.keys()))
cr_combobox.pack(padx=10, pady=5)
cr_combobox.bind("<<ComboboxSelected>>", update_cr_label)

cr_label = ttk.Label(root, text='', foreground='#800000', background='#F5DEB3')
cr_label.pack(padx=10, pady=5)

# выбор валюты для определения стоимости криптовалюты
ttk.Label(root, text = "Целевая валюта", foreground='#800000', background='#F5DEB3').pack(padx=10, pady=5)

t_combobox = ttk.Combobox(values = list(t_cur.keys()))
t_combobox.pack(padx=10, pady=5)
t_combobox.bind("<<ComboboxSelected>>", update_t_label)

t_label = ttk.Label(root, text='', foreground='#800000', background='#F5DEB3')
t_label.pack(padx=10, pady=5)

# кнопка "получить курс обмена"
Button(text = "Получить курс обмена криптовалюты", command=exchange, fg='#800000', bg='#FFFFE0').pack(padx=10, pady=5)


root.mainloop()







