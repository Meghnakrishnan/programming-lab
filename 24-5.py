'''create a class publisher (name).Derive class book from publisher with attribute
title and author.derive from book with
'''

class publisher:    #base classse is difined
    def __init__(self,pn):
        self.PublisherName=pn
class book(publisher):  #subclass book
    def __init__(self,pn,title,author):
        publisher.__init__(self,pn)
        self.Title=title
        self.Author=author
class python(book): #sub class python
    def __init__(self,pn,title,author,price,nopages):
        book.__init__(self,pn,title,author)
        self.Price=price
        self.no_pages=nopages
    def bookdetails(self):
        print("Name of publisher:",self.PublisherName)
        print("Title:",self.Title)
        print("Author:",self.Author)
        print("Number of pages:",self.no_pages)
        print("Price:",self.Price)

python_book=python("OReilly","Think python","Allen B Downey ","650","500")  #object
python_book.bookdetails()


'''output
Name of publisher: OReilly
Title: Think python
Author: Allen B Downey 
Number of pages: 500
Price: 650
'''
