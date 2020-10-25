class Book:
    books = []

    def __init__(self, author, title, genre, price):
        self.author = author
        self.title = title
        self.genre = genre
        self.price = price
        self.number = len(Book.books) + 1
        Book.books.append(self)

    def __repr__(self):
        return self.title + ' by ' + self.author


if __name__ == "__main__":
    book1 = Book('Mark L.', 'Learning Python 3-d edition', 'tech', 50)
    print(Book.books)
