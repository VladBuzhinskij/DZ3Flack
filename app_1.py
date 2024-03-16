from flask import Flask, render_template,make_response,request,url_for
from flask_sqlalchemy import SQLAlchemy
from models import db,User
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from forms import RegistrationForm
from flask import redirect


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///mydatabase.db'
app.config['SECRET_KEY']='52ce8509a8bf08d4e5dbdfec8ab10629fc9bda5748a79f86ab9d3deca1d12c0d'
csrf=CSRFProtect(app)
db.init_app(app)

@app.route('/')
def index():
    context={
        'registration':"0"
    }
    return render_template('index.html',**context)

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')



@app.route('/submit')
def registration_exit():
    context={
        'registration':"0"
    }
    return render_template('index.html',**context)
 
@app.route('/registration', methods=['GET','POST'])
def registration():
    form=RegistrationForm()
    if request.method=='POST' and form.validate():
        name=form.name.data
        name1=form.name1.data
        mail=form.mail.data
        password=form.password.data
        user=User(name=name,name1=name1,mail=mail,password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template('registration.html',form=form)




if __name__ == '__main__':
    app.run