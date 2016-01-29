from app import app
from flask import render_template,request,make_response,flash,redirect
from app.forms import LoginForm
from app.forms import RegisterForm
from app.db_models import Users
from app import db

@app.route('/',methods=['GET','POST'])
def index():
    login = LoginForm()
    if request.method == 'GET':
        return render_template('template_index.html',form=login)
    else:
        if login.validate_on_submit():
            print(login.email.data)
            print(login.passw.data)
            return render_template('template_user.html')
        else:
            flash('Väärää tietoa. Anna oikeat tiedot.')
            return render_template('template_index.html',form=login)
@app.route('/user/<name>')
def user(name):
    return render_template('template_user.html',name=name)

@app.route('/user',methods=['GET','POST'])
def userParams():
    name = request.args.get('name')
    return render_template('template_user.html',name=name)
@app.route('/register',methods=['GET','POST'])
def register():
    register = RegisterForm()
    if request.method == 'GET':
        return render_template('template_register.html',form=register)
    else:
        if register.validate_on_submit():
            user = Users(register.email.data,register.passw.data)
            db.session.add(user)
            db.session.commit()
            flash("Success: email {0} registered.".format(register.email.data))
            print(register.email.data)
            print(register.passw.data)
            return redirect('/')
        else:
            flash('Warning; Väärää tietoa. Anna oikeat tiedot.')
            return render_template('template_register.html',form=register)

# this one line comment style
""" this is multiple 
    line comment style"""