# 1. Приветствие
# 2. Мануал – как пользоваться программой и какие валюты доступны
# 3. Ввести исходную валюту
# 4. Ввести в какую валюту перевести
# 5. Количество валюты
# 6. Подсчёт
# 7. Вывод результата
import requests
#import online                  почему то не подргужается.

URL = "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_n9H6KPdm21BaXDGFkjrscSfYPCobHwHeWLLn6PGL"
#API_KEY = "fca_live_n9H6KPdm21BaXDGFkjrscSfYPCobHwHeWLLn6PGL"


def get_actual_currencies():
    r = requests.get(URL)
    return r.json().get('data')

CURRENCIES = get_actual_currencies()



def convert(amount, from_currency, to_currency, currencies):
    from_value = currencies.get(from_currency)  # CURrubRENCIES[current_currency]
    to_value = currencies.get(to_currency)

    coefficient = to_value / from_value
    return round(amount * coefficient, 2)


# 1
print("Добро пожаловать в конвертатор валют!")

# 2
print("""
Инструкция:
1. Ввести исходную валюту
2. Ввести результирующую валюту
3. Ввести количество валюты
""")

print("Доступные валюты:")

for key in CURRENCIES:
    print(f'* {key}')

# 3
current_currency = input("Введите исходную валюту: ").upper()
while not current_currency in CURRENCIES:
    current_currency = input('ТАкой валюты нет, введите существующую: ').upper()

# 4
result_currency = input("Введите исходную валюту: ").upper()
while not result_currency in CURRENCIES:
    result_currency = input('ТАкой валюты нет, введите существующую: ').upper()
# 5
amount = input("Введите количество: ")
# 6
result = convert(float(amount), current_currency, result_currency, CURRENCIES)

print(f'{amount} {current_currency} = {result} {result_currency}')
