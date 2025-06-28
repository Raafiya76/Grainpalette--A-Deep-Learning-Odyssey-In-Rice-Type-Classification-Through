# 🌾 GrainPalette - A Deep Learning Odyssey in Rice Type Classification Through Transfer Learning

GrainPalette is an AI-powered solution that leverages deep learning to classify different types of rice grains based on images. Designed with farmers, agriculture scientists, and enthusiasts in mind, this project uses Convolutional Neural Networks (CNN) and transfer learning (MobileNetV4) to provide accurate rice type identification.

---

## 📌 Features

- 🌾 Identify up to **five types of rice grains**
- 🧠 Built with **TensorFlow** and **Keras**
- 🚀 Powered by **Transfer Learning** using **MobileNetV4**
- 💻 User-friendly web interface for image upload and prediction
- 🔍 Accurate and fast classification for agricultural use cases

---

## 🛠️ Tech Stack

- **Python 3**
- **TensorFlow / Keras**
- **OpenCV**
- **Matplotlib / NumPy / Pandas**
- **MobileNetV4 (Pre-trained model)**
- **Flask** (for web deployment)

---

## 📂 Project Structure

GrainPalette/
│
├── data/ # Dataset (organized in train/val/test folders)
├── model/ # Saved model and architecture
├── notebooks/ # Jupyter notebooks for training & EDA
├── static/ # Static images, CSS, JS (for web app)
├── templates/ # HTML templates (Flask app)
├── app.py # Flask application
├── train_model.py # Model training script
├── rice_predictor.py # Model loading and prediction
├── requirements.txt # Python dependencies
└── README.md


---

## 🧪 How It Works

1. Upload an image of a rice grain through the web interface.
2. The model preprocesses the image (resizing, normalization).
3. Using a MobileNetV4-based CNN, the system predicts the most probable rice type.
4. The result is displayed instantly with confidence scores.

---

## 🔍 Dataset

The dataset contains images of **five rice varieties**, each categorized into separate folders:
- Basmati
- Jasmine
- Arborio
- Brown
- Red

Ensure your dataset is organized like this:

🧠 Train the Model
bash
Copy
Edit
python train_model.py
Ensure dataset path is correctly configured in the script.

🌐 Run the Web App
bash
Copy
Edit
python app.py
Visit http://localhost:5000 in your browser.

📈 Sample Output
yaml
Copy
Edit
Uploaded image: rice_sample.jpg
Predicted class: Basmati
Confidence: 94.2%
🧠 Transfer Learning Info
Base Model: MobileNetV4

Layers: Frozen base + custom dense layers for classification

Optimizer: Adam

Loss Function: Categorical Crossentropy

👩‍💻 Author
Your Name
LinkedIn | GitHub

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙌 Acknowledgements
TensorFlow and Keras Teams

Open-source rice grain image datasets

Agricultural AI initiatives

yaml
Copy
Edit

