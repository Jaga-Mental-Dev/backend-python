from fastapi import APIRouter, Form, HTTPException
from fastapi.responses import JSONResponse
from app.service.text_model import predict_text
from app.service.feedback_service import EmotionFeedbackAgent
from functools import lru_cache

router = APIRouter()

@lru_cache()
def get_feedback_agent():
    return EmotionFeedbackAgent()

@router.post("/api/emotion/")
async def classify_emotion(text: str = Form(...)):
    """
    Endpoint untuk klasifikasi emosi saja.
    """
    try:
        prediction_result = predict_text(text)
        return JSONResponse(
            content={
                "text": text,
                "label": prediction_result["label"]
            }
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

@router.post("/api/feedback/")
async def get_feedback(
    text: str = Form(...),
    emotion: str = Form(...)  
):
    """
    Endpoint untuk mendapatkan feedback berdasarkan teks dan emosi.
    """
    try:
        emotion_result = {
            "label": emotion,
            "probability": 1.0  
        }
        
        feedback_agent = get_feedback_agent()
        result = await feedback_agent.generate_feedback(
            text=text,
            emotion_result=emotion_result
        )
        
        return JSONResponse(
            content={
                "text": text,
                "feedback": result["feedback"]
            }
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

@router.post("/api/textclassification/")
async def classify_text(text: str = Form(...)):
    """
    Endpoint original yang menggabungkan klasifikasi dan feedback.
    """
    try:
        prediction_result = predict_text(text)
        
        feedback_agent = get_feedback_agent()
        result_with_feedback = await feedback_agent.generate_feedback(
            text=text,
            emotion_result=prediction_result
        )
        
        return JSONResponse(
            content={
                "text": text,
                "result": result_with_feedback
            }
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )