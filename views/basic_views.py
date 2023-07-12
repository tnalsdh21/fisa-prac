from flask import Blueprint, render_template

from app.models import Question

fisa = Blueprint('basic', __name__, url_prefix='/')


@fisa.route('/detail/<int:question_id>/')
def detail(question_id):
    question = Question.query.get(question_id)
    return render_template('question/question_detail.html', question=question)

@fisa.route('/list')
def post_list():
    question_list = Question.query.all()
    return render_template('question/question_list.html', question_list= question_list)