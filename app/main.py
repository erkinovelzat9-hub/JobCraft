
from fastapi import FastAPI, HTTPException, Depends, Response
from pydantic import BaseModel
from authx import AuthX, AuthXConfig
from database import engine, Base
import models

app = FastAPI()

# Настройки JWT
config = AuthXConfig(
    JWT_SECRET_KEY="your_secret_key",
    JWT_TOKEN_LOCATION=["cookies"],
    JWT_COOKIE_SECURE=False  # Для локальной разработки
)

auth = AuthX(config=config)
auth.handle_errors(app)


# Схема пользователя
class UserLoginSchema(BaseModel):
    username: str
    password: str


# Авторизация
@app.post("/login")
def login(creds: UserLoginSchema, response: Response):
    if creds.username == "test" and creds.password == "test":

        token = auth.create_access_token(uid="12345")

        # Сохраняем токен в CookieC:\Users\user\anaconda3\python.exe -u "c:\Users\user\Desktop\JobCraft_\main.py"
        auth.set_access_cookies(token, response)

        return {"message": "Успешная авторизация"}

    raise HTTPException(
        status_code=401,
        detail="Incorrect username or password"
    )


# Защищённый маршрут
@app.get(
    "/protected",
    dependencies=[Depends(auth.access_token_required)]
)
def protected():
    return {"message": "Доступ разрешён!"}

Base.metadata.create_all(engine)