# cv2 (OpenCV): images ko read, process, aur manipulate karne ke liye use hota hai.
# matplotlib.pyplot: graphs aur images ko show karne ke liye use hota hai.

import cv2
import matplotlib.pyplot as plt

# ek sample image ka path diya hai
img_path = r"C:\Users\ITG LAB\Downloads\archive (1)\HAM10000_images_part_1\ISIC_0024306.jpg"

# cv2.imread() image ko load karta hai aur usay matrix (pixels) ki form mai store karta hai.
img = cv2.imread(img_path)

# check karo image loaded hui ya nahi
if img is None:
    # Agar image galat path ki wajah se load na ho, to ye warning print karega.
    print("Image not found, path check karo!")
else:
    # matplotlib se show karo
    # plt.imshow(...) → image ko show karta hai.
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    # plt.title("Sample Skin Image") → upar title likhta hai.
    plt.title("Sample Skin Image")
    # plt.axis("off") → axis numbers (x, y labels) hatata hai.
    plt.axis("off")
    # plt.show() → final image screen pe display karta hai.
    plt.show()








# OpenCV image ko BGR format mai read karta hai (Blue, Green, Red).
# Matplotlib RGB format use karta hai (Red, Green, Blue).
# cv2.cvtColor(img, cv2.COLOR_BGR2RGB) → BGR ko RGB mai convert kar raha hai.
