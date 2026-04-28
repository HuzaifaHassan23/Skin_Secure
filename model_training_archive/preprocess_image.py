import cv2
import matplotlib.pyplot as plt

# --------------------------------------------
# 1. IMAGE KA PATH SET KARO (yahaan ek sample image li gayi hai)
# --------------------------------------------
img_path = r"C:\Users\ITG LAB\Downloads\archive (1)\HAM10000_images_part_1\ISIC_0024306.jpg"

# --------------------------------------------
# 2. IMAGE READ KARO (OpenCV BGR format mein image read karta hai)
# --------------------------------------------
img = cv2.imread(img_path)

# --------------------------------------------
# 3. STEP 1: IMAGE RESIZE KARNA
# Target size (224x224) deep learning models ke liye standard hoti hai
# --------------------------------------------
resized = cv2.resize(img, (224, 224))

# --------------------------------------------
# 4. STEP 2: NORMALIZATION
# Pixel range 0–255 se convert karke 0–1 kar diya jata hai
# Yeh training ko fast aur stable banata hai
# --------------------------------------------
normalized = resized / 255.0

# --------------------------------------------
# 5. PRINT INFORMATION
# Original aur resized shape dekhne ke liye
# Normalized pixel range check karne ke liye
# --------------------------------------------
print("Original shape:", img.shape)
print("Resized shape:", resized.shape)
print("Normalized pixel range:", normalized.min(), "to", normalized.max())

# --------------------------------------------
# 6. ORIGINAL vs PREPROCESSED IMAGE DISPLAY
# OpenCV BGR format use karta hai → isliye RGB mein convert karna zaroori hai
# --------------------------------------------

# Original Image show
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # BGR → RGB
plt.title("Original")

# Resized + Normalized Image show
plt.subplot(1, 2, 2)
plt.imshow(normalized)   # Already normalized + RGB order correct
plt.title("Resized + Normalized")

# Display both images together
plt.show()
