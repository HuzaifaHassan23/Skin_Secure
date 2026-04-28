import os
import cv2
import numpy as np
import base64
from io import BytesIO
from PIL import Image

# Suppress TensorFlow logging to keep your terminal clean
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
from tensorflow.keras.models import load_model

# 👉 IMPORT YOUR COLLEAGUE's CODE HERE!
# Note: Assuming you run your server from the Backend folder
from ai.grad_cam import generate_gradcam_heatmap

# --- 1. LOAD THE MODEL GLOBALLY ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "skin_disease_model_v5.h5")

try:
    model = load_model(MODEL_PATH)
    print("✅ AI Model successfully loaded into memory!")
except Exception as e:
    print(f"⚠️ Failed to load model: {e}")
    model = None

# The exact classes from your colleague's code
CLASSES = ['akiec', 'bcc', 'bkl', 'df', 'mel', 'nv', 'vasc']

DISEASE_NAMES = {
    'akiec': 'Actinic Keratoses',
    'bcc': 'Basal Cell Carcinoma',
    'bkl': 'Benign Keratosis',
    'df': 'Dermatofibroma',
    'mel': 'Melanoma (High Risk)',
    'nv': 'Melanocytic Nevi',
    'vasc': 'Vascular Lesion'
}

# --- 2. THE MAIN PREDICTION FUNCTION ---
def analyze_skin_image(image_bytes: bytes) -> dict:
    """Takes raw image bytes, runs the AI, and returns results + heatmap base64."""
    if model is None:
        return {"error": "Model not loaded on server."}

    # 1. Read Image from Memory Bytes (Super Fast!)
    nparr = np.frombuffer(image_bytes, np.uint8)
    img_bgr = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # 2. Preprocess exactly how the model expects
    img_resized = cv2.resize(img_bgr, (224, 224)) # type: ignore
    img_normalized = img_resized / 255.0
    img_batch = np.expand_dims(img_normalized, axis=0) # Shape: (1, 224, 224, 3)

    # 3. Predict & Get Top 3 Results!
    preds = model.predict(img_batch, verbose=0)[0]
    
    # Get indices of the top 3 highest probabilities
    top_3_indices = np.argsort(preds)[-3:][::-1]
    
    # Format the top 3 predictions for the frontend
    top_3_predictions = []
    for idx in top_3_indices:
        class_id = CLASSES[idx]
        top_3_predictions.append({
            "name": DISEASE_NAMES.get(class_id, class_id),
            "confidence": float(preds[idx]),
            "raw_id": class_id
        })

    # The #1 prediction dictates the main risk level
    primary_class = top_3_predictions[0]["raw_id"]
    risk_level = "high" if primary_class in ['mel', 'bcc'] else "med" if primary_class == 'akiec' else "low"

    # 4. Generate Heatmap using your colleague's imported function
    heatmap = generate_gradcam_heatmap(img_batch, model)
    
    # Apply colormap in memory
    heatmap_resized = cv2.resize(heatmap, (224, 224))
    heatmap_uint8 = np.uint8(255 * heatmap_resized)
    heatmap_color = cv2.applyColorMap(heatmap_uint8, cv2.COLORMAP_JET) # type: ignore

    # Blend original and heatmap
    superimposed_img = cv2.addWeighted(img_resized, 0.6, heatmap_color, 0.4, 0)
    superimposed_rgb = cv2.cvtColor(superimposed_img, cv2.COLOR_BGR2RGB)

    # 5. Convert to Base64
    pil_img = Image.fromarray(superimposed_rgb)
    buffered = BytesIO()
    pil_img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")

    return {
        "success": True,
        "primary_prediction": top_3_predictions[0]["name"],
        "primary_confidence": top_3_predictions[0]["confidence"],
        "risk_level": risk_level,
        "top_3": top_3_predictions,  # <--- Now sending the top 3!
        "heatmap_base64": img_str
    }