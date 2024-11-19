# from fastapi import APIRouter, File, UploadFile, HTTPException
# from fastapi.responses import JSONResponse
# from app.utils.image_preprocessing import preprocess_image
# from app.models.image_model import predict_image

# router = APIRouter()

# @router.post("/api/imageclassification/")
# async def upload_image(file: UploadFile = File(...)):
#     try:
#         file_data = await file.read()
#         image_tensor = await preprocess_image(file_data)
#         prediction = predict_image(image_tensor)
#         return JSONResponse(content={"filename": file.filename, "prediction": prediction.tolist()})
#     except Exception as e:
#         raise HTTPException(status_code=500, detail="Prediction error: " + str(e))
