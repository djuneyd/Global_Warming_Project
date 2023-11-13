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

@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)