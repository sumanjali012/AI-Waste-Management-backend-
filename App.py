'''from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "success": True,
        "message": "Waste Management Backend is running!"
    })


if __name__ == "__main__":
    app.run(debug=True) '''

    
from flask import Flask, jsonify, request
from PIL import Image, UnidentifiedImageError
from io import BytesIO

app = Flask(__name__)

# Maximum image size: 5 MB
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}


@app.route("/")
def home():
    return jsonify({
        "success": True,
        "message": "Waste Management Backend is running!"
    })


@app.route("/api/upload", methods=["POST"])
def upload_image():

    # Check whether an image was uploaded
    if "image" not in request.files:
        return jsonify({
            "success": False,
            "message": "No image uploaded."
        }), 400

    file = request.files["image"]

    if file.filename == "":
        return jsonify({
            "success": False,
            "message": "Please select an image."
        }), 400

    # Check file extension
    filename = file.filename.lower()
    extension = (
        "." + filename.rsplit(".", 1)[-1]
        if "." in filename else ""
    )

    if extension not in ALLOWED_EXTENSIONS:
        return jsonify({
            "success": False,
            "message": "Upload JPG, JPEG, PNG, or WEBP images only."
        }), 415

    # Verify that the file is a real image
    try:
        image_bytes = file.read()
        image = Image.open(BytesIO(image_bytes))
        image.verify()

    except (UnidentifiedImageError, OSError, ValueError):
        return jsonify({
            "success": False,
            "message": "The uploaded file is not a valid image."
        }), 400

    return jsonify({
        "success": True,
        "message": "Image received and validated successfully!",
        "filename": file.filename,
        "next_step": "Connect the AI waste classifier."
    }), 200


@app.errorhandler(413)
def file_too_large(error):
    return jsonify({
        "success": False,
        "message": "Image is too large. Maximum size is 5 MB."
    }), 413


if __name__ == "__main__":
    app.run(debug=True)
