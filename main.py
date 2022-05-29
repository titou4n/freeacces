from flask import Flask, render_template, request
app = Flask('app')


@app.route('/')
def acceuil():
    return ("Je suis la page d'acceuil")

@app.route('/signup')
def signup():
    #if request.method == 'POST':
        #recuperer = request.form['name']
        #return render_template('page2.html',name=recuperer)
    return("Je suis la page d'inscription'")

@app.route('/signin')
def signin():
    mail=str(mail)
    if mail  == :
        return ("Je suis la page de connection")
    
    pass #mail de la base
    


@app.route('/salon')
def salon():
    return print("Je suis la page de disccussion")

print("gouzi gouzi")
#git commit -m "First commit"
app.run(host='0.0.0.0', port=8080)