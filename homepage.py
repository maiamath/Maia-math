from flask import *

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sistemasdinamicos")
def sistemas():
    return render_template("sd.html")

@app.route("/faleconosco")
def eu():
    return render_template("eu.html")

@app.route("/aritmetica")
def aritmetica():
    return render_template("aritimetica.html")

@app.route("/numerosnaturais")
def numerosnaturais():
    return render_template("naturais.html")

if __name__ == '__main__':
    app.run(debug=True)