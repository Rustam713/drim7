from random import random,choice

all_number = [i for i in range(1,37)]
colors = ['Красный', 'Черный']
ruletka = ['0:Зеленый']
stavka = int(input('Поставьте ставку --> '))
lucky = input('Поставьте на какое-то число и цвет (пример: 16:Красный) --> ')
win = 0

for i in all_number:
    for j in colors:
        ruletka.append(f'{i}:{j}')


user = choice(ruletka)
print(f'Выпало число  {user}')
if lucky == user:
    if lucky == '0:Зеленый':
        print(user)
        total = stavka * 4
        print(f'User won {total}')
    print(user)
    total = stavka * 2
    print(f'User won {total}')
else:
    print('You lose')
