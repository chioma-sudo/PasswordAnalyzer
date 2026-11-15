from flask import Flask, render_template, request
from main import analyze_password, load_common_passwords 

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        password = request.form.get("password")
        common_passwords = load_common_passwords()
        results = analyze_password(password, common_passwords)
        return render_template("index.html", results=results)
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/tips")
def tips():
    return render_template("tips.html")

if __name__ == "__main__":
    app.run(debug=True)
