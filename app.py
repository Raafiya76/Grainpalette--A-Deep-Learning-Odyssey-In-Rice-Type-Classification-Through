import tensorflow as tensorflow
import tensorflow_hub as hub
import warnings
warnings.filterwarnings('ignore')
import h5py
import numpy as np
import os
from flask import Flask, app,request,render_template
from tensorflow import keras
import cv2
import tensorflow_hub as hub


model = tf.keras.model.load_modelfilepath='rice.h5,custom_objectives={'keraslayer':hub.kerasLayer})
app = Flak(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/details')
def pred():
    return render_template('details.html')

@app.route('/result', methods=['GET', 'POST'])
def predict():
    if request.method == "POST":
        f = request.files['image']
        basepath = os.path.dirname(__file__)
        filepath = os.path.join(basepath, 'Data', 'val', f.filename)
        f.save(filepath)

        a2 = cv2.imread(filepath)
        a2 = cv2.resize(a2, (224, 224))
        a2 = np.array(a2) / 255.0
        a2 = np.expand_dims(a2, axis=0)

        pred = model.predict(a2)
        pred = pred.argmax()

        df_labels = {
            'arborio': 0,
            'basmati': 1,
            'ipsala': 2,
            'jasmine': 3,
            'karacadag': 4
        }

        prediction = ''
        for i, j in df_labels.items():
            if pred == j:
                prediction = i

        return render_template('results.html', prediction_text=prediction)

        if __name__ == "__main__":
            app.run(debug=True)