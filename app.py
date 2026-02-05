from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/")
def pagina_principal():
    return render_template("principal.html")

@app.route("/sobre")
def pagina_sobre():
    return render_template("sobre.html")

@app.route("/login", methods=["GET"])
def pagina_login():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login_post():
    email = request.form.get("email")
    senha = request.form.get("senha")

    if email == "pietro123" and senha == "123590":
        return "Voce acessou a pagina restrita"
    else:
        return render_template("login.html", erro = "Acesso Negado!")

# PAGINA RESTRITA
@app.route("/comentarios")
def pagina_comentario():
    return render_template("comentarios.html")


app.run(debug=True)

