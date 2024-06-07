from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Хранилище для данных пользователей
users = []

@app.route('/', methods=['GET', 'POST'])
def index():
    global users
    if request.method == 'POST':
        # Получение данных из формы
        name = request.form.get('name')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        age = request.form.get('age')

        # Добавление данных пользователя в список
        users.append({'name': name, 'city': city, 'hobby': hobby, 'age': age})

    return render_template('index.html', users=users)


if __name__ == '__main__':
    app.run(debug=True)