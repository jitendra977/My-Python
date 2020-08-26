class Library:
    def __init__(self, list, name):
        self.listBook = list
        self.name = name
        self.lendDict = {}

    def addBook(self, book):
        self.listBook.append(book)
        with open("listfile.txt","a") as f:
            f.write(book)

    def returnBook(self, book):
        self.lendDict.pop(book)

    def displayBook(self):
        print(f"we have following Book are available in our {self.name}")
        for book in self.listBook:
            print(book)

    def lendBook(self, book, user):
        if book not in self.lendDict.keys():
            self.lendDict.update({book: user})
            print("Your are register in database you can take book now ")
        else:
            print("book was already taken by ", self.lendDict[book])

    def reportBook(self):
        print(f"Avialable Book now ")

    def allBook(self):
        with open("listfile.txt") as f:
            text = f.read()
            print(text)


if __name__ == '__main__':
    library = Library(["python", "Rubby", "HTML", "Java", "SQL"], "NISHANA LIBRARY")
    while (True):
        print(f"welcome to {library.name} Enter your choice")
        print("1 Display Book\n2.Lend Book\n3.Add Book\n4Return Book \n5 All books Report")
        user_input = input()
        if user_input not in ["1", "2", "3", "4", "5"]:
            print("input valid input")
        else:
            user_input = int(user_input)
        if user_input == 1:
            library.displayBook()
        elif user_input == 2:
            book = input("Enter Name of Book ")
            user = input("Enter Your name")
            library.lendBook(user, book)
        elif user_input == 3:
            book = input("Enter the book name you want to add library")
            library.addBook(book)
            print(f"{book} has been added in {library.name}")
        elif user_input == 5:
            library.allBook()
        else:
            print("v")
