
class LibraryIndex:
    def __init__(self):
        self.books = []
        self.index = []
        self.count = 0

    # Insert Book Record
    def InsertBook(self):
        bookID = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        # Assign record position
        position = self.count

        # Store book record
        book = {
            "bookID": bookID,
            "title": title,
            "author": author
        }

        self.books.append(book)

        # Store index information
        index_record = {
            "bookID": bookID,
            "position": position
        }

        self.index.append(index_record)

        # Increase record count
        self.count += 1

        print("Book added successfully")

    # Display Index
    def DisplayIndex(self):
        if self.count == 0:
            print("Index is empty")
            return

        print("\nBook ID\tPosition")

        for i in range(self.count):
            print(self.index[i]["bookID"],
                  "\t", self.index[i]["position"])

    # Search Book Record
    def SearchBook(self):
        searchID = int(input("Enter Book ID to search: "))

        found = False

        # Search the index
        for i in range(self.count):
            if self.index[i]["bookID"] == searchID:

                # Obtain record position
                position = self.index[i]["position"]

                # Retrieve book record
                print("\nBook ID:",
                      self.books[position]["bookID"])
                print("Title:",
                      self.books[position]["title"])
                print("Author:",
                      self.books[position]["author"])

                found = True
                break

        if found == False:
            print("Book not found")

    # Display All Books
    def DisplayBooks(self):
        if self.count == 0:
            print("No books available")
            return

        print("\nAll Book Records")

        for i in range(self.count):
            print("\nBook ID:", self.books[i]["bookID"])
            print("Title:", self.books[i]["title"])
            print("Author:", self.books[i]["author"])


# Main Function
library = LibraryIndex()

while True:
    print("\n===== LIBRARY BOOK INDEX MANAGEMENT =====")
    print("1. Insert Book")
    print("2. Display Index")
    print("3. Search Book")
    print("4. Display All Books")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        library.InsertBook()

    elif choice == 2:
        library.DisplayIndex()

    elif choice == 3:
        library.SearchBook()

    elif choice == 4:
        library.DisplayBooks()

    elif choice == 5:
        print("Program terminated")
        break

    else:
        print("Invalid choice")
