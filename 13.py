# Define a class called Book
class Book:
    # Constructor to initialize book details
    def __init__(self, title, author, date):
        self.title = title
        self.author = author
        self.date = date

    # Method to display book information
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"date: {self.date}")

# Create book objects
book1 = Book("The Bravehearts PVC Stories", "Rachna Bisht Rawat", 2014)
book2 = Book("Attitude is Everything", "Jeff Keller", 1999)

# Display information of each book
print("Book 1 Details:")
book1.display_info()

print("\nBook 2 Details:")
book2.display_info()
