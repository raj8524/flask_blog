from flask import Flask, render_template

app = Flask(__name__)


@app.route("/raj")
def serious():
    return render_template('index.html')


@app.route("/abc")
def kidding():
    name = "raj the tiger"
    return render_template('about.html', name2=name)


@app.route("/a")
def bootstrap():
    return render_template('bootstrap.html')

app.run(debug=True)
