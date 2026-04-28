# evaluate_model.py (FINAL VERSION)

import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.applications.resnet50 import preprocess_input
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# 1 Load Dataset
# =========================

X = np.load("X.npy").astype(np.float32)
y = np.load("y.npy")

print("Dataset Loaded")
print("Shape:", X.shape)

# =========================
# 2 Same Split as Training
# =========================

_, X_test, _, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# =========================
# 3 Preprocess
# =========================

X_test = preprocess_input(X_test)

# =========================
# 4 Load Model
# =========================

model = load_model("final_skin_secure_model.h5")

# =========================
# 5 Evaluate Model
# =========================

loss, accuracy = model.evaluate(
    X_test,
    to_categorical(y_test),
    verbose=1
)

print("\nModel Evaluation")
print("Loss     :", loss)
print("Accuracy :", accuracy)

# =========================
# 6 Predictions
# =========================

y_pred = model.predict(X_test)
y_pred_classes = np.argmax(y_pred, axis=1)

# =========================
# 7 Manual Accuracy
# =========================

manual_acc = accuracy_score(y_test, y_pred_classes)

print("\nManual Accuracy Calculation")
print("Accuracy =", manual_acc)

# =========================
# 8 Classification Report
# =========================

print("\nClassification Report")
print(classification_report(y_test, y_pred_classes))

# =========================
# 9 Confusion Matrix
# =========================

cm = confusion_matrix(y_test, y_pred_classes)

plt.figure(figsize=(8,6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()