from app import app
from flask import render_template,request,make_response

@app.route('/')
def index():
    name = 'Aku Ankka'
    address = 'Ankkalinnankatu 13'
    response = make_response(render_template('template_index.html',name=name,title=address))
    response.headers.add('Cache-Control','no-cache')
    print(request.headers.get('User-Agent'))
    return response

@app.route('/user/<name>')
def user(name):
    return render_template('template_user.html',name=name)

@app.route('/user',methods=['GET','POST'])
def userParams():
    name = request.args.get('name')
    return render_template('template_user.html',name=name)

# this one line comment style
""" this is multiple 
    line comment style"""