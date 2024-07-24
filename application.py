from flask import Flask, render_template, Response
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import cv2

application = Flask(__name__)

# Load the trained model
model = load_model('artifacts/training/model.h5')

# Load the Haar Cascade file for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

emotions = ['Mask', 'No Mask']


def preprocess_face(face):
    face = cv2.resize(face, (224, 224))
    face_array = image.img_to_array(face)
    face_array = np.expand_dims(face_array, axis=0)
    face_array /= 255.0
    return face_array

def gen_frames():
    camera = cv2.VideoCapture(0)  # Use 0 for web camera

    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            # Convert the frame to grayscale for face detection
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            for (x, y, w, h) in faces:
                # Extract the face region
                face = frame[y:y+h, x:x+w]
                face_array = preprocess_face(face)

                # Make prediction
                predictions = model.predict(face_array)
                predicted_class = np.argmax(predictions[0])
                confidence_scores = predictions[0]

                print(f'Predictions: {predictions}, Predicted class: {predicted_class}')

                # Draw the rectangle around the face and the emotion text
                emotion_text = emotions[predicted_class]
                
                if emotion_text==0:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    cv2.putText(frame, f'Face: {emotion_text}', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                else:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
                    cv2.putText(frame, f'Face: {emotion_text}', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
                
                    
            # Encode the frame in JPEG format
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@application.route('/')
def index():
    return render_template('live.html')

@application.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    application.run(debug=True)
