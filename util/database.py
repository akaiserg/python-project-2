import json


books_file = 'books.json'



def add_book(name, author):    
    books = list_books()
    books.append({'name': name, 'author': author, 'read': False})
    _save_all_books(books)
    
def list_books():
    with open(books_file, 'r') as file:
        return json.load(file)

def mark_as_read(name):
    books = list_books()
    for book in books:
        if book['name'] == name:
            book['read'] = True
    _save_all_books(books)
 

def delete_book(name):    
    books = list_books()
    for book in books:
        if book['name'] == name:
            books.remove(book)
    _save_all_books(books)
    

def _save_all_books(books):
    with open(books_file, 'w') as file:
       json.dump(books, file)
           
           
           