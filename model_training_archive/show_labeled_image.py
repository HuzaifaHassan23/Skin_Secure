import os
import pandas as pd
import cv2
import matplotlib.pyplot as plt

# -------------------------------------------------
# 1. MAIN DATASET FOLDER (jahan images + metadata hain)
# -------------------------------------------------
data_path = r"C:\Users\ITG LAB\Downloads\archive (1)"

# Metadata CSV ka complete path
metadata_path = os.path.join(data_path, "HAM10000_metadata.csv")

# -------------------------------------------------
# 2. METADATA LOAD KARO
# CSV file mein har image ki information hoti hai:
# image_id, diagnosis (dx), age, sex, etc.
# -------------------------------------------------
df = pd.read_csv(metadata_path)

# -------------------------------------------------
# 3. EK SAMPLE RECORD CHOOSE KARO
# Yahan hum dataset ki first row le rahe hain:
# - image_id : image ka file name (without .jpg)
# - dx : disease label
# -------------------------------------------------
sample_id = df.iloc[0]["image_id"]
sample_label = df.iloc[0]["dx"]

# -------------------------------------------------
# 4. IMAGE KA PATH CREATE KARNA
# "image_id" ke sath .jpg add karna hota hai.
# Hamari image folder: HAM10000_images_part_1
# -------------------------------------------------
img_path = os.path.join(data_path, "HAM10000_images_part_1", sample_id + ".jpg")

# -------------------------------------------------
# 5. IMAGE READ KARO (OpenCV BGR format mein read karta hai)
# -------------------------------------------------
img = cv2.imread(img_path)

# -------------------------------------------------
# 6. CHECK KARO KE IMAGE MILI HAI YA NAHI
# Agar None aaya → file missing
# -------------------------------------------------
if img is None:
    print("Image not found")
else:
    # -------------------------------------------------
    # 7. BGR → RGB CONVERT KARO
    # Matplotlib ko RGB format chahiye warna colors ulte dikhte hain
    # -------------------------------------------------
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # -------------------------------------------------
    # 8. IMAGE KO SHOW KARO
    # matplotlib se display + disease title
    # -------------------------------------------------
    plt.imshow(img)
    plt.title(f"Disease: {sample_label}")
    plt.axis("off")  # Axis numbers hide kar deta hai
    plt.show()
