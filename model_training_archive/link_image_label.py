import os
import pandas as pd

# --------------------------------------------------------
# 1. DATASET FOLDER KA MAIN PATH
# Yahan "archive (1)" folder ke andar sari files hain
# --------------------------------------------------------
data_path = r"C:\Users\ITG LAB\Downloads\archive (1)"

# Metadata CSV ki location (image_id + disease labels)
metadata_path = os.path.join(data_path, "HAM10000_metadata.csv")

# --------------------------------------------------------
# 2. METADATA CSV FILE LOAD KARO
# Is CSV file mein har image ki information hoti hai:
# image_id, disease type (dx), age, sex, location, etc.
# --------------------------------------------------------
df = pd.read_csv(metadata_path)

# --------------------------------------------------------
# 3. SAMPLE DATA PRINT KARO
# head() → pehli 5 rows show karega
# Yeh check karne ke liye ke CSV theek load hui ya nahi
# --------------------------------------------------------
print(df.head())

# --------------------------------------------------------
# 4. EK RANDOM / SAMPLE RECORD LENA
# Yahan hum first row ka "image_id" aur "dx" (disease)
# dekh rahe hain
# --------------------------------------------------------
sample_id = df.iloc[0]["image_id"]    # pehla image_id
sample_label = df.iloc[0]["dx"]       # uska diagnosis label

# --------------------------------------------------------
# 5. IMAGE KA PATH BANANA
# dataset mein images folders "HAL10000_images_part_1" 
# aur "part_2" mein hote hain
# ".jpg" add karna zaroori hai kyun ke image_id ke sath extension nahi hoti
# --------------------------------------------------------
img_path = os.path.join(data_path, "HAM10000_images_part_1", sample_id + ".jpg")

# --------------------------------------------------------
# 6. INFO PRINT KARO
# Image path, label, aur exist() check karta hai ke image file maujood hai ya nahi
# --------------------------------------------------------
print(f"Sample Image: {img_path}")
print(f"Label: {sample_label}")
print("Image exists?", os.path.exists(img_path))
