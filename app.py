from flask import Flask, render_template, request, redirect, url_for, session, flash



app = Flask(__name__)

SECRET_KEY = "pudim" # sempre acessar de outro arquivo do computador, nunca no código
app.config.from_object(__name__)

# POSTS MOCK (simulando um banco de dados)

posts = [
    {
        "titulo": "Post 1",
        "texto": "Meu primeiro Post"
    },
    {
        "titulo": "Post 2",
        "texto": "Olha eu aqui de novo"
    },
    {
        "titulo": "Post 3",
        "texto": "Novo Post"
    }
]

# USER MOCKS
USERNAME = "germana"
PASSWORD = "14708249"

@app.route('/')
def exibir_entradas():
    #pegar os post no banco
    return render_template("exibir_entradas.html", entradas=posts)

@app.route('/inserir', methods=["POST"])
def inserir_entradas():
    novo_post = {
        "titulo": request.form['titulo'],
        "texto": request.form['texto'],
    }
    request.form['titulo']
    request.form['texto']
    return redirect(url_for('exibir_entradas'))


@app.route('/login', methods=["GET", "POST"])
def login ():
    erro = ""
    if request.method == "POST":
        if request.form['username'] == USERNAME and request.form['password'] == PASSWORD:
           session ['logado'] = True
           flash("Login efetuado com sucesso")
           return redirect(url_for('exibir_entradas'))
        erro = "Usuário ou senha inválidos"
    return render_template("login.html", erro=erro)

@app.route('/logout')
def logout():
    session.pop('logado', None)
    flash("Logout efetuado com sucesso")
    return redirect(url_for('exibir_entradas'))