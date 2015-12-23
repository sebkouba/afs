
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def user_page():
    var = "My Text"
    return render_template("index.html", var=var)

if __name__ == '__main__':
    app.run(debug=True)
