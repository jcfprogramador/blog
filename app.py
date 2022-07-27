from flask import Flask, render_template
from datetime import datetime

app = Flask("hello")

posts = [
    {
        "title": "Meu primeiro post",
        "body": "Eu escrevi este post para testar a pagina no flask",
        "description": "teste post flask",
        "author": "Julio C. Franco",
        "created": datetime(2002,7,25)
    },
    {
        "title": "O meu Segundo Post",
        "body": "Teste do Segundo Post",
        "author": "Julio C. Franco",
        "created": datetime(2022,7,26)
    },
]

@app.route("/")
def index(debug=True):
    return render_template("index.html", posts=posts)
    
app.run(debug=True)
    
if __name__ == '__main__':
    app.run(debug=True)