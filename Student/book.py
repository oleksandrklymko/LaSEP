from student import Student
from datetime import timedelta


class Book:
    books = []
    borrowed_books = []

    def __init__(self, author, title, genre, price):
        self.author = author
        self.title = title
        self.genre = genre
        self.price = price
        self.number = len(Book.books) + 1
        Book.books.append(self)

    def __repr__(self):
        return self.title + ' by ' + self.author

    @classmethod
    def show_all_debtors(cls):
        for student in Student.students:
            if student.rented_books:
                for book in student.rented_books:
                    if book[1] <= book1[1] + timedelta(365):
                        print(student, student.rented_books, student.credit)


if __name__ == "__main__":
    book1 = Book('Mark L.', 'Learning Python 3-d edition', 'tech', 50)
    print(Book.books)
