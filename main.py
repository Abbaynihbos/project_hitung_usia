from flask import Flask
from flask import render_template
from flask import request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    web_title = "MAU CEK USIA KAMU ?"
    return render_template("home.html", web_title=web_title)

@app.route("/about")
def about():
    web_title = "Halaman About"
    return render_template("about.html", web_title=web_title)

@app.route("/contact")
def contact():
    web_title = "Halaman Contact"
    return render_template("contact.html", web_title=web_title)

@app.route("/nav")
def nav():
    web_title = "Halaman nav"
    return render_template("nav.html", web_title=web_title)

@app.route("/usia", methods=['GET','POST'])
def cek_usia():
    if request.method == 'POST':
        tahun_lahir = int(request.form['tahun_lahir'])
        tahun_sekarang = datetime.now().year
        usia = tahun_sekarang - tahun_lahir
        return render_template("cek_usia.html", usia=usia, tahun_lahir=tahun_lahir)
    return render_template("cek_usia.html", usia=None)

if __name__ == '__main__':
    app.run(debug=True)