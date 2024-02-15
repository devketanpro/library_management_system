# Library Management System
CRUD operations for a library management system focusing on the borrowing process, including the management of book borrow records.

## Tech stack used:
- python 3.10
- django 5.0
- django rest framework
- sqlite

## Setup project locally:
- Install python v3.10.10.
- Setup virtual environment with this python version and activate it (optional).
- Go to the project directory in terminal.
- Install required python libraries by using below command: `pip install -r requirements.txt`
- Run the server by using this command: `python manage.py runserver`

## To access django admin site:
- Go to this url in browser `http://127.0.0.1:8000/admin/` and login with below credentials: username: `admin`, password: `admin`

## To get API documentation:
Implemented swagger for this purpose. You can access the swagger portal by using below url:
`http://127.0.0.1:8000/swagger/`

## Authentication and permissions:
- Used JWTAuthentication in all APIs.
- Only staff users can have access to the APIs as only librarian should have rights to create and manage books and records.
- You need to add authorisation token in header to use the APIs.
- You can get authorisation token from below api:
api: `http://127.0.0.1:8000/gettoken/`

payload: 
```
{
    "username": <username>,
    "password": <password>
}
```

You will get response like this if the payload is correct:
```
{
    "refresh": "<refresh_token>",
    "access": "<access_token>"
}
```
- Add the access_token in API header while calling any API, like below:
```
{
    "Authorization": "Bearer <access_token>"
}
```

- Access token can expire shortly. Use `refreshtoken` api to refresh access token, like below:
api: `http://127.0.0.1:8000/refreshtoken/`

payload: 
```
{
    "refresh": <refresh_token>
}
```
You will get response like this:
```
{
    "access": "<access_token>"
}
```
Now use this access token in header.

## Datebase information:
Used below database models:

- `Book` : Stores book informations like `title`, `author` and `quantity`.
- `BorrowRecord` : Stores borrow records. Having fields like: `book`, `borrower`, `borrow_date` and `return_date`.

## API information:
- This API is used to perform CRUD operations on books.
`http://127.0.0.1:8000/api/books`

You can also filter books like this:

`http://127.0.0.1:8000/api/books/?title=<book_title>&author=<author_name>`

- This API is used to perform CRUD operations on borrowing records.
`http://127.0.0.1:8000/api/borrow-records`

You can also filter borrowing records like this:

`http://127.0.0.1:8000/api/borrow-records/?book__title=<book_title>&book__author=<author_name>`

- Use below api to register a book as borrowed:
API: `http://127.0.0.1:8000/api/borrow-book/`

Method: `POST`

Payload:
```
{
    "book": <book_id>,
    "borrower": <borrower_id>
}
```

- Use below api to register a book as returned:
API: `http://127.0.0.1:8000/api/return-book/`

Method: `POST`

Payload:
```
{
    "book": <book_id>,
    "borrower": <borrower_id>
}
```
Check swagger endpoint for further informations.

