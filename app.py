from flask import Flask, render_template, redirect, request

app = Flask(__name__)

app.secret_key = "123590"

lista_de_comentario = []

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

    if email == "pietro@gmail.com" and senha == "123":
        return redirect("/comentario")
    else:
        return render_template("login.html", erro = "Acesso Negado!")


@app.route("/comentario", methods=["GET"])
def pagina_comentario():
    return render_template("comentarios.html", lista_de_comentario = lista_de_comentario)

@app.route("/adicionar_comentario", methods=["POST"])
def adicionar_comentario():
    comentario = request.form.get("comentario")
    lista_de_comentario.append(comentario)
    print(lista_de_comentario)
    return redirect("/comentario")


app.run(debug=True)

