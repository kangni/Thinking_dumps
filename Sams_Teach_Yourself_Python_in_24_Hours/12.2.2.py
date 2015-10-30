class Book(InventoryItem):
    def __init__(self, title, description, price, format, author, store_id):
        super(Book, self).__init__(title=title,
                                   description=description,
                                   price=price,
                                   store_id=store_id)
        self.format = format
        self.author = author

    def __str__(self):
        book_line = "{title} by {author}".format(
            title = self.title,
            author = self.author)
        return book_line

    def __eq__(self, other):
        if self.title == other.title and self.author == other.author:
            return True
        else:
            return False

    def change_format(self, format):
        if not format:
            format = raw_input("Please give me the new format: ")
        self.format = format

    def change_author(self, author):
        if not author:
            author = raw_input("Please give me the new author: ")
        self.author = author
