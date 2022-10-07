import os
from pathlib import Path

from flask import Flask, jsonify, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        
        if "canvasImage" not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files["canvasImage"]

        if file:
            filename = secure_filename("picture.png")
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('index'))

        return jsonify({"status": "successful"})


if __name__ == "__main__":
    upload_path = Path(app.config["UPLOAD_FOLDER"])
    if not upload_path.exists():
        upload_path.mkdir()

    app.debug = True
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)