from flask import Flask, jsonify, render_template, request, redirect, url_for # type: ignore
app = Flask(__name__)

events_list =[
    {
        "name": "API Workshop",
        "time": "7:00pm",
        "Location": "Room 420"
    },
    {
        "name": "AI Workshop",
        "time": "10:00am",
        "Location": "Room 420"
    },
    {
        "name": "Website Development Workshop",
        "time": "2:00pm",
        "Location": "Room 420"
    },
    {
        "name": "Hardware Workshop",
        "time": "5:00pm",
        "Location": "Room 420"
    },
    {
        "name": "Binary Workshop",
        "time": "8:00pm",
        "Location": "Room 450"
    }
]

announcements_list = [
    {
        "title": "Check-In/Arrival",
        "content": "9AM",
        "description": "Please check in at the registration desk upon arrival."
    },
    {
        "title": "Breakfast",
        "content": "9:30AM",
        "description": "Join us for breakfast in the main hall."
    },
    {
        "title": "Check-out",
        "content": "Midnight",
        "description": "Please check out of your rooms by midnight."
    },
    {
        "title": "Opening Ceremony",
        "content": "4:30PM",
        "description": "Join us for the opening ceremony in the main hall."
    }
]

@app.route('/')
def index():
    return render_template("dashboard.html", events=events_list, announcements=announcements_list)

@app.route("/events", methods=["GET"])
def events():
    return jsonify(events_list)

@app.route("/announcements", methods=["GET"])
def announcements():
    return jsonify(announcements_list)

@app.route("/dashboard", methods=["GET"])
def dashboard():
    return render_template("dashboard.html", events=events_list, announcements=announcements_list)

@app.route("/ask_question", methods=["GET", "POST"])
def ask_question():
    if request.method == "POST":
        question = request.form.get("question")
        # Here you would send the question to the email if possible, but for now just acknowledge receipt
        # Optionally, you could log or store the question
        print(f"Received question: {question}")
        return render_template("ask_question.html", submitted=True, question=question)
    return render_template("ask_question.html", submitted=False)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000, debug=True)