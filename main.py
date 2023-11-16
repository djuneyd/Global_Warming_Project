from flask import redirect
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///suggestions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Offers(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    offer = db.Column(db.Text)

    def __repr__(self):
        return f'<Offers{self.id}>' 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<Card {self.id}>'

@app.route("/")
def log_reg():
    return render_template('log_reg.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    global name
    error = ''
    if request.method == 'POST':
        form_login = request.form['login']

        users_db = User.query.all()

        for user in users_db:
            if user.login == form_login:
                name = form_login
                return redirect('/main')
        else:
            error = 'Неправильный пользователь или пароль'
            return render_template('login.html', error = error)

    else:
        return render_template('login.html')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        login = request.form['login']

        users = User.query.all()

        for user in users:
            if user.login == login:
                error = 'Такая почта уже была зарегестрирована'
                return render_template("register.html", error=error)
        else:
            user_card = User(login=login)

            db.session.add(user_card)
            db.session.commit()

            return redirect('/')
    else:
        return render_template("register.html")

@app.route('/main')
def main_page():
    global name
    return render_template('index.html', name=name)

@app.route('/suggestions')
def suggestions():
    offers = Offers.query.order_by(Offers.id).all()
    i = 0
    return render_template('suggestions.html', offers=offers
                                            , i=i)

@app.route('/main_info')
def main_info():
    return render_template('must_know.html')


if __name__ == "__main__":
    app.run(debug=True)