import os
from flask import Flask, redirect, url_for, render_template
import gunicorn

app = Flask(__name__, template_folder='templates')

imageFolder = os.path.join("static", "images")
app.config["UPLOAD_FOLDER"] = imageFolder


@app.route("/")
def index():
    # images = os.listdir(os.path.join(app.static_folder("images")))
    images = os.listdir('static/images')
    images = ['images/' + image for image in images]
    sorted_images = sorted(images)

    return render_template("index.html", images=sorted_images)


if __name__ == "__main__":
    app.run(debug=False)
