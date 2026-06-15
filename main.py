from fastapi import FastAPI
import uvicorn
from routes import book_routes, report_routes, member_routes
from database import db_connection

app = FastAPI()
app.include_router(book_routes.router, prefix="/books")
app.include_router(report_routes.router, prefix="/reports")
app.include_router(member_routes.router, prefix="/members")


if __name__ == "__main__":
    db_connection.create_tables_books_and_members()
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
