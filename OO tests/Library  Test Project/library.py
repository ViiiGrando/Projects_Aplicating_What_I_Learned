from books import Books



def main():
 book1 = Books('Victor',  'Le Belle Donne', 2004, False)
 print(book1.borrow())
 print(book1)
 
if __name__ =='__main__':
    main() 