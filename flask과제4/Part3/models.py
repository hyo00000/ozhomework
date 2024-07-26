# model을 만든다는건 table을 만든다는거임
# 게시글 - board
# 유저 - user
# 객체를 만드는 단위는 단수다.

from db import db

class User(db.Model): #db.model을 상속 받고 있다.(알케미의 모델이란 기능을)
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    boards = db.relationship('Board', back_populates='author', lazy='dynamic')
# author를 역참조 

#게시글 객체 만들기
class Board(db.Model):
    __tablename__ = "boards"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(300))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    author = db.relationship('User', back_populates='boards')
# 게시글 작성을 할 때 유저의 아이디 값을 저장할 필요가 있다.
# 유저랑 보드라는 테이블이 게시물이 작성될 때마다 게시글에다가 유저 아이디 값을 foreign key로 저장을 한다면 나중에 게시글에서도 
# 어떤 유저가 게시글을 작성했는지 볼 수가 있다.