# 🛡️ Skin Secure: AI-Powered Dermatological Analysis

**Skin Secure** is a comprehensive full-stack healthcare application designed to provide accessible, AI-driven skin health assessments.

This project combines advanced **Deep Learning (ResNet50)** with a modern web architecture to offer:

- Real-time skin disease analysis
- Symptom tracking
- Explainable AI (Grad-CAM Heatmaps)
- Community-driven support system
- Secure authentication and user history tracking

Built specifically to bridge the gap between patients and limited dermatological resources, especially in the Pakistani healthcare context.

---

# 🎓 University Project Details

## Institution
**University of Gujrat**

## Team Members
- Huzaifa
- Sehrish
- Zaineb
- Ayesha

## Project Type
**Final Year Project (FYP)**

---

# 🚀 Live Demonstration

## Frontend (Streamlit)
**https://skinsecure.streamlit.app**

## Backend API (FastAPI)
**https://skin-secure-api-ufhov.ondigitalocean.app/**

---

# 🛠️ Tech Stack & Architecture

This project follows a professional decoupled architecture, ensuring scalability, maintainability, and security across three distinct layers.

## 1. Frontend (The User Experience)

### Streamlit
Used for:
- Interactive dashboard
- Real-time UI updates
- User authentication pages
- Detection workflow
- Community features
- Profile management

### Custom CSS
Implemented for:
- Professional UI/UX
- Dark-grey readability theme
- Responsive layout
- Modern healthcare branding
- Smooth visual consistency

## 2. Backend (The Engine)

### FastAPI
Used for:
- Handling API requests
- Authentication endpoints
- AI model inference
- Community CRUD operations
- User profile management

### TensorFlow
Used to power the ResNet50 Deep Learning Model for:
- Skin disease classification
- Medical image analysis
- Confidence score generation

### Git LFS
Used for managing and deploying:
- Large AI model files
- High-capacity assets (>200MB)

## 3. Database & Security (The Vault)

### Aiven MySQL
Used for storing:
- User profiles
- Scan history
- Community posts
- Comments
- Likes
- Medical detection logs

### JWT (JSON Web Tokens)
Used for:
- Secure login sessions
- Stateless authentication
- Protected backend routes
- Session persistence

### PyMySQL
Used as the secure connector between FastAPI and Cloud MySQL Database.

---

# ✨ Key Features

## 🔍 AI Skin Analysis
Upload skin images for real-time classification across multiple dermatological conditions.

## 🔥 Explainable AI (Grad-CAM)
Generates heatmaps showing exactly which areas influenced the AI’s decision.

## 📈 User Scan History
Track previous assessments and monitor skin changes over time.

## 👥 Community Hub
Users can share experiences, ask questions, and support others anonymously.

## 🔐 Secure Authentication
Professional-grade login system with encrypted password handling and JWT authentication.

---

# 💻 Local Setup

## Prerequisites

- Python 3.11.x
- MySQL Server (Local or Cloud)
- Git
- Git LFS

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/HuzaifaHassan23/Skin_Secure
cd Skin_Secure
```

### 2. Environment Configuration

Create a `.env` file inside the `Backend/` folder:

```toml
DATABASE_URL=mysql+pymysql://user:pass@localhost:3306/skin_secure
SECRET_KEY=your_secret_key_here
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Servers

### Terminal 1 — Backend

```bash
cd Backend
uvicorn api:app --reload
```

### Terminal 2 — Frontend

```bash
cd Frontend
streamlit run app.py
```

---

# 📸 Screenshots

<img width="1582" height="872" alt="main" src="https://github.com/user-attachments/assets/e096ceca-df1b-4b72-8c0c-91fe17146048" />

<img width="1706" height="878" alt="dash" src="https://github.com/user-attachments/assets/b583231a-8c40-480a-b79a-4542907e7d6c" />

<img width="1665" height="862" alt="result" src="https://github.com/user-attachments/assets/8e718852-e5e4-4560-b02e-a220d8f386e6" />

<img width="1630" height="866" alt="com" src="https://github.com/user-attachments/assets/d61db437-7e39-4495-8fd3-0114e74afcd3" />

<img width="1585" height="862" alt="prof" src="https://github.com/user-attachments/assets/455d6bf5-4e6d-4705-b86d-ddb048d75e18" />

---

# 📝 License

This project is developed as part of the academic curriculum at the University of Gujrat.

All rights reserved by the project authors.
