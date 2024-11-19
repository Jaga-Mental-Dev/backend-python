from fastapi import APIRouter, Form, HTTPException
from fastapi.responses import JSONResponse
from app.service.text_model import predict_text

router = APIRouter()

@router.post("/api/textclassification/")
async def classify_text(text: str = Form(...)):
    try:  
        result = predict_text(text)
        return JSONResponse(content={"text": text, "result": result})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")
