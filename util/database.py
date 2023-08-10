books_file = 'books.txt'



def add_book(name, author):    
    with open(books_file, 'a') as file:
        file.write(f'{name},{author},0\n')

def list_books():
    with open(books_file, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]
        books = [
            {'name': line[0], 'author': line[1], 'read': line[2]}
            for line in lines
        ]
    return books

def mark_as_read(name):
    books = list_books()
    for book in books:
        if book['name'] == name:
            book['read'] = '1'
    _save_all_books(books)
 

def delete_book(name):    
    books = list_books()
    for book in books:
        if book['name'] == name:
            books.remove(book)
    _save_all_books(books)
    

def _save_all_books(books):
    with open(books_file, 'w') as file:
       for book in books:
           file.write(f"{book['name']},{book['author']},{book['read']}\n")
           
           
           