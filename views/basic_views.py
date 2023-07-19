from flask import Blueprint, render_template, redirect
from app.models import Question, Answer
from datetime import datetime
from app import db
from app.forms import QuestionForm, AnswerForm


fisa = Blueprint('basic', __name__, url_prefix='/')

@fisa.route('/')
def index():
    return render_template('index.html')

@fisa.route('/loop')
def loop():
    test = [1,2,3,4,5]
    return render_template('test.html', list = test)


@fisa.route('/me')
def about_me():
    return render_template('about_me.html')



