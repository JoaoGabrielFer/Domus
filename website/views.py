from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime
tks = []

with open("website/db.txt", "r") as f:
    for line in f:
        tks.append(line.split())

        

views = Blueprint("views", __name__)

@views.route("/", methods=["GET"])
def home():
    return render_template("home.html")

@views.route("/agendar", methods=["GET", "POST"])
def agendar():
    if request.method == "POST":
        local = request.form.get("local")
        hora = request.form.get("hora")
        horafinal = request.form.get("horafinal")
        if local and hora and horafinal:
            with open("website/db.txt", "a") as f:
                f.write(f"{local} {hora} {horafinal}\n")
    
    tks = []
    updated_lines = []
    now = datetime.now()

    with open("website/db.txt", "r") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 3:
                local, hora_inicio, hora_fim = parts
                try:
                    hora_fim_dt = datetime.fromisoformat(hora_fim)
                    if hora_fim_dt > now:
                        tks.append(parts)
                        updated_lines.append(line)
                except ValueError:
                    continue  

    with open("website/db.txt", "w") as f:
        f.writelines(updated_lines)

    return render_template("agendar.html", db=tks)


