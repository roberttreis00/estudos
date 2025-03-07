from . import app
from flask import render_template, flash, redirect, url_for
from .forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {
        'username': 'Robertt',
    }
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beuatiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Os Vingadores é filme TOP'
        }
    ]
    return render_template('index.html', data=user, posts=posts)


Democrata = {
    "604203": 158.64,
    "604202": 158.64,
    "610101": 137.14,
    "527101": 146.91,
    "600102": 145.98,
    "240801": 122.43,
    "527103": 146.91,
    "448027": 130.53,
    "55202": 108.21,
    "526102": 129.01,
    "55201": 108.21,
    "526101": 123.41,
    "600101": 145.98,
    "527102": 145.64,
    "252101": 104.22,
    "298102": 124.93,
    "298101": 124.93,
    "272101": 116.57,
    "244102": 104.03,
    "244101": 104.03,
    "272103": 116.57,
    "272104": 120.56,
    "298103": 145.73,
    "298111": 124.93,
    "528101": 149.91,
    "528102": 153.43,
    "135201": 81.56,
    "255106": 118.24,
    "151119": 99.85,
    "298105": 124.93,
    "301105": 159.11,
    "336101": 124.93,
    "034034": 115.90,
    "240105": 122.43,
    "136201": 116.57,
    "450052": 104.03,
    "203201": 114.23,
    "240501": 122.43,
    "273105": 124.93,
    "151301": 109.67,
    "CIN0790": 48.61,
    "240106": 116.56,
    "265102": 137.37,
    "240201": 122.43,
}


@app.route('/teste')
def custos():
    return render_template('teste.html', democrata=Democrata)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login solicitado para Usuario: {form.username.data}, Lembrar-me: {form.remember_me.data}')
        return redirect(url_for('index'))

    return render_template('login.html', title="Login", form=form)
