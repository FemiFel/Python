sosed = input('Укажите любые значения через запятую: ').split(',')

for i in range(1, len(sosed) -1, 2):
    sosed[i], sosed[i+1] = sosed[i+1], sosed[i]

print(sosed)