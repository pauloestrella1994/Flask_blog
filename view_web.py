from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from model import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e5abea61208527838844a7dfce77ca97'


posts = [{ 
           'author': 'Paulo Netto',
           'title': 'Blog post 1',
           'content': 'This is my post 1',
           'date_posted': 'June 24'

         },
        {  
           'author': 'Paulo Netto',
           'title': 'Blog post 1',
           'content': 'This is my post 1',
           'date_posted': 'June 24'
}
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home_page.html', posts=posts)

@app.route('/register', methods=["GET", "POST"])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    flash(f'Account created for {form.username.data}!', 'success')
    return redirect(url_for('home'))
  return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=["GET", "POST"])
def login():
  form = LoginForm()
  return render_template('login.html', title='Login', form=form)


app.run(debug=True)
