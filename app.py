from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simpan data di list (di PythonAnywhere tetap berfungsi)
pendaftar = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/daftar", methods=["GET", "POST"])
def daftar():
    if request.method == "POST":
        data = {
            "nama": request.form["nama"],
            "nisn": request.form["nisn"],
            "alamat": request.form["alamat"],
            "jurusan": request.form["jurusan"]
        }
        pendaftar.append(data)
        return redirect(url_for("data_pendaftar"))
    return render_template("daftar.html")

@app.route("/data")
def data_pendaftar():
    return render_template("data.html", pendaftar=pendaftar)

if __name__ == "__main__":
    app.run(debug=True)
