import sqlite3



class Database:

    def __init__(self,db):
        self.connection=sqlite3.connect(db)
        self.cursor=self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.connection.commit()


    def view(self):
        self.cursor.execute("SELECT * FROM book")
        rows=self.cursor.fetchall()
        return rows

    def add(self,title,author,year,isbn):     
        self.cursor.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
        self.connection.commit() 

    def search(self,title='',author='',year='',isbn=''):       
        self.cursor.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
        rows=self.cursor.fetchall()
        return rows

    def update(self,id,title,author,year,isbn):     
        self.cursor.execute("UPDATE book SET title=?, author=?, year=?, isbn=? where id=?",(title,author,year,isbn,id))
        self.connection.commit()
        

    def dele(self,id):   
        self.cursor.execute("DELETE FROM book WHERE id=?", (id,))
        self.connection.commit()

    def __del__(self):
        self.connection.close()
 



