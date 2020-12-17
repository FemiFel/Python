# sec = int(input('Укажите желаемое количество секунд: '))

sec = -1
while sec < 0:
    sec = int(input('Укажите желаемое количество секунд: '))
    # if (sec >= 0):
    #     break

h = ((sec // 3600)) % 24
m = (sec // 60) % 60
s = sec % 60

print('%02d:%02d:%02d' % (h, m, s))
