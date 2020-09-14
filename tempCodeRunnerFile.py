
        self.lendDict.pop(book)

    def displayBook(self):
        print(f"we have following Book are available in our {self.name}")
        for book in self.listBook:
            print(book)