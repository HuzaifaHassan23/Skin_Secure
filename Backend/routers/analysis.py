import os
import uuid
import base64
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
from datetime import datetime
from pathlib import Path  # <--- Import Pathlib
from typing import List
# Local imports
import database, models, schemas
from Security.dependencies import get_current_user
from ai.predictor import analyze_skin_image
from ai.remedies import get_remedy

router = APIRouter(prefix="/analyze", tags=["Analysis"])

# PROPHYLAXIS: Create absolute paths based on where this router file is located!
# This ensures 'uploads' is ALWAYS created inside the 'Backend' folder.
BASE_DIR = Path(__file__).resolve().parent.parent
UPLOAD_DIR = BASE_DIR / "uploads" / "raw"
HEATMAP_DIR = BASE_DIR / "uploads" / "heatmaps"

# Create directories if they don't exist
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
HEATMAP_DIR.mkdir(parents=True, exist_ok=True)

# Main endpoint to handle analysis
@router.post("")
async def run_analysis(
    file: UploadFile = File(...),
    body_part: str = Form(...),
    symptoms: str = Form(...),  # Expecting a comma-separated string from Streamlit
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(database.get_db)
):
    # 1. Read the uploaded file
    image_bytes = await file.read()
    
    # 2. Run the AI Model!
    ai_result = analyze_skin_image(image_bytes)
    if "error" in ai_result:
        raise HTTPException(status_code=500, detail=ai_result["error"])

    # 3. Save Raw Image to disk
    # Use UUID to generate a random, unique filename
    unique_id = str(uuid.uuid4())
    raw_filename = f"{unique_id}.jpg"
    raw_path = str(UPLOAD_DIR / raw_filename)
    
    with open(raw_path, "wb") as f:
        f.write(image_bytes)

    # 4. Save Heatmap Image to disk
    heatmap_filename = f"heatmap_{unique_id}.png"
    heatmap_path = str(HEATMAP_DIR / heatmap_filename)
    
    # Decode base64 back to image bytes and save
    heatmap_bytes = base64.b64decode(ai_result["heatmap_base64"])
    with open(heatmap_path, "wb") as f:
        f.write(heatmap_bytes)

    # 5. Fetch Remedies
    remedy = get_remedy(ai_result["primary_prediction"])

    # 6. Save RELATIVE paths to MySQL (so the browser can read them!)
    db_raw_path = f"uploads/raw/{raw_filename}"
    db_heatmap_path = f"uploads/heatmaps/{heatmap_filename}"

    new_scan = models.Scan(
        user_id=current_user["user_id"],
        body_part=body_part,
        symptoms=symptoms,
        primary_prediction=ai_result["primary_prediction"],
        confidence=ai_result["primary_confidence"],
        risk_level=ai_result["risk_level"],
        raw_image_path=db_raw_path,      
        heatmap_path=db_heatmap_path     
    )
    
    db.add(new_scan)
    db.commit()
    db.refresh(new_scan)

    # 7. Return everything to Streamlit!
    return {
        "scan_id": new_scan.id,
        "prediction": ai_result["primary_prediction"],
        "confidence": ai_result["primary_confidence"],
        "risk_level": ai_result["risk_level"],
        "top_3": ai_result["top_3"],
        "remedies": remedy,
        # We send the base64 back directly so Streamlit can display it instantly without fetching it again
        "heatmap_base64": ai_result["heatmap_base64"] 
    }

# New endpoint to fetch user's scan history
@router.get("/history", response_model=List[schemas.ScanResponse])
async def get_scan_history(
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(database.get_db)
):
    scans = db.query(models.Scan)\
              .filter(models.Scan.user_id == current_user["user_id"])\
              .order_by(models.Scan.created_at.desc())\
              .all()
    return scans