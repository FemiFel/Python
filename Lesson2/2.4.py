pol = str(input('Укажите несколько любых слов через пробел: ')).split()

i = 1
for i, pol in enumerate(pol):
    i += 1
    print(f' {i}: {pol[:10]}')

