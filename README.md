This is a Django REST Framework-based API for managing books, book rentals, and user authentication using JWT. It includes CRUD operations for books, a rental system ensuring one book per user at a time, pagination, filtering, and file upload for book covers.

Features

Authentication: JWT-based authentication for secure access

Book Management: CRUD operations for books

Book Rentals & Returns:

A book can only be rented once at a time

A user can rent only one book at a time

Users must return a book before renting another

Pagination & Filtering: Applied to book listing and rental records

File Upload: Support for book cover images

Installation

Prerequisites

Python 3.x

Django & Django REST Framework

PostgreSQL (or SQLite for development)
