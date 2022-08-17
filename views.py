from peewee import *
from models import *
from flask import Flask, render_template, request
from random import random,choice


app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        try:
            data = dict(request.form)
            User.create(name=data['Name'],phone_number = data['Phone number'], email = data['Email'], message = data['Message'])
        except:
            print('Error')
    return render_template('index.html')

@app.route('/feedback', methods = ['GET', 'POST'])
def feedback():
    User.select()
    data_all = User.select()
    return render_template('all_user.html', data = data_all)

@app.route('/game', methods = ['GET','POST'])
def game():
    if request.method == 'POST':
        forms_ = dict(request.form)
        print(forms_)
        all_number = [i for i in range(1, 37)]
        colors = ['Красный', 'Черный']
        ruletka = ['0:Зеленый']
        stavka = int(12)
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
    return render_template('game.html', data = total)


if __name__ == '__main__':
    app.run(debug=True)