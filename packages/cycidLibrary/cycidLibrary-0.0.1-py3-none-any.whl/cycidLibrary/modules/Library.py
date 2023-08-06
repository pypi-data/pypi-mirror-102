
class Library:


    def __init__(self, name, list_of_books=None, list_of_readers=None):
        self.name=name
        self.list_of_books = []
        self.list_of_readers = []



    def __repr__(self):
        return f'{self.name}'


    def add_book(self, book):
        self.list_of_books.append(book)
        return f'book was added successful'


    def del_book(self, book):
        self.list_of_books.remove(book)
        return f'book was removed'



    def give_book_to_reader(self, book, reader):

        """
        the function change the status lib to status with reader
        status lib means the book is in library
        :param book: book object
        :param reader: reader object
        :return: message with operation
        """
        book_index=self.list_of_books.index(book)
        if self.list_of_books[book_index].status=="lib":
            self.list_of_books[book_index].status=reader
            return print(f'the book was given')
        else:
            return print(f'some one already took this book')



    def get_book_from_reader(self,book):
        """
        the func return book from any reader who had it

        """
        book_index=self.list_of_books.index(book)
        self.list_of_books[book_index].status="lib"
        return print(f'the book come back to library')

    def print_books(self,param):
        """the function return books in library depends on parameter

        :param param: could be "all", "in" mean in library, and "out" mean out of library
        :return:
        """
        if param=="all":
            for item in self.list_of_books:
                print(item)

                #iterating all list of books and if book is in library - print it
        elif param=="in":
            for item in self.list_of_books:
                if item.status=="lib":
                    print(item)
                else:pass
        else:
            for item in self.list_of_books:
                if item.status!="lib":
                    print(item)
                else:pass



    def sort(self,param):
        if param=="year":
            sorted_list=sorted(self.list_of_books, key=lambda item:item.year)
            for i in sorted_list:
                print(i)
        elif param=="name":
            sorted_list = sorted(self.list_of_books, key=lambda item: item.name)
            for i in sorted_list:
                print(i)
        elif param=="author":
            sorted_list = sorted(self.list_of_books, key=lambda item: item.author)
            for i in sorted_list:
                print(i)
        else:
            raise Exception("Sorry, keyword wasnt correct")
        return print("all the books in our library")

    def show_user_book(self,user):
        print(f"{user} have such books:")
        for item in self.list_of_books:
            if item.status==user:
                print(item)
            else:
                pass