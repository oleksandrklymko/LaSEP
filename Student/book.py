class Book:
    book_id = 1

    def __init__(self, author, title, genre, price):
        self.author = author
        self.title = title
        self.genre = genre
        self.price = price
        self.book_id = self.__class__.book_id
        self.__class__.book_id += 1


    def __repr__(self):
        return self.title + ' by ' + self.author
