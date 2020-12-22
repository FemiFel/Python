# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя,
# фамилия,
# год рождения,
# город проживания,
# email,
# телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
import re

def info(name, second_name, date_of_birth, city, email, phone):
    return f'Вас зовут: {name} {second_name}\n' \
        f'Вы родились: {date_of_birth}\n' \
        f'Вы проживате в городе {city}\n' \
        f'Ваша электронная почта: {email}\n' \
        f'Ваш номер телефона: {phone}'

# def info(str):
#     name = re.compile(r'[а-яА-Я.]')
#     str = name.search(str)
#     return not bool(str)
# def info(str):
#     second_name = re.compile(r'[а-яА-Я.]')
#     str = second_name.search(str)
#     return not bool(str)
# def info(int):
#     date_of_birth = re.compile(r'[0-9"., "]')
#     int = date_of_birth.search(int)
#     return not bool(int)
# def info(str):
#     city = re.compile(r'[а-яА-Я.]')
#     str = city.search(str)
#     return not bool(str)
# def info(str):
#     email = re.compile(r'[a-zA-Z0-9"@._".]')
#     str = email.search(str)
#     return not bool(str)
# def info(int):
#     phone = re.compile(r'[0-9.]')
#     int = phone.search(int)
#     return not bool(int)

print(info(
    name=input('Укажите ваше имя: '),
    second_name=input('Укажите вашу фамилию: '),
    date_of_birth=input('Укажите вашу дату рождения: '),
    city=input('Укажите ваш город проживания: '),
    email=input('Укажите вашу электронную почту: '),
    phone=input('Укажите ваш номер телефона: ')
))