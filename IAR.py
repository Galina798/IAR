from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
from pycoingecko import CoinGeckoAPI
from requests import RequestException

# Подключаем API CoinGecko.com
cg = CoinGeckoAPI()


# изменение метки криптовалюты при выборе из комбобокса
def update_cr_label(event):
    cr_code = cr_combobox.get()  # получение выбранного кода криптовалюты
    cr_name = cr_cur[cr_code]  # получение полного названия по коду
    cr_label.config(text = cr_name)  # обновление текста метки


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
    t_code = t_combobox.get()  # получение выбранного кода валюты
    t_name = t_cur[t_code]  # получение полного названия по коду
    t_label.config(text = t_name)  # обновление текста метки


# словарь валют для конвертации
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


# функция получения курса обмена
def exchange():
    cr_code = cr_combobox.get()  # получаю данные о выбранной в комбобоксе криптовалюте
    t_code = t_combobox.get()   # получаю данные о выбранной в комбобоксе валюте

    if not cr_code or not t_code:  # проверка выбора валют
        mb.showwarning("Предупреждение", "Выберите криптовалюту и целевую валюту")  # предупреждение
        return  # выход из функции

    # получаю полное название выбранных валют
    cr_name = cr_cur.get(cr_code)  # получение названия криптовалюты
    t_name = t_cur.get(t_code)  # получение названия валюты

    if not cr_name:  # проверка поддержки криптовалюты
        mb.showerror("Ошибка", f"Монета {cr_code} не поддерживается")  # сообщение об ошибке
        return  # выход из функции

    try:
        # запрос к API для получения курса
        price_dict = cg.get_price(ids=cr_name.lower(), vs_currencies=t_code.lower())  # получение данных о цене
        price = price_dict[cr_name.lower()][t_code.lower()]  # извлечение цены из словаря
        # отображение результата
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


# Создание интерфейса
root = Tk()  # создание главного окна
root.title("Курсы обмена криптовалют")  # установка заголовка окна
root.geometry("400x250")  # установка размеров окна
root.configure(bg = "#F5DEB3")  # установка цвета фона

# метка - выбор криптовалюты, курс которой требуется узнать
ttk.Label(root, text = "Криптовалюта", foreground='#800000', background='#F5DEB3').pack(padx=10, pady=10)

# комбобокс для выбора криптовалюты
cr_combobox = ttk.Combobox(values = list(cr_cur.keys()))  # создание комбобокса с кодами криптовалют
cr_combobox.pack(padx=10, pady=5)  # размещение комбобокса
cr_combobox.bind("<<ComboboxSelected>>", update_cr_label)  # привязка события выбора

# метка для отображения названия криптовалюты
cr_label = ttk.Label(root, text='', foreground='#800000', background='#F5DEB3')  # создание пустой метки
cr_label.pack(padx=10, pady=5)  # размещение метки

# метка - выбор валюты для определения стоимости криптовалюты
ttk.Label(root, text = "Целевая валюта", foreground='#800000', background='#F5DEB3').pack(padx=10, pady=5)

# комбобокс для выбора целевой валюты
t_combobox = ttk.Combobox(values = list(t_cur.keys()))  # создание комбобокса с кодами валют
t_combobox.pack(padx=10, pady=5)  # размещение комбобокса
t_combobox.bind("<<ComboboxSelected>>", update_t_label)  # привязка события выбора

# метка для отображения названия валюты
t_label = ttk.Label(root, text='', foreground='#800000', background='#F5DEB3')  # создание пустой метки
t_label.pack(padx=10, pady=5)  # размещение метки

# кнопка "получить курс обмена"
Button(text = "Получить курс обмена криптовалюты", command=exchange, fg='#800000', bg='#FFFFE0').pack(padx=10, pady=5)  # создание и размещение кнопки


root.mainloop()  # запуск главного цикла обработки событий






