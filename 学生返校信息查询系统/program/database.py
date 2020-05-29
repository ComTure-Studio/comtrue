from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()
app=Flask(__name__)
#
app.config['SECRET_KEY'] = '123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/jichuangweilai'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True
#
db=SQLAlchemy(app)

class User(db.Model):
    __tablename__='user'
    id = db.Column(db.String(50), nullable=True,primary_key=True) #学号
    password=db.Column(db.String(50),nullable=True)               #密码

class Student(db.Model):
    __tablename__ = 'student'
    college=db.Column(db.String(50), nullable=True)                #学院
    teacher = db.Column(db.String(50), nullable=True)              #导员
    teacherphone=db.Column(db.String(50), nullable=True)          #导员电话
    name = db.Column(db.String(50), nullable=True)                 #学生姓名
    Id = db.Column(db.String(50), nullable=True)                   #学生学号
    Class = db.Column(db.String(50), nullable=True)                #专业班级
    phone=db.Column(db.String(50), nullable=True, primary_key=True)#学生电话当主键
    dorm = db.Column(db.String(50), nullable=True)                 #宿舍

# user1=User.query.filter_by(id='0123456789').first()     #方法1
# print(user1.username)
# user1=User(id='admin',password='admin')
# db.session.add(user1)
# student1=Student(college='计算机科学与技术学院',teacher='魏伟',teacherphone='1234567890',name='admin',Id='admin',
#               Class='计算机科学与技术学院',phone='1234567890',dorm='XX号楼XXX')
# db.session.add(student1)
#
# db.create_all()
# db.session.commit()
#
# @app.route('/')
# def index():
#     return "建表完成"
