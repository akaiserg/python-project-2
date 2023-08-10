from util import database
from time import sleep
import os
# a add  l list r mark as read d delete q quit

USER_CHOICE = """
- 'a' to add a book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Enter your choice:"""
def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else: 
            print("Unknown Command")
        sleep(2)    
        os.system('clear')    
        user_input = input(USER_CHOICE)
            
def prompt_add_book():
    name = input('Enter the new book name: ')
    author = input('Enter the new book author: ')
    database.add_book(name,author)
    print('new book added.....')
    
    
def list_books():
    books = database.list_books()
    if len(books) > 0:        
        for book in books:
            read = 'YES' if book['read'] == '1' else 'NO'
            print(f' name: {book["name"]}, author {book["author"]}, read {read}. \n')
    else:
        print('there is not books saved.')

def prompt_read_book():
    name = input('Enter the book name: ')
    database.mark_as_read(name)

def prompt_delete_book():
    name = input('Enter the name of the book to delete: ')
    database.delete_book(name)

menu()