# 📚 Book Management REST API using FastAPI

A beginner-friendly RESTful API built using **FastAPI and Python** to perform CRUD (Create, Read, Update, Delete) operations on a book catalogue. This project demonstrates API development, request validation, HTTP methods, status codes, exception handling and automatic API documentation.

<p align="center">

**Practical Assignment**

**Name:** Rishikesh Bhagat  
**Roll Number:** 49

</p>

---

## 🎯 Objective

To design and develop a REST API using FastAPI that enables clients to manage book records through standard HTTP methods. The application demonstrates how modern Python frameworks handle API routing, data validation, request processing and structured JSON responses.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| FastAPI | REST API framework |
| Pydantic | Request validation and data modelling |
| Uvicorn | ASGI development server |
| Swagger UI | Interactive API documentation |

## ✨ Features

- **Create Books:** Add new books to the catalogue.
- **Retrieve Books:** Fetch all books or a specific book using its ID.
- **Update Books:** Replace existing book information.
- **Delete Books:** Remove records from the catalogue.
- **Automatic ID Generation:** Assign unique identifiers to newly created books.
- **Data Validation:** Validate titles, authors and publication years using Pydantic.
- **Error Handling:** Return meaningful HTTP error responses.
- **Interactive Documentation:** Explore and test endpoints through Swagger UI.

## 📂 Project Structure

```text
Fast_API_BOOKS/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Rishi-314/Fast_API_BOOKS.git

cd Fast_API_BOOKS
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

If requirements.txt is not available:

```bash
pip install fastapi "uvicorn[standard]"
```

## 🚀 Running the Application

Start the FastAPI development server:

```bash
uvicorn main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

### Interactive API Documentation

FastAPI automatically generates Swagger UI documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

You can explore endpoints, provide request data and execute API operations directly through the browser.

## 🔗 API Endpoints

| HTTP Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome message |
| GET | `/books` | Retrieve all books |
| GET | `/books/{book_id}` | Retrieve a specific book |
| POST | `/books` | Create a new book |
| PUT | `/books/{book_id}` | Update an existing book |
| DELETE | `/books/{book_id}` | Delete a book |

## 📖 Example Data

The application starts with two sample books:

| ID | Title | Author | Publication Year |
|---|---|---|---|
| 1 | The Alchemist | Paulo Coelho | 1988 |
| 2 | Wings of Fire | A. P. J. Abdul Kalam | 1999 |

### Example: Create a Book

**POST** `/books`

Request Body:

```json
{
    "title": "Atomic Habits",
    "author": "James Clear",
    "publication_year": 2018
}
```

Response:

```json
{
    "id": 3,
    "title": "Atomic Habits",
    "author": "James Clear",
    "publication_year": 2018
}
```

### Example: Retrieve All Books

**GET** `/books`

Returns the complete collection of available books.

### Example: Retrieve a Specific Book

**GET** `/books/1`

Returns the book associated with ID 1.

### Example: Update a Book

**PUT** `/books/3`

```json
{
    "title": "Atomic Habits - Revised",
    "author": "James Clear",
    "publication_year": 2018
}
```

### Example: Delete a Book

**DELETE** `/books/3`

Removes the specified book and returns a confirmation response.

## ✅ Validation and Error Handling

Pydantic validates incoming request data according to the defined Book model.

| Validation Rule | Constraint |
|---|---|
| Title | 1–100 characters |
| Author | 1–80 characters |
| Publication Year | 1450–2100 |

### HTTP Status Codes

| Status Code | Meaning |
|---|---|
| 200 OK | Request completed successfully |
| 201 Created | New book created successfully |
| 404 Not Found | Requested book does not exist |
| 422 Unprocessable Entity | Request validation failed |

## 🗄️ Data Storage

This demonstration uses an in-memory Python dictionary to store book records.

**Note:** Data is temporary and resets whenever the application process restarts. A production implementation would typically use a persistent database such as PostgreSQL or MySQL.

## 🎓 Learning Outcomes

Through this practical, the following concepts are demonstrated:

1. Understanding REST architectural principles.
2. Creating API endpoints using FastAPI decorators.
3. Working with HTTP methods and JSON requests.
4. Defining data models using Pydantic.
5. Implementing CRUD functionality.
6. Handling exceptions and HTTP status codes.
7. Exploring APIs through automatically generated Swagger documentation.

## 📝 Conclusion

This project demonstrates the development of a functional REST API using FastAPI. The Book Management System implements essential CRUD operations while showcasing request validation, API routing, HTTP status codes and exception handling.

FastAPI simplifies backend development through Python type hints, Pydantic integration and automatic API documentation, making it an effective framework for building modern web services.

---

**Developed by:** Rishikesh Bhagat  
**Roll Number:** 49  
**Repository:** [Fast_API_BOOKS](https://github.com/Rishi-314/Fast_API_BOOKS)
