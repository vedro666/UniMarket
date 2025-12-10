from fastapi import FastAPI
from config import settings

# Создаем приложение FastAPI
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Платформа для покупки и продажи товаров между студентами",
    docs_url="/docs",  # Swagger UI
    redoc_url="/redoc",  # ReDoc документация
)


@app.get("/")
async def root():
    return {
        "message": "Добро пожаловать в UniMarket!",
        "version": settings.VERSION,
        "docs": "/docs",
    }


@app.get("/health")
async def health_check():
    return {"status": "healthy", "project": settings.PROJECT_NAME}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,  # Автоперезагрузка при изменении кода
    )


@app.get("/about")
async def about():
    return {
        "project": "UniMarket",
        "description": "Студенческий маркетплейс",
        "author": "Ильяс",
    }
