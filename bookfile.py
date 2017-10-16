import csv


class Shelf:
	def __init__(self):
		sample = open("booklist.csv" , "r")
		csv1 = csv.reader("booklist", delimiter = ",")
		
		self.books = []
		
		for line in sample:
			eachline = line.rstrip("\n")
			self.books.append(eachline)
		
		print(self.books)
	
	def catalogue(self):
		print("Books currently available to borrow: ")
		print(self.books)
	
		
	def menu(self):
		print("\nSelect: ")
		print("1 to view Catalogue")
		print("2 to Borrow a book")
		print("3 to Return a book")
		print("4 to exit")
	
	
	def borrowBook(self):
		print("\nBooks currently available to borrow:\n")
		print(self.books)
		
		check = input("\nwhat book do you want to borrow? ")
		if check in self.books:			 
			self.books.remove(check)
			
			with open("booklist.csv", "w") as output:
				output.write(str(self.books)+"\n")
			
			print("Written successfully")
			print("\nyou have successfully borrowed book")
			print("The following books are now available to borrow:\n ")
			print(self.books)
			
		else:
			print("Sorry that title is not avaiable")
			
			
	def returnBook(self):
		check = input("what book do you want to return? ")			 
		self.books.append(check)
		
		with open("booklist.csv", "w") as output:
			output.write(str(self.books)+"\n")
			print("\nyou have successfully returned the book")
			print("The following books are now available to borrow:\n ")
			print(self.books)
			
		
# #---------------------------------------

bookshelf = Shelf()

var = "0"
while var != "1":
	bookshelf.menu()

	option = input(" > ")
	if option == "1":
		bookshelf.catalogue()
	if option == "2":
		bookshelf.borrowBook()
	if option == "3":
		bookshelf.returnBook()
	elif option == "4":
		break
		
	continue
