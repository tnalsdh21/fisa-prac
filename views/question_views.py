from flask import Blueprint, render_template, redirect, request, flash,g, url_for
from app.models import Question, Answer
from datetime import datetime
from app import db
from app.forms import QuestionForm, AnswerForm

from views.auth_views import login_required

question = Blueprint('question', __name__, url_prefix='/question')


@question.route('/detail/<int:question_id>/')
def detail(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    if g.user != question.user:
        flash('수정권한이 없습니다')
        return redirect(url_for('question.detail', question_id=question_id))
    if request.method=='POST':
        form = QuestionForm()
        if form.validate_in_submit():
            form.populate_obj(question)
            db.session.commit()
            return redirect(url_for('question.detail', question_id = question_id))
        else:
            form = QuestionForm(obj=question)
    return render_template('question/question_detail.html', question=question, form= form)


@question.route('/list/')
def _list():
    question_list = Question.query.all()
    #최신순으로 10개씩 끊어서 
    page = request.args.get('page', type=int, default=1)  # 페이지
    question_list = Question.query.order_by(Question.create_date.desc())
    question_list = question_list.paginate(page=page, per_page=10)
    return render_template('question/question_list.html', question_list=question_list)

    
@question.route('/list1/')
def post_list():
    question_list = Question.query.all()
    return render_template('question/question_list.html', question_list= question_list)


@login_required
@question.route('/create', methods=['GET', 'POST'])
def create():
    # 입력양식에 데이터를 입력 받는다
    form = QuestionForm()
    # 로그인 한 경우, 로그인 하지 않은 경우
    # 데이터가 요구조건에 맞춰서 모두 잘 들어와있는지 
    if form.validate_on_submit():
        q = Question(subject=form.subject.data, content=form.content.data, create_date=datetime.now())
        db.session.add(q)
        db.session.commit()
        return redirect('/success')
    return render_template('question/question_form.html', form=form)

@question.route('/success')
def success():
    question_list = Question.query.all()
    return render_template('question/question_list.html', question_list= question_list)