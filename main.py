from fastapi import FastAPI
import uvicorn
from routes import book_routes, report_routes

app = FastAPI()
app.include_router(book_routes.router, prefix="/books")
app.include_router(report_routes.router, prefix="/reports")



if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
