from exts import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    telephone = db.Column(db.String(11), nullable=False)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(100), nullable=False)


class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    # now()获取得是服务器第一次运行得时间
    # now就是每次创建一个模型得时候 都获取当前时间
    create_time = db.Column(db.DateTime, default=datetime.now())
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    auther = db.relationship('User', backref=db.backref('questions'))


class Answer(db.Model):
    __tablename__ = 'answer'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    create_time=db.Column(db.DateTime,default=datetime.now)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    auther_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    question = db.relationship('Question', backref=db.backref('answers',order_by=id.desc()))
    author = db.relationship('User', backref=db.backref('answers'))















