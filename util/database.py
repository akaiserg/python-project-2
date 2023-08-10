books = []



def add_book(name, author):
    books.append({'name': name, 'author': author, 'read': False})    

def list_books():
    return books

def mark_as_read(name):
    for book in books:
        if book['name'] == name:
            book['read'] = True

#def delete_book(name):
#    for book in books:
#        if book['name'] == name:
#            books.remove(book)

def delete_book(name):
    global books
    books = [book for book in books if book['name'] != name]
    

