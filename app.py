from flask import Flask, render_template, request

app = Flask(__name__)

# --- Custom Birthday Settings ---
GIRLFRIEND_NAME = "Siya"
LOVE_MESSAGE = "Happy Birthday Siya 💖 You are my everything, my joy, and my forever. Today is your day to shine ✨🎂"
REASONS = [
    "Your smile makes my world brighter 🌸",
    "You have the kindest heart ❤️",
    "Every moment with you is a blessing ✨",
    "You make even simple days magical 🌈",
    "You are my forever happiness 💕"
]

@app.route("/")
def index():
    return render_template("index.html", name=GIRLFRIEND_NAME, message=LOVE_MESSAGE, reasons=REASONS)

@app.route("/gallery")
def gallery():
    return render_template("gallery.html", name=GIRLFRIEND_NAME)

@app.route("/love-note", methods=["POST"])
def love_note():
    note = request.form.get("note", "").strip()
    if not note:
        note = "P.S. Siya, you’ll always be my greatest gift 💗"
    return render_template("note.html", note=note, name=GIRLFRIEND_NAME)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
