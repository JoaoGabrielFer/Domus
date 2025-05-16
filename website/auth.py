from flask import Blueprint, render_template, request

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")
        with open("website/db.txt", "a") as f:
            f.write(f"{email} {senha}\n")
    return render_template("login.html")

@auth.route("/logout")
def logout():
    return ""

@auth.route("/sign-up")
def sign_up():
    return render_template("sign_up.html")
