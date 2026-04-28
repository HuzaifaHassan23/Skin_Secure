import os
import numpy as np
from tensorflow.keras.preprocessing import image
# LabelEncoder is ki class ko 0,1,2 ki from mai encoding k liya use karta hai
from sklearn.preprocessing import LabelEncoder
import cv2

# -----------------------------
# 1. SETTINGS
# -----------------------------
dataset_dir = "dataset"       
 # Main folder containing all class folders
img_size = (224, 224)         
 # Target size for all images (width, height)
X, y = [], []                 
 # Lists to store images and labels


# -----------------------------
# 2. READING ALL FOLDERS (CLASSES)
# -----------------------------
for folder in os.listdir(dataset_dir):
    folder_path = os.path.join(dataset_dir, folder)

    # Skip if not a folder
    if not os.path.isdir(folder_path):
        continue

    print(f"Loading images from: {folder}")

    # -----------------------------
    # 3. READING IMAGES INSIDE CLASS FOLDER
    # -----------------------------
    for img_name in os.listdir(folder_path):
        img_path = os.path.join(folder_path, img_name)

        try:
            # Read image using OpenCV
            img = cv2.imread(img_path)

            # Resize to desired size
            img = cv2.resize(img, img_size)

            # Add image data to X
            X.append(img)

            # Add label (folder name) to y
            y.append(folder)

        except Exception as e:
            # If any image gives an error, print the message
            print(f" Error loading {img_name}: {e}")


# -----------------------------
# 4. CONVERT TO NUMPY ARRAYS
# -----------------------------
X = np.array(X)
y = np.array(y)

print("✅ Dataset Loaded Successfully!")
print("X shape:", X.shape)             # (num_images, 224, 224, 3)
print("y shape:", y.shape)             # (num_images,)
print("Classes:", np.unique(y))        # All unique classes


# -----------------------------
# 5. ENCODE LABELS TO NUMBERS
# -----------------------------
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y) 
  # Convert Class A -> 0, Class B -> 1, etc.


# -----------------------------
# 6. SAVE DATA AS .NPY FILES
# -----------------------------
np.save("X.npy", X)
np.save("y.npy", y_encoded)

print("✅ Saved X.npy and y.npy")
