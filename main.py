from flask import Flask, render_template, request
from flask_pymongo import PyMongo

app = Flask('app')
cluster=PyMongo( app, "mongodb://freeacces:freeacces@cluster.mongode.net/admin")


@app.route('/')
def acceuil():
    return render_template('accueil.html')

@app.route('/signup')
def signup():
    cluster.insert_one({"mail":"mail"},{"password":"password"})
    #if request.method == "mail" and :
        #recuperer = request.form['mail']
    return render_template('page2.html')

@app.route('/signin')
def signin():
    #mail=str(mail)
    #if mail  == :
        return ("Je suis la page de connection")
    
    #pass #mail de la base
    


@app.route('/salon')
def salon():
    return print("Je suis la page de disccussion")

print("gouzi gouzi")
print("gouzi gouzi")
print("gouzi gouzi")
print("gouzi gouzi")
#git commit -m "First commit"

app.run(host='0.0.0.0')