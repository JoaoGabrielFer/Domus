from flask import Blueprint, render_template, request

views = Blueprint("views", __name__)

@views.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        nome = request.form.get("nome")
        with open("website/db.txt", "a") as f:
           f.write(nome)
    return render_template("home.html", nome=nome)


