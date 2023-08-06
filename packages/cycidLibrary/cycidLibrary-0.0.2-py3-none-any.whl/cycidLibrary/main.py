from .modules import book,Library, reader


if __name__=="main":
    a=Library.Library("name")

    b=book.Book(20,"1984","George Orwell", 2000)
    print(b)
    a.add_book(b)
    a.print_books("all")