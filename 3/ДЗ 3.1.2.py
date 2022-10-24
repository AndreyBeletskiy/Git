class Book:

    def __init__(self, author, name, year_of_publishing, genre):
        self.author = author
        self.name = name
        self.year_of_publishing = year_of_publishing
        self.genre = genre
        self.reviews = []

    def add_review(self, user, review):
        self.reviews.append(Review(user, review))

    def info_book(self):
        for info in (self.author, self.name, self.year_of_publishing, self.genre):
            print(info)
        for review in self.reviews:
            print(review)


class Review:

    def __init__(self, user, review):
        self.user = user
        self.review = review

    def __str__(self):
        return f'пользователь - {self.user}\nотзыв - {self.review}'


book_1 = Book("orwell", "1984", 2015, "fiction")
book_1.add_review("art_000", "life-changing")
book_1.add_review("maxXX", "is not a particularly good novel")
book_1.info_book()