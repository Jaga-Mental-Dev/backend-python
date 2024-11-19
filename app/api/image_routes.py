from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from app.service.image_model import predict_image

router = APIRouter()

@router.post("/api/imageclassification/")
async def classify_text(file: UploadFile = File(...)):
    try:
        result = predict_image(file)
        return JSONResponse(content={"filename": file.filename, "result": result})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")
