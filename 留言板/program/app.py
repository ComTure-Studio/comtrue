from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from database import Student,Message
import pymysql
import qrcode

Num=1

app = Flask(__name__)
pymysql.install_as_MySQLdb()
app.config['SECRET_KEY'] = '123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/yiban'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('login.html')


@app.route('/admin', methods=['POST'])
def login():
    uid = request.values.get('id')
    password = request.values.get('password')
    try:
        user = Student.query.filter_by(id=uid).first()  # 方法1
        db.session.close()
        if password == user.password:  # 不需验证学号，只验证密码就行了。
            print("登录成功")
            return render_template('index.html', user=user)
        else:
            print("登录失败")
            return render_template('login.html', message='密码错误')

    except AttributeError:
        return render_template('login.html', message='学号不存在')


#发送留言
@app.route('/send', methods=['POST'])
def admin_send():
    global Num
    SenderId = request.values.get('SenderId')       #发送人学号
    Sender = request.values.get('Sender')           #发送人
    recipient = request.values.get('recipient')     #接收人
    recipientId = request.values.get('recipientId') #接收人学号
    message = request.values.get('message')         #留言信息
    # print(SenderId, Sender, recipient, recipientId, message)

    NewRecipient = Student.query.filter_by(id=recipientId).first()
    db.session.close()
    user=Student.query.filter_by(id=SenderId).first()
    db.session.close()
    # print(NewRecipient.password)
    if user:
        try:
            if recipient == NewRecipient.username:
                Message1 = Message(Num=str(Num),SenderId=SenderId, Sender=Sender,
                           recipient=recipient, recipientId=recipientId,
                           message=message)
                db.session.add(Message1)
                db.session.commit()
                db.session.close()
                print("发送成功")
                Num=Num+1
                return render_template('index.html', message='发送成功',user=user)
            else:
                print("发送失败")
                return render_template('index.html', message='请检查姓名和学号是否正确',user=user)
        except AttributeError:
            return render_template('index.html', message='请检查姓名和学号是否正确', user=user)
    else:
        return render_template('index.html', message='请检查姓名和学号是否正确', user=user)
#查看我收到的留言
@app.route('/find',methods=["POST"])
def find():
    Id = request.values.get('Id')
    username=request.values.get('username')
    print(Id,username)
    result=Message.query.filter_by(recipientId=Id).all()
    db.session.close()
    return render_template('find.html',result=result)

#查看我发送的留言
@app.route('/sent',methods=["POST"])
def sent():
    Id = request.values.get('Id')
    username=request.values.get('username')
    result=Message.query.filter_by(SenderId=Id).all()
    db.session.close()
    return render_template('sent.html',result=result)


@app.route('/pdf',methods=['POST'])
def text():
    message1=request.values.get('message')
    m = Message.query.filter_by(message=message1).first()
    db.session.close()
    return render_template('pdf.html', m=m)

@app.route('/pdf2',methods=['POST'])
def text2():
    message1=request.values.get('message')
    m = Message.query.filter_by(message=message1).first()
    db.session.close()
    return render_template('pdf2.html', m=m)

#查看我的二维码
@app.route('/qrcode',methods=['POST'])
def Newqrcode():
    Id = request.values.get('Id')
    username = request.values.get('username')
    d={'Id':Id,'username':username}
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(d)
    qr.make(fit=True)
    img = qr.make_image()
    img.save('./static/qrcode/'+Id+username+'.png')
    return render_template('myqrcode.html', Id=Id, username=username)

if __name__ == '__main__':
    app.run()
