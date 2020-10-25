from book import Book
from student import Student
from datetime import datetime, timedelta


class Library:
    # __instance = None
    #
    # def __new__(cls, *args, **kwargs):
    #     if not isinstance(cls.__instance, cls):
    #         cls.__instance = super(Library, cls).__new__(cls)

    def __init__(self):
        self.books = Book.books
        self.borrowed_books = []

    def borrow_book(self, book, student, date=datetime.date(datetime.today())):
        if book in self.borrowed_books or student.credit >= 100:
            return False
        student.rented_books.append((book, date))
        student.credit += book.price
        self.borrowed_books.append((book, date))
        return True

    def accept_book_back(self, book, student):
        if book in student.rented_books:
            student.rented_books.remove(book)
            student.credit -= book.price
            self.borrowed_books.remove(book)

    def show_all_debtors(self):
        for student in Student.students:
            if student.rented_books:
                for book in student.rented_books:
                    if datetime.date(datetime.now()) >= book[1] + timedelta(365):
                        print(f"Student - {student}, Book - {book[0]}, Student credit - {student.credit}")
