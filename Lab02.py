# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 10:45:06 2023

@author: DELL
"""

class Book:
    IBAN = None
    Name = None
    Author = None
    Issued = None
    
    #@classmethod()
    def __init__(self,iban,name,author,issue):
        self.IBAN = iban
        self.Name=name
        self.Author= author
        self.IBAN= issue
    
    def iss_book(self):
        if(self.Issued):
            print("This Book cannot be issued as it is already issued")
        else:
            print("Book is free for issue")
            self.Issued=False
                
                
    def return_book(self):
        if(self.Issued):
            print("This Book is already issued")
            self.Issued=False
            

    def spilting(string):
        chunks=string.split(",")
        return (chunks[0],chunks[1],chunks[2],chunks[3])
        
    
        
    
lst=[]
BookList=[]
with open("books.txt","r") as f:
   book=f.readlines()
   for line in book:
       tokens = line.split(',')
       bk = Book(tokens[0],tokens[1],tokens[2],tokens[3])
       BookList.append(bk)



def addBook(iban,name,author):
    b1=Book(iban,name,author,0)
    BookList.append(b1)
    
def search_book(name):
    for i in BookList:
        if(i.Name==name):
            print("Your Book  is found \n")
            return i
            
addBook(1233, "Life","Qanbar")
print("The name of the Author is : ",BookList[-1].Author)
search_book("Life")

    
def show_books():
    for i in BookList:
        print(i.IBAN)
        print(i.Name)
        print(i.Author)
        print(i.Issued)
        
val=input()
if(val==1):
    addBook(10022,"Pakistan", "Khaki")
elif(val==2):
    search_book("Pakistan")
elif(val==3):
    show_books()
elif(val==4):
    BookList[1].iss_book()
elif(val==5):
    BookList[1].return_book()
#show_books()
BookList[0].return_book()
BookList[0].iss_book()


    