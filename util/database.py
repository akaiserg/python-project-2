

from .database_connection import DatabaseConnection

books_file = 'data.db'



def create_book_table():
    with DatabaseConnection(books_file) as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')
        

def add_book(name, author):    
    with DatabaseConnection(books_file) as connection:
        cursor = connection.cursor()
        #cursor.execute(f'INSERT INTO books VALUES ("{name}", "{author}", 0)')
        cursor.execute(f'INSERT INTO books VALUES (?, ?, 0)',(name, author))    
    
    
def list_books():
    with DatabaseConnection(books_file) as connection:
        cursor = connection.cursor()    
        cursor.execute('Select * from books')
        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]  # [(name, author, read), (name, author, read)]
    
    connection.close()
    return books

def mark_as_read(name):
    with DatabaseConnection(books_file) as connection:
        cursor = connection.cursor()    
        cursor.execute(f'UPDATE books SET read=1 WHERE name=?',(name,))
    

def delete_book(name):    
    with DatabaseConnection(books_file) as connection:
        cursor = connection.cursor()    
        cursor.execute(f'DELETE FROM books WHERE name=?',(name,))
    