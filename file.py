#!/usr/bin/python3
import json


class Book:
    all_books = []
    deser_books = []
    def __init__(self, title, author, isbn, price, num_of_pages):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price
        self.num_of_pages = num_of_pages

        Book.all_books.append(self)

    @classmethod
    def serialize_books(cls, filename="momoa.json"):
        with open(filename, 'w') as file:
            json.dump([book.__dict__ for book in cls.all_books], file)

    @staticmethod
    def deserialize_books(filename="momoa.json"):
            with open(filename, 'r') as file:
                deser_books = json.load(file)
                return deser_books

book_1 = Book("Book Title 1", "John", "3423423", 34, 450)
Book.serialize_books()
Book.all_books = []
deser_books = Book.deserialize_books()

for book in deser_books:
    print(book)
