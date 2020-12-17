n = [7, 5, 3, 3, 2]

while True:
    new_dan = input('Укажите число от 1 до 9: ')
    if new_dan == 'q':
        break
    new_dan = int(new_dan)

    for i in range(1, len(n)):
        if new_dan >= max(n):
            n.insert(0, new_dan)
            break
        elif new_dan <= min(n):
            n.append(new_dan)
            break
        elif n[i - 1] >= new_dan >= n[i]:
            n.insert(i, new_dan)
    # n.sort()
    print(n)