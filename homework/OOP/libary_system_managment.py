class Item:
    def __init__(self, item, year):
        self.item = item
        self.year = year
    def __str__(self):
        return f'Имя предмета: "{self.item}". \nГод: {self.year}. \n'
        

class Book(Item):
    def __init__(self, item, year, author, pages):
        super().__init__(item, year)
        self.author = author
        self.pages = pages
        
    def __str__(self):
        tmp = super().__str__()
        return f'{tmp}Автор: "{self.author}". \nСтраниц: {self.pages}. \n'

class Magazine(Book):
    def __init__(self, item, year, author, pages, issue, publisher):
        super().__init__(item, year, author, pages)
        self.issue = issue
        self.publisher = publisher
        
    def __str__(self):
        tmp = super().__str__()
        return f'{tmp}Номер: {self.issue}. \nИздатель: "{self.publisher}". \n'
print(Magazine('Математика', 1991, 'Дерягин П. А.', 337, 7, 'Питер'))