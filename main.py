from flask import Flask, render_template, request
from flask_pymongo import PyMongo

app = Flask('app')
cluster=PyMongo( app, "mongodb://freeacces:freeacces@cluster.mongode.net/admin")


@app.route('/')
def acceuil():
    return render_template('accueil.html')

@app.route('/signup')
def signup():
    if request.method == 'POST':
        recuperer_mail = request.form['mail']
        recuperer_mdp = request.form['mdp']
        cluster.insert_one({"mail":"mail"},{"password":"password"})
        return render_template('pageconnected.html',mail=recuperer_mail,mdp=recuperer_mdp)

@app.route('/signin')
def signin():
    if request.method == 'POST':
        recuperer_mail = request.form['mail']
        recuperer_mdp = request.form['mdp']
        if recuperer_mail==cluster.find_one({"mail":"mail"}) and recuperer_mdp == cluster.find_one({"password":"password"}):
            return render_template('pageconnected.html',mail=recuperer_mail,mdp=recuperer_mdp)

@app.route('/connected')
def salon():
    return print("Je suis la page ou vous etes connectés")

@app.route('/salon')
def salon():
    return print("Je suis la page de disccussion")
    
#git commit -m "First commit"

app.run(host='0.0.0.0')