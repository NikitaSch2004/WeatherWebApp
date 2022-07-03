from re import sub
import sqlite3
from datetime import date,datetime


from requests import session
#conectare cu database-ul
db = sqlite3.connect('test.db',check_same_thread=False)
cursor = db.cursor()

def getTime():
    return datetime.now().strftime("%H:%M:%S")

def getDate():
    return date.today()

def GetFormatedDate(date):
    month = date[5:7]
    if month == '01':
        month = "January"
    elif month == '02':
        month = 'February'
    elif month == '03':
        month = 'March'
    elif month == '04':
        month = 'April'
    elif month == '05':
        month = 'May'
    elif month == '06':
        month = 'June'
    elif month == '07':
        month = 'July'
    elif month == '08':
        month = 'August'
    elif month == '09':
        month = 'September'
    elif month == '10':
        month = 'Octomber'
    elif month == '11':
        month = 'November'
    elif  month == '12':
        month = 'December'
    else:
        month = 'None'
    formatDay = date[8:]
    if formatDay[0] == '0':
        formatDay = date[9:]
    formatDate = formatDay + " " + month
    return formatDate

def isNone(*argv):
    for arg in argv:
        if not arg:
            return True
        else:
            continue

def validUser(user):
    info = cursor.execute("select user from register where user  = ?",[user]).fetchall()
    if len(info) == 0:
        return True
    else:
        return False

def validPassword(password,user):
    info = cursor.execute("SELECT HASHED_PASSWORD FROM REGISTER WHERE USER = ? ",[user]).fetchall()
    for passw in info:
        if password == passw[0]:
            return True
        else:
            return False

def updatePassword(password,user,ip):
    oldPass = cursor.execute("SELECT HASHED_PASSWORD FROM REGISTER WHERE USER = ?",[user]).fetchall()[0][0]
    id = cursor.execute("SELECT ID FROM REGISTER WHERE USER = ?",[user]).fetchall()[0][0]
    cursor.execute("UPDATE register set hashed_password = ? where user = ?",(password,user,))
    cursor.execute("INSERT INTO RESET (USER_ID,OLD_PASS,NEW_PASS,IP,DATE,TIME) VALUES (?,?,?,?,?,?)",(id,oldPass,password,ip,getDate(),getTime(),))
    db.commit()

def getLogin(user,password):
    info = cursor.execute("select user from register where user  = ? and hashed_password = ?",[user,password]).fetchall()
    if not len(info) == 0:
        return True
    else:
        return False

def registerDB(user,password):
    cursor.execute("INSERT INTO REGISTER (USER,HASHED_PASSWORD,DATE,TIME) VALUES (?,?,?,?)",(user,password,getDate(),getTime(),))
    db.commit()

def registerIP(ip,user):
    IP = ip['ip']
    id = cursor.execute("SELECT ID FROM REGISTER WHERE USER = ?",[user]).fetchall()[0][0]
    info = cursor.execute("SELECT * FROM IP_LOGS where ip = ? and user_id = ?",(IP,id,)).fetchall()
    if len(info) == 0:
        country = ip['country']
        city = ip['city']
        languages = ip['languages']
        flag = ip['flag']
        cursor.execute("INSERT INTO IP_LOGS (USER_ID,IP,COUNTRY,CITY,LANGUAGE,FLAG,DATE,TIME) VALUES (?,?,?,?,?,?,?,?)",
        (id,IP,country,city,languages,flag,getDate(),getTime(),))
        db.commit()
    
def registerMail(mail,subject,body,user):
        cursor.execute("INSERT INTO MAIL (USER_ID,MAIL,SUBJECT,BODY,DATE,TIME) VALUES (?,?,?,?,?,?)",(user,mail,subject,body,getDate(),getTime(),))
        db.commit()

