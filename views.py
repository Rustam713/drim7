
from models import *
from flask import Flask, render_template, request
from random import choice


app = Flask(__name__)

# datadata = [
#     {
#         'name' : 'game3', 'url': '/game'
#     }
# ]

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
    ura = ''
    if request.method == 'POST':
        forms_ = dict(request.form)
        print(forms_)
        all_number = [i for i in range(1, 37)]
        colors = ['Красный', 'Черный']
        ruletka = ['0:Зеленый']
        stavka = int(forms_['stavka'])
        lucky = forms_['choose']
        win = 0

        for i in all_number:
            for j in colors:
                ruletka.append(f'{i}:{j}')

        user = choice(ruletka)
        print(f'Выпало число  {user}')
        if lucky == '0:Зеленый':
            print(user)
            total = stavka * 4
            ura = f'User won {total}'
        elif lucky == user:
            print(user)
            total = stavka * 2
            ura = f'User won {total}'
        else:
            ura = f'You lose'
            print('You lose')
    return render_template('game.html', ura=ura)


if __name__ == '__main__':
    app.run(debug=True)