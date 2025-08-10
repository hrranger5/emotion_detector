from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    emotion = None
    if request.method == "POST":
        text = request.form["text"]
        emotion = detect_emotion(text) 
    return render_template("index.html", emotion=emotion)

def detect_emotion(text):
    if "happy" in text.lower():
        return "Happy 😊"
    elif "sad" in text.lower():
        return "Sad 😢"
    else:
        return "Neutral 😐"

if __name__ == "__main__":
    app.run(debug=True)
