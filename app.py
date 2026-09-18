from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/download")
def download():
    return send_from_directory(
        app.static_folder,
        "keep_system.py",
        as_attachment=True
    )

if __name__ == "__main__":
    print("السيرفر يعمل الآن!")
    print("افتح: http://127.0.0.1:5000")
    app.run(debug=True)