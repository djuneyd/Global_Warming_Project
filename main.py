from flask import redirect
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///suggestions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Offers(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
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
    i = 0
    error = 'Такого логина не существует'
    if request.method == 'POST':
        form_login = request.form['login']

        users_db = User.query.all()

        for user in users_db:
            if user.login == form_login:
                name = form_login
                return redirect('/main')
        else:
            i = 1
            return render_template('login.html', error = error, i=i)

    else:
        return render_template('login.html',error=error, i=i)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    error = 'Такой логин уже был зарегестрирован'
    i = 0
    if request.method == 'POST':
        login = request.form['login']

        users = User.query.all()

        for user in users:
            if user.login == login:
                i = 1
                return render_template("register.html", error=error, i=i)
        else:
            user_card = User(login=login)

            db.session.add(user_card)
            db.session.commit()

            return redirect('/')
    else:
        return render_template("register.html", error=error, i=i)

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

@app.route('/offer', methods = ['GET', 'POST'])
def offer():
    global name
    if request.method == 'POST':
        offer = request.form['offer']

        offer_card = Offers(offer=offer, name=name)

        db.session.add(offer_card)
        db.session.commit()

        return redirect('/suggestions')
    else:
        return render_template("offer.html")

@app.route('/main_info')
def main_info():
    return render_template('must_know.html')

@app.route('/our_ai')
def ai():
    return render_template('ai_page.html')


if __name__ == "__main__":
    app.run(debug=True)