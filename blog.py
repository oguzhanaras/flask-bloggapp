from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt


app = Flask(__name__)

# Config MySQL

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'blog_db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


# kullanıcı kayıt formu
class RegisterForm(Form):
    name = StringField("İsim Soyisim", validators=[validators.Length(min=4, max=25)])
    username = StringField("Kullanıcı Adı", validators=[validators.Length(min=5, max=25)])
    email = StringField("Email Adresi", validators=[validators.Email(message="Lütfen geçerli bir email adresi giriniz")])
    password = PasswordField("Parola:", validators=[
        validators.DataRequired(message="Lütfen bir parola belirleyin"),
        validators.Length(min=6, max=30),
        validators.EqualTo('confirm', message="Parolalar eşleşmiyor")
    ])
    confirm = PasswordField("Parolayı Doğrula")


mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)

    if request.method == 'POST':
        return redirect(url_for("index"))
    else:
        return render_template("register.html", form=form)

@app.route('/article/<string:id>')
def detail(id):
    return f"article id: {id}"

if __name__ == '__main__':
    app.run(debug=True)