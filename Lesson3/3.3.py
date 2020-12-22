# Реализовать функцию my_func(),
# которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func (a, b, c, d):
    res = [a, b, c, d]
    max_el = max(res)
    res.remove(max_el)
    return max_el + max(res)

print(my_func(5,8,7,6))