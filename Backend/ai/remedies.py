# A hard-coded dictionary mapping disease predictions to safe, actionable advice.
REMEDIES = {
    "Melanoma (High Risk)": {
        "action": "Seek Immediate Medical Attention",
        "description": "Melanoma is a serious form of skin cancer. We strongly recommend scheduling an appointment with a dermatologist immediately.",
        "home_care": "Do not scratch, pick, or apply harsh chemicals. Keep the area covered from direct sunlight."
    },
    "Basal Cell Carcinoma": {
        "action": "Consult a Dermatologist",
        "description": "BCC is a highly treatable form of skin cancer, but it requires professional medical removal.",
        "home_care": "Protect the area from UV rays using a physical barrier (clothing/bandage)."
    },
    "Actinic Keratoses": {
        "action": "Schedule a Checkup",
        "description": "These are pre-cancerous spots caused by sun damage. A doctor can easily freeze or treat them.",
        "home_care": "Apply broad-spectrum SPF 50+ daily. Moisturize the area with gentle creams."
    },
    "Benign Keratosis": {
        "action": "Monitor for Changes",
        "description": "This is typically a harmless, non-cancerous skin growth.",
        "home_care": "No medical treatment is strictly necessary unless it becomes irritated by clothing."
    },
    "Dermatofibroma": {
        "action": "Routine Monitoring",
        "description": "A common, harmless overgrowth of fibrous tissue.",
        "home_care": "If it becomes itchy, a mild over-the-counter hydrocortisone cream may help."
    },
    "Melanocytic Nevi": {
        "action": "Standard Monitoring",
        "description": "This is a normal mole. However, always watch for changes in the ABCDEs (Asymmetry, Border, Color, Diameter, Evolving).",
        "home_care": "Practice standard sun protection."
    },
    "Vascular Lesion": {
        "action": "Routine Monitoring",
        "description": "These are typically harmless marks caused by blood vessels.",
        "home_care": "Avoid physical trauma to the area to prevent bleeding."
    }
}

def get_remedy(prediction_name: str) -> dict:
    """Returns the remedy dictionary for a given prediction, or a safe default."""
    return REMEDIES.get(prediction_name, {
        "action": "Consult a Healthcare Professional",
        "description": "Please consult a doctor for a professional medical diagnosis.",
        "home_care": "Keep the area clean, dry, and protected from the sun."
    })