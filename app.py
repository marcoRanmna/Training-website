from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

from logic import calc_bmr 

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'

app.config['MYSQL_USER'] = 'root'

app.config['MYSQL_PASSWORD'] = '12345'

app.config['MYSQL_DB'] ='training_website'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calorie-calculator', methods=['GET', 'POST'])
def calorie_calculator():
      if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        age = int(request.form['age'])
        gender = request.form['gender']
        training_difficulty = request.form['training_difficulty']

        bmr = calc_bmr.calculate_bmr(weight, height, age, gender, training_difficulty)
        return render_template('calorie_calculator_result.html', bmr=bmr)
      else:
        return render_template('calorie_calculator_form.html')


@app.route('/training-programs')
def training_programs():
    return render_template('training_programs.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)