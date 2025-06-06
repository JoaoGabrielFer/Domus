from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime

views = Blueprint("views", __name__)

NICE_NAMES = {
    "piscina": "Piscina",
    "salaodefesta": "Salão de Festas",
    "quadra": "Quadra"
}

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
        return redirect(url_for('views.agendar'))

    future_events = []
    updated_lines = []
    now = datetime.now()

    try:
        with open("website/db.txt", "r") as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) == 3:
                    try:
                        hora_fim_dt = datetime.fromisoformat(parts[2])
                        if hora_fim_dt > now:
                            future_events.append(parts)
                            updated_lines.append(line)
                    except ValueError:
                        continue
    except FileNotFoundError:
        open("website/db.txt", "w").close()

    with open("website/db.txt", "w") as f:
        f.writelines(updated_lines)

    processed_schedules = []
    for event in future_events:
        local, inicio_str, fim_str = event
        schedule = {
            "local": NICE_NAMES.get(local, local.capitalize()),
            "inicio": datetime.fromisoformat(inicio_str),
            "fim": datetime.fromisoformat(fim_str)
        }
        processed_schedules.append(schedule)

    return render_template("agendar.html", db=processed_schedules)
