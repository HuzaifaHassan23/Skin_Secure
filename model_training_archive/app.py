from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

# ---------------------------------------------------------
# 1. CREATE FLASK APP
# ---------------------------------------------------------
app = Flask(__name__)

# ---------------------------------------------------------
# 2. LOAD TRAINED MODEL
# The CNN model trained to classify skin disease
# ---------------------------------------------------------
model = load_model("skin_disease_model_v5.h5")

# ---------------------------------------------------------
# 3. UPLOAD FOLDER SETUP
# User uploaded images will be saved here
# os.makedirs ensures folder exists
# ---------------------------------------------------------
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ---------------------------------------------------------
# 4. CLASS LABELS AND DISEASE MAP
# 'classes' → model output labels
# 'disease_map' → full human-readable disease names
# ---------------------------------------------------------
classes = ['akiec', 'bcc', 'bkl', 'df', 'mel', 'nv', 'vasc']
disease_map = {
    'akiec': 'Actinic Keratoses',
    'bcc': 'Basal Cell Carcinoma',
    'bkl': 'Benign Keratosis-like Lesions',
    'df': 'Dermatofibroma',
    'mel': 'Melanoma',
    'nv': 'Melanocytic Nevus',
    'vasc': 'Vascular Lesion'
}

# ---------------------------------------------------------
# 5. HOME PAGE ROUTE
# Just renders index.html
# ---------------------------------------------------------
@app.route('/')
def home():
    return render_template('index.html')

# ---------------------------------------------------------
# 6. PREDICTION ROUTE
# Accepts POST request when user uploads image
# ---------------------------------------------------------
@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']    # uploaded file
    if not file:
        return "No file uploaded!"  # error if no file

    # -----------------------------------------------------
    # 7. SAVE IMAGE TO UPLOAD FOLDER
    # -----------------------------------------------------
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # -----------------------------------------------------
    # 8. IMAGE PREPROCESSING
    # - Resize to 224x224
    # - Convert to array
    # - Normalize to 0-1
    # - Add batch dimension
    # -----------------------------------------------------
    img = image.load_img(file_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    # -----------------------------------------------------
    # 9. MODEL PREDICTION
    # pred → probabilities for each class
    # np.argmax → class with highest probability
    # -----------------------------------------------------
    pred = model.predict(img_array)
    pred_class = classes[np.argmax(pred)]
    confidence = np.max(pred)

    # -----------------------------------------------------
    # 10. CHECK CONFIDENCE
    # If confidence < 0.75 → prediction is unclear
    # Else → use full disease name from disease_map
    # -----------------------------------------------------
    if confidence < 0.75:
        full_name = "Unknown or Unclear Skin Condition"
    else:
        full_name = disease_map.get(pred_class, "Unknown")

    # -----------------------------------------------------
    # 11. RENDER RESULT BACK TO HTML
    # prediction → disease name
    # image_path → uploaded image path for display
    # -----------------------------------------------------
    return render_template('index.html', prediction=full_name, image_path=file_path)

# ---------------------------------------------------------
# 12. RUN FLASK APP
# debug=True → server reloads on code change
# ---------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
