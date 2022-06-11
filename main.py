from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
import bcrypt

app = Flask('app')
cluster=PyMongo( app, "mongodb://freeacces:freeacces@cluster.mongodb.net/admin")


#@app.route('/', methods=['POST','GET'])
#def acceuil():
    #if 'util' in session:
      #  return render_template('accueil.html',nom=session['util'])
   # else:
       # return render_template('accueil.html')    

@app.route('/', methods=['POST','GET'])
def acceuil():
	return render_template('accueil.html')    

@app.route('/logout')
def logout():
	session.clear()
	return redirect(url_for("index"))


@app.route('/login', methods=['POST','GET'])
def login():
	if request.method == 'POST':
		base_donne = cluster.db.test
		util = base_donne.find_one({'mail' : request.form['mail']})
		if util :
			if request.form['mdp'] == request.form['verif_mdp']:
				if bcrypt.checkpw(request.form['mdp'].encode('utf-8'), util['mdp']):
					session['util']= request.form['mail']
					return redirect(url_for("acceuil"))
				else:
					return render_template('login.html',erreur="Le mot de passe est incorect")
		else :
			return render_template('login.html', erreur="Le nom d'utlisateur n'existe pas")
	
	else:
		return render_template('login.html')



@app.route('/register', methods=['POST','GET'])
def register():
	if request.method == 'POST':
		base_donne = cluster.db.test
		if base_donne.find_one({'mail' : request.form['mail']}) :
			return render_template('register.html', erreur="Le mail existe deja")
		else :
			mdp_encrypte = bcrypt.hashpw(request.form['mdp'].encode('utf-8'),bcrypt.gensalt())
			base_donne.insert_one({'mail': request.form['mail'], 'mdp' : mdp_encrypte})
			session['util'] = request.form['mail']
			return redirect(url_for('acceuil'))
	else:
		return render_template('register.html')

#@app.route('/signup', methods=['POST','GET'])
#def signup():
    #if request.method == 'POST':
        #recuperer_mail = request.form['mail']
        #recuperer_mdp = request.form['mdp']
        #cluster.insert_one({"mail":"mail"},{"password":"password"})
        #return render_template('pageconnected.html',mail=recuperer_mail,mdp=recuperer_mdp)

#@app.route('/signin', methods=['POST','GET'])
#def signin():
    #if request.method == 'POST':
       # recuperer_mail = request.form['mail']
      #  recuperer_mdp = request.form['mdp']
        #if recuperer_mail==cluster.find_one({"mail":"mail"}) and recuperer_mdp == cluster.find_one({"password":"password"}):
           # return render_template('pageconnected.html',mail=recuperer_mail,mdp=recuperer_mdp)

#@app.route('/connected', methods=['POST','GET'])
#def connected():
    #return print("Je suis la page ou vous etes connectés")

#@app.route('/salon', methods=['POST','GET'])
#def salon():
    #return print("Je suis la page de disccussion")
    
#git commit -m "First commit"

app.run(host='0.0.0.0')