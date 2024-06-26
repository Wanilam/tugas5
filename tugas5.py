from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def beranda():
    return render_template("beranda.html")

@app.route("/rekomendasi")
def rekomendasi():
    return render_template("rekomendasi.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/checkout")
def checkout():
    return render_template("checkout.html")

