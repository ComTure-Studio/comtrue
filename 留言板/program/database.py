from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# from flask import Flask
import pymysql

pymysql.install_as_MySQLdb()

# app=Flask(__name__)
# app.config['SECRET_KEY'] = '123'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/yiban'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['SQLALCHEMY_ECHO'] = True

db=SQLAlchemy()

class Student(db.Model):
    __tablename__='student'       #表的名字
    id = db.Column(db.String(50), nullable=True,primary_key=True,unique=True) #学号
    username=db.Column(db.String(50),nullable=True)     #姓名
    password=db.Column(db.String(50),nullable=True)     #密码

class Message(db.Model):
    __tablename__ = 'message'      #表的名字
    Num=db.Column(db.String(10), nullable=True,primary_key=True)
    Sender = db.Column(db.String(50), nullable=True)                      #发送者姓名
    SenderId=db.Column(db.String(50), nullable=True)                      #发送者学号
    recipient = db.Column(db.String(50), nullable=True)                   #接受者姓名
    recipientId = db.Column(db.String(50), nullable=True)                 #接受者学号当主键
    message=db.Column(db.Text,nullable=True)                              #留言信息
    time = db.Column(db.DateTime, default=datetime.now)                   #发送时间


# user1=User(id='1111111111',username='小甲',password='1')
# # user2=User(id='2222222222',username='小乙',password='2')
# # user3=User(id='3333333333',username='小丙',password='3')
# # db.session.add(user1)
# # db.session.add(user2)
# # db.session.add(user3)

# db.create_all()
# db.session.commit()


# @app.route('/')
# def index():
#     return "建表完成"
#