from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]
    description = request.form.get("description", "")

    if file:
        file.save(f"uploads/{file.filename}")  # Save file in 'uploads' folder
        return "File uploaded successfully!"

    return "No file selected!"


if __name__ == "__main__":
    app.run(debug=True)
