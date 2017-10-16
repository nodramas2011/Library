import csv


class Shelf:
	def __init__(self):
		sample = open("booklist.csv" , "r")			#opens the csv file
		csv1 = csv.reader("booklist", delimiter = ",")		#reads the csv file
		
		self.books = []                      			#create empty list
		
		for line in sample:
			eachline = line.rstrip("\n") #list contains \n after each book when imported from file. this line strips the \n
			self.books.append(eachline)  # writes each book to the python list "self.books"
		
		print(self.books)
	
	def catalogue(self):				#prints the current catalogue of books available in csv file
		print("Books currently available to borrow: ")
		print(self.books)
	
		
	def menu(self):					# displays the menu in order navigate the program
		print("\nSelect: ")
		print("1 to view Catalogue")
		print("2 to Borrow a book")
		print("3 to Return a book")
		print("4 to exit")
	
	
	def borrowBook(self):						# allows user to see what books are available. 
		print("\nBooks currently available to borrow:\n")
		print(self.books)
		
		check = input("\nwhat book do you want to borrow? ")	# user input, choose what books he wants to borrow
		if check in self.books:			 		# check if the desired book is in list. 
			self.books.remove(check)      # if its in list, remove from list because user is borrowing and so is no longer available
			
			with open("booklist.csv", "w") as output:    # now write the updated list to csv file so that it remains current
				output.write(str(self.books)+"\n")
			
			print("\nyou have successfully borrowed book")
			print("The following books are now available to borrow:\n ")
			print(self.books)
			
		else:
			print("Sorry that title is not avaiable")
			
			
	def returnBook(self):
		check = input("what book do you want to return? ")			 
		self.books.append(check)  			    #write the name of the book being returned to the list "self.books"
		
		with open("booklist.csv", "w") as output:	# update the csv file by writing the updated list to the file.
			output.write(str(self.books)+"\n")
			print("\nyou have successfully returned the book")
			print("The following books are now available to borrow:\n ")
			print(self.books)
			
		
# #---------------------------------------

bookshelf = Shelf()

var = "0"			
while var != "1":		#keep loop open 
	bookshelf.menu()	# gives user the menu to choose activity

	option = input(" > ")
	if option == "1":
		bookshelf.catalogue()	#displays the current catalogue of books from the csv file
	if option == "2":
		bookshelf.borrowBook()	#calls on the method to allow user to borrow the book and update csv file
	if option == "3":
		bookshelf.returnBook() # calls on the method to allow user to return a book and update file
	elif option == "4":		# breaks out of the while loop, exiting the program
		break
		
	continue
