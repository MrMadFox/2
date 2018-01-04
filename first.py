from flask import Flask,render_template,request,redirect,session
import flask
import MySQLdb,os,random,smtplib
db=MySQLdb.connect("localhost","root","","home")

a=Flask(__name__)
a.secret_key=os.urandom(24)
@a.route("/")
def sai():
    return(render_template("login.html"))
@a.route("/check.html",methods=["POST","GET"])
def check():


    c=db.cursor()

    
    try:
        c.execute("insert into chat1 values('%s','%s');"%(session["email"],request.form["chat"]))
        print(1)
        c.execute("select email,chat from chat1;")
        text=c.fetchall()
        return(render_template("/check.html",var=[text,session["email"]]))
        
    except:
        print(2)
        if len(request.form["email"])==0:
            return(redirect("/"))
        c.execute("select pass from user1 where email='%s';"%request.form['email'])
        x1=c.fetchall()
        print(x1)
        if len(x1)==0:
            return(flask.redirect("/",code=302,Response=None))
        if request.form["pass"]==x1[0][0]:
            session["email"]=request.form["email"]
            c.execute("select email,chat from chat1;")
            text=c.fetchall()
            return(render_template("/check.html",var=[text,session["email"][:-10:1]]))
        print("")


    return(flask.redirect("/",code=302,Response=None))

@a.route("/rege.html",methods=["POST","GET"])
def rege():
    c=db.cursor()
    #print("insert into user1(email,pass) values('%s','%s')"%(request.form["email"],request.form["pass"]))
    if len(request.form["email"])!=0 and len(request.form["pass"])!=0:
        conn=smtplib.SMTP("smtp.gmail.com")
        conn.starttls()
        conn.login("saipraneethhome@gmail.com","saipraneethhome@gmail")
        m=random.randint(100000,999999)
        session["rand"]=m
        session["regemail"]=request.form["email"]
        session["regepass"]=request.form["pass"]
        conn.sendmail("saipraneethhome@gmail.com",request.form["email"],"ur confirmation number %d"%m)
        return(render_template("confirm.html",var=[request.form["email"]]))
        
        
    return(redirect("/"))
@a.route("/frege.html",methods=["POST","GET"])
def frege():
    c=db.cursor()
    print(session["rand"])
    if session["rand"]==int(request.form["otp"]):
        c.execute("insert into user1(email,pass) values('%s','%s');"%(session["regemail"],session["regepass"]))
    else :
        print(type(session["rand"]),type(request.form["otp"]))
    return(redirect("/"))

a.run()

