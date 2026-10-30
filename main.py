"""Book Management REST API practical implementation using FastAPI.

Student Details:
- Name: Rishikesh Bhagat
- Roll No: 49
"""

from typing import Dict, List
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, field_validator

app = FastAPI(
    title="Book Management API",
    description="A simple REST API built with FastAPI.",
    version="1.0.0",
)


class BookBase(BaseModel):
    """Base schema for book data with validation rules."""

    title: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Book title (1-100 characters)",
        examples=["The Alchemist"],
    )
    author: str = Field(
        ...,
        min_length=1,
        max_length=80,
        description="Book author (1-80 characters)",
        examples=["Paulo Coelho"],
    )
    publication_year: int = Field(
        ...,
        ge=1450,
        le=2100,
        description="Publication year between 1450 and 2100",
        examples=[1988],
    )

    @field_validator("title", "author")
    @classmethod
    def validate_non_empty_string(cls, value: str) -> str:
        """Ensure title and author are not only whitespace."""
        trimmed = value.strip()
        if not trimmed:
            raise ValueError("Value cannot be blank or contain only whitespace.")
        return trimmed


class BookCreate(BookBase):
    """Schema for book creation and update requests."""

    pass


class Book(BookBase):
    """Schema for book response including automatically generated ID."""

    id: int = Field(..., description="Unique auto-generated identifier")


# In-memory storage for books
books_db: Dict[int, Book] = {}
_id_counter: int = 1


def _initialize_sample_data() -> None:
    """Pre-populate the in-memory database with initial books."""
    global _id_counter
    initial_books = [
        {
            "title": "The Alchemist",
            "author": "Paulo Coelho",
            "publication_year": 1988,
        },
        {
            "title": "Wings of Fire",
            "author": "A. P. J. Abdul Kalam",
            "publication_year": 1999,
        },
    ]
    for item in initial_books:
        book = Book(id=_id_counter, **item)
        books_db[_id_counter] = book
        _id_counter += 1


_initialize_sample_data()


@app.get(
    "/",
    status_code=status.HTTP_200_OK,
    summary="Root Welcome Endpoint",
    tags=["General"],
)
def read_root():
    """Return a friendly welcome message for the API."""
    return {"message": "Welcome to the Book Management API"}


@app.get(
    "/books",
    response_model=List[Book],
    status_code=status.HTTP_200_OK,
    summary="Retrieve all books",
    tags=["Books"],
)
def get_all_books():
    """Retrieve the full list of books currently stored."""
    return list(books_db.values())


@app.get(
    "/books/{book_id}",
    response_model=Book,
    status_code=status.HTTP_200_OK,
    summary="Retrieve one book by ID",
    tags=["Books"],
)
def get_book_by_id(book_id: int):
    """Retrieve a single book by its unique ID. Returns 404 if not found."""
    book = books_db.get(book_id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with ID {book_id} not found",
        )
    return book


@app.post(
    "/books",
    response_model=Book,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new book",
    tags=["Books"],
)
def create_book(payload: BookCreate):
    """Create a new book with automatic ID assignment and input validation."""
    global _id_counter
    new_book = Book(id=_id_counter, **payload.model_dump())
    books_db[_id_counter] = new_book
    _id_counter += 1
    return new_book


@app.put(
    "/books/{book_id}",
    response_model=Book,
    status_code=status.HTTP_200_OK,
    summary="Update an existing book",
    tags=["Books"],
)
def update_book(book_id: int, payload: BookCreate):
    """Update all fields of an existing book. Returns 404 if the book does not exist."""
    if book_id not in books_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with ID {book_id} not found",
        )
    updated_book = Book(id=book_id, **payload.model_dump())
    books_db[book_id] = updated_book
    return updated_book


@app.delete(
    "/books/{book_id}",
    status_code=status.HTTP_200_OK,
    summary="Delete a book",
    tags=["Books"],
)
def delete_book(book_id: int):
    """Delete a book by ID. Returns 404 if the book does not exist."""
    if book_id not in books_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with ID {book_id} not found",
        )
    del books_db[book_id]
    return {
        "message": f"Book with ID {book_id} has been deleted successfully",
        "deleted_id": book_id,
    }
