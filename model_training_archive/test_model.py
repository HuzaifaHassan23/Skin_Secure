import cv2
import numpy as np
from tensorflow.keras.models import load_model

# --------------------------------------------------------
# 1. TRAINED MODEL LOAD KARO
# "final_model_v10.h5" aapka trained CNN model hai
# load_model() se model memory me load ho jata hai
# --------------------------------------------------------
model = load_model("final_model_v10.h5")

# --------------------------------------------------------
# 2. DISEASE CLASSES LIST
# Ye labels exactly wahi order me hone chahiye
# jisme model ko train kiya gaya tha.
# --------------------------------------------------------
classes = ['akiec','bcc','bkl','df','mel','nv','vasc']

# --------------------------------------------------------
# 3. EK SAMPLE IMAGE KA PATH
# Yahan pe HAM10000 dataset ki ek dermatology image li gayi hai.
# --------------------------------------------------------
img_path = r"C:\Users\ITG LAB\Downloads\archive (1)\HAM10000_images_part_1\ISIC_0024306.jpg"

# --------------------------------------------------------
# 4. IMAGE PREPROCESSING (VERY IMPORTANT)
# Deep learning model input ko specific format chahiye hota hai:
#  - correct size (224x224)
#  - normalized pixel values (0–255 → 0–1)
#  - batch dimension add karna (1,224,224,3)
# --------------------------------------------------------

# Step 1: image load
img = cv2.imread(img_path)

# Step 2: resize image (model input size)
img = cv2.resize(img, (224,224))

# Step 3: normalize (pixel range 0–1)
img = img / 255.0

# Step 4: batch dimension add karna (model expects 4D input)
img = np.expand_dims(img, axis=0)  # shape becomes (1,224,224,3)

# --------------------------------------------------------
# 5. MODEL PREDICTION
# model.predict(img) → probabilities return karta hai
# Example: [0.1, 0.05, 0.7, 0.02, 0.01, 0.1, 0.02]
# --------------------------------------------------------
preds = model.predict(img)

# --------------------------------------------------------
# 6. MAX PROBABILITY INDEX
# np.argmax(preds) → jis class ki probability highest hogi
# Uska index return karega
# --------------------------------------------------------
predicted_class = classes[np.argmax(preds)]

# --------------------------------------------------------
# 7. CONFIDENCE SCORE
# np.max(preds) → highest probability (0 se 1 ke beech)
# --------------------------------------------------------
confidence = np.max(preds)

# --------------------------------------------------------
# 8. RESULTS PRINT KARO
# --------------------------------------------------------
print("Predicted class:", predicted_class)
print("Confidence score:", confidence)
