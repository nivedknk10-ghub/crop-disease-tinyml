import tensorflow as tf
import numpy as np
import cv2
import json
import requests
from flask import Flask, request, render_template
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
WEBHOOK_URL = "https://hook.relay.app/api/v1/playbook/cmmkns13d00hx0qm047hn75w8/trigger/uAH5YaTdszj04H4XkvULIg"

# Load class names
with open("model/class_names.json") as f:
    class_indices = json.load(f)

class_names = {v: k for k, v in class_indices.items()}

# Load TinyML model
interpreter = tf.lite.Interpreter(model_path="model/crop_disease_model.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()


def detect_disease(image_path):

    img = cv2.imread(image_path)
    img = cv2.resize(img, (128,128))
    img = img / 255.0
    img = np.expand_dims(img, axis=0).astype(np.float32)

    interpreter.set_tensor(input_details[0]['index'], img)
    interpreter.invoke()

    output = interpreter.get_tensor(output_details[0]['index'])

    class_index = np.argmax(output)
    confidence = float(output[0][class_index])

    disease = class_names[class_index]

    return disease, confidence


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    phone = request.form["phone"]
    file = request.files["image"]

    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER,filename)
    file.save(filepath)

    disease, confidence = detect_disease(filepath)

    payload = {
        "phone": phone,
        "disease": disease,
        "confidence": confidence
    }

    requests.post(WEBHOOK_URL, json=payload)

    return f"Disease detected: {disease}. SMS will be sent."


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
