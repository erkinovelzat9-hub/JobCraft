from app.database import engine, Base
from app import models

def init_db():
    print(f"Подключаемся к базе данных: {engine.url.database}")
    print("Создаем таблицы в базе данных JobCraft...")
    Base.metadata.create_all(bind=engine)
    print("Таблицы успешно созданы!")

if __name__ == "__main__":
    init_db()