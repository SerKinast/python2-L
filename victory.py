
'''
# г.р. Путина - 1952
# г.р. Лаврова - 1950
# г.р. Шойгу - 1955
# г.р. Небензя - 1962
# г.р. Володина - 1964
'''

begin = 'Да'

while begin == 'Да' or 'да':

    points = 0
    faults = 0

    bornPutin = int(input('Напишите год рождения Путина: '))
    if bornPutin == 1952:
        points += 1
    else:
        faults += 1
    bornLavrov = int(input('Напишите год рождения Лаврова: '))
    if bornLavrov == 1950:
        points += 1
    else:
        faults += 1
    bornShoygu = int(input('Напишите год рождения Шойгу: '))
    if bornShoygu == 1955:
        points += 1
    else:
        faults += 1
    bornNebenzya = int(input('Напишите год рождения Небензя: '))
    if bornNebenzya == 1962:
        points += 1
    else:
        faults += 1
    bornVolodin = int(input('Напишите год рождения Володина: '))
    if bornVolodin == 1964:
        points += 1
    else:
        faults += 1

    share = points*100/5
    print('Верных ответов:', points)
    print('Неверных ответов:', faults)
    print('Доля верных ответов:', share, '%')

    begin = input('Если хотите начать сначала, напишите "Да": ')