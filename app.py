from traceback import print_tb
from flask import Flask, redirect, render_template, request, session
from functools import wraps
from IP import getIp,validateIP
from helpers import isNone,validUser,registerDB,getLogin,validPassword,updatePassword,registerMail,GetFormatedDate
from mail import sendMail
from Weather import Refresh

app = Flask(__name__)
app.config.from_pyfile('config.py')
#VERIFY IF USER IS LOGGED IN 
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

#MAIN PAGE
@app.route('/',methods = ['POST','GET'])
def index():
    if request.method == 'POST':
        mail = request.form.get("mail")
        subject =  request.form.get("subject")
        body = request.form.get("body")
        if isNone(mail):
            return render_template("main.html",error = "Email not sent, please enter a valid mail adress!")
        elif not '@' in mail:
            return render_template("main.html",error = "Email not sent, please enter a valid mail adress!") 
        else:
            sendMail(mail,subject,body)
            registerMail(mail,subject,body,0)
            return render_template("main.html",error = "Email sent, thank you for your feedback!")
    else:
        return render_template("main.html",error = " ")

#REGISTER PAGE
@app.route('/register',methods = ['POST', 'GET'])
def register():
    if request.method == "POST":
        #GET USER INFORMATION FROM THE REGISTRATION FORM 
        user = request.form.get("user")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        #VERIFY IF THE INFORMATION IS VALID THEN REGISTER IT IN DATABASE OR THROW AN ERROR
        if isNone(user,password,confirmation):
            return render_template("register.html",error = "Blank username or password , please try again!")
        elif not validUser(user):
                return render_template("register.html",error = "Username already taken, please try another one!")
        elif not password == confirmation:
                return render_template("register.html",error = "Passwords do not match , please try again!")
        else:
            #REGISTER THE INFORMATION INTO DATABASE
            registerDB(user,password)
            return redirect('/')
    else:
        return render_template("register.html",error = " ")

#LOGIN PAGE
@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == "POST":
        user = request.form.get("user")
        password = request.form.get("password")
        if isNone(user,password):
            return render_template("login.html",error = "Blank username or password, pleasetry again!")
        elif not getLogin(user,password):
            return render_template("login.html",error = "Username or password is incorrect, please try again!")
        else:
            ip = request.access_route[0]
            session['user'] = user
            ipInfo = getIp(ip)
            if validateIP(ipInfo,user):
                session['ip'] = ip
        return redirect("/")
    else:
        return render_template("login.html",error = " ")

#RESET PAGE
@app.route('/reset',methods = ['POST', 'GET'])
@login_required
def reset():
    if request.method == "POST":
        old = request.form.get("oldPassword")
        new = request.form.get("newPassword")
        confirm = request.form.get("confirm")
        if isNone(old,new,confirm):
            return render_template("reset.html", error = "Blank old or new password , please try again!")
        elif not validPassword(old,session['user']):
            return render_template("reset.html", error = "Old password is incorrect, please try again!")
        elif not new  == confirm:
            return render_template("reset.html", error = "Passwords do not match, please try again!")
        else:
            updatePassword(new,session['user'],session['ip'])
            session.pop('user',default=None)
            session.pop('ip',default=None)
            return redirect('/')
    else:
        return render_template("reset.html", error = " ")

#LOGOUT PAGE
@app.route('/logout')
@login_required
def logout():
    session.pop('user',default=None)
    session.pop('ip',default=None)
    return redirect('/')

#WEATHER PAGE
@app.route('/weather',methods = ['POST', 'GET'])
@login_required
def weather():
    if request.method == "GET":
        info = Refresh(session['ip'])
        first_date = GetFormatedDate( info['forecast']['forecastday'][1]['date'])
        second_date = GetFormatedDate( info['forecast']['forecastday'][2]['date'])
        return render_template("weather.html",current = info['current'],img = info['current']['condition']['icon'],
        location = info['location']['country'],first_day = info['forecast']['forecastday'][1],second_day = info['forecast']['forecastday'][2],
        first_date = first_date, second_date = second_date)
    else:
        return render_template("weather.html")


if __name__ == "__main__":
    app.run()
