from flask import Blueprint, render_template, request

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    # if request.method == "POST":
        # email = request.form.get("email")
        # senha = request.form.get("senha")
        # with open("website/db.txt", "a") as f:
        #     f.write(f"{email} {senha}\n")
    return render_template("login.html")

@auth.route("/logout")
def logout():
    return ""

@auth.route("/sign-up", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha1") if request.form.get("senha1") == request.form.get("senha2") else None
        condoid = request.form.get("condoid")
        if email != "" and condoid != "" and senha != "" or senha != None:
                with open("website/auth.txt", "a") as f:
                    f.write(f"{email} {senha} {condoid}\n")
    return render_template("sign_up.html")
