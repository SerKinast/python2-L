bornyear = int(input('Напишите год рождения А.С. Пушкина: '))

if bornyear == 1799:
    bornday = int(input('Напишите день рождения: '))
    if bornday == 6:
        print('Верно')
    else:
        print('Неверный день рождения')
else:
    print('Неверный год')
