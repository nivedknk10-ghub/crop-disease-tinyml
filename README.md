🌱 AI Powered Crop Disease Detection System

An AI-based crop health monitoring system that detects plant diseases from leaf images using a TinyML model, then automatically sends treatment recommendations to farmers via SMS using an AI agent workflow.

The system is designed to be lightweight, scalable, and accessible, allowing farmers to simply upload a leaf image and receive disease diagnosis and remedies instantly.
📌 Project Overview

Crop diseases significantly reduce agricultural productivity. Early detection is critical for preventing crop loss.

This project uses:

    Computer Vision

    TinyML

    AI agents

    Web automation

to create a smart disease detection pipeline.

The system performs the following tasks:

    Farmer uploads a crop leaf image.

    TinyML model detects the disease.

    Disease information is sent to an AI agent.

    AI agent generates treatment suggestions.

    The treatment is sent to the farmer via SMS.

🧠 Technologies Used
| Technology               | Purpose                     |
| ------------------------ | --------------------------- |
| Python                   | Backend processing          |
| TensorFlow               | Model training              |
| TensorFlow Lite (TinyML) | Lightweight model inference |
| Flask                    | Web server                  |
| OpenCV                   | Image processing            |
| Relay.app                | AI agent workflow           |
| Twilio                   | SMS delivery                |
| HTML/CSS                 | Web interface               |
| Render                   | Deployment                  |

⚙️ System Architecture

The system follows this pipeline:
User (Web Interface)
        │
        ▼
Upload Leaf Image + Phone Number
        │
        ▼
Flask Edge Server
        │
        ▼
TinyML Model (.tflite)
Disease Detection
        │
        ▼
Webhook → Relay.app AI Agent
        │
        ▼
AI Generates Treatment
        │
        ▼
Twilio SMS API
        │
        ▼
Farmer Receives Diagnosis & Remedy

📷 Project Screenshots
Web Interface

Users upload a leaf image and their phone number.
Dataset

PlantVillage dataset used for model training.
Model Training

CNN model trained using TensorFlow.
Relay AI Workflow

AI agent processes disease information and generates treatment.
SMS Output

Farmers receive disease diagnosis and remedy via SMS.
🧪 Dataset

The model was trained using the PlantVillage Dataset, which contains labeled images of healthy and diseased crop leaves.

Dataset features:

    Multiple crop types

    Multiple disease classes

    Thousands of labeled images

🤖 Model

The system uses a Convolutional Neural Network (CNN) trained for plant disease classification.

Model characteristics:

    Image size: 128 × 128

    Framework: TensorFlow

    Converted to TensorFlow Lite

    Optimized for TinyML inference

🚀 How to Run the Project
1️⃣ Clone Repository
git clone https://github.com/YOUR_USERNAME/crop-disease-ai.git
cd crop-disease-ai
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Start the Server
python edge_server.py
4️⃣ Open Web Interface
http://localhost:5000

Upload a crop leaf image and phone number to receive diagnosis.


🌍 Deployment

The project is deployed using Render.

Deployment features:

    Flask backend hosted on Render

    Public URL for evaluation

    TinyML model running on server

    Webhook integration with Relay AI agent

    SMS delivery via Twilio

📩 Example SMS Output
Disease: Tomato Early Blight
Confidence: 56%

Remedy:
Mix 8–12 tbsp 3% hydrogen peroxide in 1 gallon water.
Spray all leaves every 2 weeks.
Remove infected leaves.

🎯 Key Features

✔ AI-based crop disease detection
✔ TinyML lightweight inference
✔ AI agent generated treatment recommendations
✔ SMS notification system
✔ Web-based image upload interface
✔ Cloud deployment
🔮 Future Improvements

    Mobile app integration

    Multilingual farmer support

    More crop disease classes

    Offline edge device deployment

    IoT sensor integration

👨‍💻 Author

Nived K
Made for IBM skillbuild program
AI Integrated Systems

📜 License

This project is for educational and research purposes.
