class Book:
    def __init__(self,title,author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year_published}"


get_book = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
print(get_book)