from flask import Flask, render_template

app = Flask("hello")

@app.route("/")
@app.route("/hello")


def hello():
    return "Ola"

@app.route("/meucontato")
def meuContato():
    return render_template("index.html")

app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)