# train_model.py (Skin Secure Optimized Version)
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.utils import class_weight
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, GlobalAveragePooling2D, BatchNormalization
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau

# =========================
# 1. Load Dataset
# =========================

X = np.load("X.npy").astype(np.float32)
y = np.load("y.npy")

print("Dataset Loaded")
print("X shape:", X.shape)

# =========================
# 2. Train Test Split
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# =========================
# 3. Class Weights (Handle Imbalance)
# =========================

class_weights = class_weight.compute_class_weight(
    class_weight='balanced',
    classes=np.unique(y_train),
    y=y_train
)

class_weights = dict(enumerate(class_weights))

print("Class Weights:", class_weights)

# =========================
# 4. One Hot Encoding
# =========================

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# =========================
# 5. Preprocess Images
# =========================

X_test = preprocess_input(X_test)

# =========================
# 6. Data Augmentation
# =========================

datagen = ImageDataGenerator(
    preprocessing_function=preprocess_input,
    rotation_range=25,
    width_shift_range=0.1,
    height_shift_range=0.1,
    shear_range=0.1,
    zoom_range=0.2,
    horizontal_flip=True,
    brightness_range=[0.8,1.2]
)

# =========================
# 7. Load ResNet50
# =========================

base_model = ResNet50(
    weights="imagenet",
    include_top=False,
    input_shape=(224,224,3)
)

# Freeze most layers
for layer in base_model.layers[:140]:
    layer.trainable = False

for layer in base_model.layers[140:]:
    layer.trainable = True

# =========================
# 8. Build Model
# =========================

model = Sequential([
    base_model,
    GlobalAveragePooling2D(),
    BatchNormalization(),
    Dense(256, activation='relu'),
    Dropout(0.5),
    Dense(y_train.shape[1], activation='softmax')
])

# =========================
# 9. Compile Model
# =========================

model.compile(
    optimizer=Adam(learning_rate=0.0001),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model.summary()

# =========================
# 10. Callbacks
# =========================

checkpoint = ModelCheckpoint(
    "best_model_skin_secure.h5",
    monitor='val_accuracy',
    save_best_only=True,
    mode='max',
    verbose=1
)

early_stop = EarlyStopping(
    monitor='val_loss',
    patience=10,
    restore_best_weights=True
)

reduce_lr = ReduceLROnPlateau(
    monitor='val_loss',
    factor=0.3,
    patience=5,
    min_lr=1e-6
)

# =========================
# 11. Training
# =========================

batch_size = 32
steps_per_epoch = len(X_train)//batch_size

print("Training Started...")

history = model.fit(
    datagen.flow(X_train, y_train, batch_size=batch_size),
    steps_per_epoch=steps_per_epoch,
    validation_data=(X_test,y_test),
    epochs=50,
    class_weight=class_weights,
    callbacks=[checkpoint, early_stop, reduce_lr]
)

# =========================
# 12. Save Final Model
# =========================

model.save("final_skin_secure_model.h5")

print("Training Completed")