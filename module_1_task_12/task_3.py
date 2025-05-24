books = {
    "book1": {"title": "1984", "author": "George Orwell", "year": 1949},
    "book2": {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960}
}

for book_key, book_info in books.items():
    print(f"Title:  {book_info['title']}")
    print(f"Author: {book_info['author']}")
    print(f"Year:   {book_info['year']}")
