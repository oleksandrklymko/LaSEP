from student import Student
from datetime import datetime, timedelta


class Library:

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Library, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.books = []
        self.borrowed_books = []

    def add_book(self, book):
        if book in self.books:
            return False
        self.books.append(book)
        return True

    def borrow_book(self, book, student, date=datetime.date(datetime.today())):
        if book in self.borrowed_books or student.credit >= 100:
            return False
        student.rented_books.append((book, date))
        student.credit += book.price
        self.borrowed_books.append(book)
        return True

    def accept_book_back(self, book, student):
        for rented_book, date in student.rented_books:
            if rented_book == book:
                self.borrowed_books.remove(book)
                student.rented_books.remove((rented_book, date))
                student.credit += book.price
                return True
        return False


    def show_all_debtors(self):
        for student in Student.students:
            if student.rented_books:
                books_that_not_returned_more_then_year = []
                for book in student.rented_books:
                    if datetime.date(datetime.now()) >= book[1] + timedelta(365):
                        books_that_not_returned_more_then_year.append(book[0])
                print(student, end=', ')
                if books_that_not_returned_more_then_year:
                    print(f"unreturned more then one year: {books_that_not_returned_more_then_year}", end=', ')
                print(f'amount of unreturned books: {len(student.rented_books)}, student credit: {student.credit}')


