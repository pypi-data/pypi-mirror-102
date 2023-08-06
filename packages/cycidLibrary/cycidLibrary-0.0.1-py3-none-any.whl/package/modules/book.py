class Book:
    def __init__(self,id, name, author,year, status="lib"):
        self.id=id
        self.name=name
        self.author=author
        self.year=year
        self.status=status
    def __repr__(self):
        return f'{self.name} by {self.author} published in {self.year} in {self.status}'





