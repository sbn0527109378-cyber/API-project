# Introduction Final Project

### Shlomo Baruch Noyfeld


#### Library System
#### This system will manage the library, you can create, delete, update books and members, and view their status

## command
#### docker run --name library_project -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=library_db -P 3306:3306 -d mysql:8


<br>

## Folder structure

# library-api/

    ├── main.py
    ├── database/
    │ ├── db_connection.py
    │ ├── book_db.py
    │ └── member_db.py
    ├── routes/
    │ ├── book_routes.py
    │ ├── member_routes.py
    │ └── report_routes.py
    ├── logs/
    │ └── app.log
    │
    ├── README.md
    ├── requirements.txt
    └── .gitignore

<br>


### Books `table` — fields
| field | type | comments
| :-----: | :----: | :---------------:
| **id** | INT | AUTO_INCREMENT PRIMARY KEY
| **title** |  VARCHAR(100) | NOT NULL
| **author** | VARCHAR(50) | NOT NULL
| **genre** | ENUM (Fiction, Non-Fiction, Science, History, Other)
| **is_available** | BOOLIAN | NOT NULL
| **borrowed_by_member_id** | INT

### Books `members` — fields

| field | type | comments
| :-----: | :----: | :---------------:
| **id** | INT | AUTO_INCREMENT PRIMARY KEY
| **name** | VARCHAR(50) | NOT NULL
| **email** | VARCHAR(50) | UNIQUE
| **is_active** | BOOLIAN
| **total_borrows** | INT | NOT NULL
<br>

## System rules

| Law | Subject | Rule |
| :----: | :----: | :----: |
| 1 | create book | the user send - title/author/genre — the system adds - `is_available=True`, `borrowed_by=NULL` |
| 2 | genre | must be - Fiction / Non-Fiction / Science / History / Other — Any other value returns an error. Verify both when adding - (POST) and updating - (PATCH) |
| 3 | create member | the user send name/email — system adds `is_active=True`, `total_borrows=0` |
| 4 | email | UNIQUE — if exsist returns an error |
| 5 | Inactive member | if `is_active=False` — You can't borrow a book. |
| 6 | Inactive book | You cannot borrow a book that has already been borrowed (`is_available=False`) |
| 7 | maximum books | A member cannot hold more than 3 books at a time |
| 8 | returns book |A book can only be returned if it is lent to the same friend who is returning it |

<br>

## Endpoints

### Books

| Method | Endpoint | Description |
| :----: | :----: | :----: |
| `POST` | `/books` | create_book |
| `GET` | `/books` | all_books |
| `GET` | `/books/{id}` | book_by_id |
| `PATCH` | `/books/{id}` | update_book |
| `PATCH` | `/books/{id}/borrow/{member_id}` |lending_book_to_member
| `PATCH` | `/books/{id}/return/{member_id}` | returns_book_from_member |

### Members

| Method | Endpoint | Description |
| :----: | :----: | :----: |
| `POST` | `/members` | create_member |
| `GET` | `/members` | all_members |
| `GET` | `/members/{id}` | member_by_id |
| `PATCH` | `/members/{id}` | update_member |
| `PATCH` | `/members/{id}/deactivate` | disabling_member |
| `PATCH` | `/members/{id}/activate` | member_activation |

### Reports

 Method | Endpoint | Description |
 :----:  | :----: | :-----:     |
 `GET`  | `/reports/summary` | general_report
 `GET`  | `/reports/books-by-genre` | books_by_genre
 `GET`  | `/reports/top-member` | most_active_member 


 <br>

## System flow
#### בקשת HTTP -> python FastAPI -> שאילתת SQL -> תגובת DB


## Running instructions
#### python -m venv venv -> venv\Scripts\activate
#### pip install requirements.py
#### docker run --name library_project -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=library_db -P 3306:3306 -d mysql:8
#### python main.py 