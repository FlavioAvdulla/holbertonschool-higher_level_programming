class Book:

    def __init__(self, title, author, field, pages):

        self.title = title
        self.author = author
        self.field = field
        self.pages = pages
        self.current_page = 0

    def book_details(self):
        print(f"The title of the book is: {self.title}")
        print(f"The author of the book is: {self.author}")
        print(f"The field of the book is: {self.field}")
        print(f"The number of pages is: {self.pages}")

    def book_page(self, pages):
        self.current_page += pages
        if self.current_page > self.pages:
            self.current_page = self.pages
        return f"You are now on page {self.current_page} of {self.pages}"

book1 = Book("Break the law", "John", "Social", 300)
book1.book_details()
print(book1.book_page(50))