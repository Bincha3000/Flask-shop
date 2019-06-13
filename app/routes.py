from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index/')
def index():
    user = {'username': 'Vlad'}
    posts = [
        {
            'author': {'username': 'Jhon'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susam'},
            'body': 'Good Job, very good job'
        },
        {
            'author': {'username': 'Tom'},
            'body': 'Super, i\'m fine!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Logn requested for user {}, remember_me {}'.format(
            form.username.data, form.remember_me.data))
        return redirect(ur_for('index'))
    return render_template('login.html', title='Sign In', form=form)