from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/home")
def home():
    name = request.args.get("name")
    
    return render_template("index.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)
