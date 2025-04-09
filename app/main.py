from fastapi import FastAPI
from app.routes import contacts

app = FastAPI()

app.include_router(contacts.router, prefix="/api")

# from slowapi import Limiter
# from slowapi.util import get_remote_address
# from fastapi import FastAPI

# limiter = Limiter(key_func=get_remote_address)
# app = FastAPI()

# @app.get("/me")
# @limiter.limit("5/minute")
# def me(current_user: User = Depends(get_current_user)):
#     return current_user

# import cloudinary
# import cloudinary.uploader

# cloudinary.config(
#     cloud_name="your_cloud_name",
#     api_key="your_api_key",
#     api_secret="your_api_secret"
# )

# @router.post("/users/avatar")
# def upload_avatar(file: UploadFile, current_user: User = Depends(get_current_user)):
#     result = cloudinary.uploader.upload(file.file, folder="avatars", public_id=f"{current_user.id}")
#     return {"avatar_url": result["secure_url"]}

# from fastapi.middleware.cors import CORSMiddleware

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # змінюйте на конкретні домени в продакшені
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )