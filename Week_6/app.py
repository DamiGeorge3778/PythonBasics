from flask import Flask, render_template, request, redirect

app = Flask(__name__)

from models import db, Author, Articles

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/authors', methods=['GET', 'POST'])
def authors():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        if name:
            new_author = Author(name=name, email=email)
            db.session.add(new_author)
            db.session.commit()
            return redirect('/authors')
        
    authors = Author.query.all()
    return render_template('authors.html', authors=authors)


@app.route('/articles', methods=['GET', 'POST'])
def articles():
    authors = Author.query.all()
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        author_id = request.form.get('author_id')
        category = request.form.get('category')
        if title and content and author_id and category:
            new_article = Articles(title=title, content=content, author_id=author_id, category=category)
            db.session.add(new_article)
            db.session.commit()
            return redirect('/articles')
    articles = Articles.query.all()
    return render_template('articles.html', articles=articles, authors=authors)
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

@app.route('/calculatetable', methods=['POST'])
def calculate_table():
    return render_template('calculate_table.html')

@app.route('/result', methods=['POST'])
def result():
    number_1 = request.form.get('number_1')
    answer1 = int(number_1) * 1
    answer2 = int(number_1) * 2
    answer3 = int(number_1) * 3
    answer4 = int(number_1) * 4
    answer5 = int(number_1) * 5
    return render_template('result.html', number_1=number_1, answer1=answer1, answer2=answer2, answer3=answer3, answer4=answer4, answer5=answer5)





if __name__ == '__main__':
    app.run(debug=True)
