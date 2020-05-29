from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from database import User,Student
import pymysql


app = Flask(__name__)
pymysql.install_as_MySQLdb()
app.config['SECRET_KEY'] = '123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/jichuangweilai'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method=='GET':
        return render_template('index.html',message='请先进行登录')
    else:
        uid = request.values.get('Id')
        password = request.values.get('password')
        user = User.query.filter_by(id=uid).first()  # 方法1
        if user:
            if password == user.password:  # 不需验证学号，只验证密码就行了。
                student=Student.query.filter_by(Id=uid).first()
                return render_template('student.html',student=student)
            else:
                return render_template('index.html',message='学号或密码错误')
        else:
            return render_template('index.html',message='学号不存在')

if __name__ == '__main__':
    app.run()
