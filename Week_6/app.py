from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route('/about')
def about():
    return "This is the about page."

@app.route('/contact')
def contact():
    return "This is the contact page."

@app.route('/hello')
def hello():
    fruit = "orange"
    return render_template('hello.html', fruit=fruit)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    age = request.form.get('age')
    fav_food = request.form.get('food')
    fav_color = request.form.get('color')
    return render_template('greet.html', name=name, age=age, fav_food=fav_food, fav_color=fav_color)

@app.route('/calculateform')
def calculate_form():
    return render_template('calculate_form.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    number1 = request.form.get('number1')
    number2 = request.form.get('number2')
    result = int(number1)+int(number2)
    return render_template('calculate_result.html', number1=number1, number2=number2, result=result)
if __name__ == '__main__':
    app.run(debug=True)