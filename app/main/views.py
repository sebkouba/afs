from flask import render_template, session, redirect, url_for, current_app, \
    jsonify
from .. import db
from ..models import User, Topic
from ..email import send_email
from . import main
from .forms import NameForm, TopicForm


@main.route('/', methods=['GET', 'POST'])
def index():
    topics = Topic.query.all()
    return render_template('index.html', topics=topics)


@main.route('/create', methods=['GET', 'POST'])
def create_entry():
    form = TopicForm()
    if form.validate_on_submit():
        topic = Topic(summary=form.summary.data,
                      description=form.description.data)
        db.session.add(topic)
        db.session.commit()
        return redirect(url_for('.index'))
    return render_template('create_topic.html', form=form)


@main.route('/view/<id>', methods=['GET', 'POST'])
def view_entry(id):
    topic = Topic.query.filter_by(id=id).first()
    form = TopicForm()
    if form.validate_on_submit():
        topic.summary = form.summary.data
        topic.description = form.description.data
        db.session.add(topic)
        db.session.commit()
        return redirect(url_for('.index'))
    else:
        form.summary.data = topic.summary
        form.description.data = topic.description
    return render_template('edit_topic.html', form=form)


@main.route('/upvote/<eid>', methods=['GET', 'POST'])
def upvote(eid):
    topic = Topic.query.filter_by(id=eid).first()
    upvotes = topic.upvote()
    db.session.add(topic)
    db.session.commit()
    return jsonify({'result': upvotes})


@main.route('/downvote/<eid>', methods=['GET', 'POST'])
def downvote(eid):
    topic = Topic.query.filter_by(id=eid).first()
    downvotes = topic.downvote()
    db.session.add(topic)
    db.session.commit()
    return jsonify({'result': downvotes})
