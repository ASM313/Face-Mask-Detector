from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import io, os
import numpy as np

apps = Flask(__name__)

# Load the trained model
model = load_model('artifacts/training/model.h5')

@apps.route('/')
def home():
    return render_template('first.html')

@apps.route("/train", methods=['GET','POST'])

def trainRoute():
    os.system("python main.py")
    msg= "Training done successfully!"
    return render_template('first.html', msg=msg)

@apps.route('/predict', methods=['POST'])
def predict():
    # Get the file from the POST request
    file = request.files['file']
    img_bytes = io.BytesIO(file.read())
    
    # Preprocess the image
    img = image.load_img(img_bytes, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    
    emotions=['Mask', 'No Mask']
    thoughts={'Mask':'safe', 
              'No Mask':'danger'}
    
    
    # Make prediction
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions[0])
    response = {
        'emotion': emotions[predicted_class],
        'thought': thoughts[emotions[predicted_class]]
    }
    
    return jsonify(response)

if __name__ == '__main__':
    apps.run(debug=True)
