from flask import Flask, render_template, request
import cv2
import numpy as np
from tensorflow.keras.models import load_model

# ---------------------------------------------------------
#Flask = Python ka use karke web app banane ka tareeqa
# 1. FLASK APP CREATE KARNA
# ---------------------------------------------------------
app = Flask(__name__)

# ---------------------------------------------------------
# 2. TRAINED MODEL LOAD KARO
# Ye trained CNN model (.h5 file) server start hotay hi load ho jata hai
# ---------------------------------------------------------
model = load_model("final_model_v10.h5")

# ---------------------------------------------------------
# 3. DISEASE CLASSES (exact same order jisme training hui)
# ---------------------------------------------------------
classes = ['akiec','bcc','bkl','df','mel','nv','vasc']

# ---------------------------------------------------------
# 4. HOME PAGE ROUTE (GET + POST)
# GET → sirf page show karega
# POST → image upload karega + prediction karega
# ---------------------------------------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    result = None   # initially koi result nahi

    # ------------ POST Request (Jab user image upload kare) ------------
    if request.method == "POST":
        file = request.files["image"]  # uploaded file read karo

        if file:  # agar file exist karti hai
            # ---------------------------------------------------------
            # 5. Uploaded image ko static/ folder mein save karo
            # Flask static folder se images easily serve hoti hain
            # ---------------------------------------------------------
            filepath = "static/" + file.filename
            file.save(filepath)

            # ---------------------------------------------------------
            # 6. IMAGE PREPROCESSING (same as training)
            # ---------------------------------------------------------

            img = cv2.imread(filepath)            
             # image load
            img = cv2.resize(img, (224,224))       
            # resize (224x224)
            img = img / 255.0                      
            # normalize (0-1)
            img = np.expand_dims(img, axis=0)      
            # shape → (1, 224, 224, 3)

            # ---------------------------------------------------------
            # 7. MODEL PREDICTION
            # predict() → 7 probabilities return karega
            # np.argmax() → highest probability ka index
            # ---------------------------------------------------------
            preds = model.predict(img)
            predicted_class = classes[np.argmax(preds)]
            confidence = float(np.max(preds))      # highest probability

            # ---------------------------------------------------------
            # 8. RESULT KO TEMPLATE MEIN SEND KARNA
            # ---------------------------------------------------------
            result = {
                "class": predicted_class,
                "confidence": round(confidence, 4),
                "image": filepath
            }

    # ---------------------------------------------------------
    # 9. PAGE RETURN KARO (index.html)
    # result agar None hai → empty page show hoga
    # ---------------------------------------------------------
    return render_template("index.html", result=result)

# ---------------------------------------------------------
# 10. FLASK SERVER START
# debug=True → code change par auto reload hota hai
# ---------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
