
from tkinter import *    
from os import listdir   
import os
from tkinter.filedialog import *

from tkinter import ttk

root = Tk()
root.title=("Recipe Book")

mainframe = ttk.Frame(root, padding="8 8 10 10")
mainframe.grid(column=0, row=0, sticky=(N, E, W, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

class Application(Frame):
	def __init__(self):
		self.radioButtonVariable = StringVar()
		self.servePeopleNumber = StringVar() #How many served? 
		self.numberOfIngredients = StringVar()  #amount for user
		self.recipeName = StringVar() #recipe's name 	
		self.directory = os.path.dirname(os.path.realpath(__file__)) + "/recipes/"
		self.newServePeopleNumber = StringVar() #Recalculate for how many?
	def startPage(self):
		for child in mainframe.winfo_children(): child.grid_forget()
		ttk.Label(mainframe, text="What do you want to do?").grid(column=1, row=1)
		ttk.Radiobutton(mainframe, text="Add a new Recipe", variable=self.radioButtonVariable, value="add").grid(column=1, row=2)
		ttk.Radiobutton(mainframe, text="View and modify a recipe", variable=self.radioButtonVariable, value="edit").grid(column=1, row=3)
		ttk.Radiobutton(mainframe, text="Exit", variable=self.radioButtonVariable, value="exit").grid(column=1, row=4)
		ttk.Button(mainframe, text="Next", command=self.startPageProcess).grid(column=1, row=5)

	def startPageProcess(self):
		if self.radioButtonVariable.get() == "add":
			print ("Add")
			self.addRecipe()
		elif self.radioButtonVariable.get() == "edit":
			print ("Edit")
			self.recipeEdit()
		else:
			root.destroy()
	def addRecipe(self):
		for child in mainframe.winfo_children(): child.grid_forget()
		ttk.Label(mainframe, text="How many people will this recipe serve?").grid(column=1, row=1, sticky=(E, W))
		ttk.Entry(mainframe, textvariable=self.servePeopleNumber).grid(column=1, row=2, sticky=(S, E))
		ttk.Button(mainframe, text="Next", command=self.enterNumberOfIngredients).grid(column=2, row=2, sticky=W)
		
	def enterNumberOfIngredients(self):
		for child in mainframe.winfo_children(): child.grid_forget()
		ttk.Label(mainframe, text="How many ingredients will you be inoutting?").grid(column=1, row=1)
		ttk.Entry(mainframe, textvariable=self.numberOfIngredients).grid(column=1, row=2)
		ttk.Button(mainframe, text="Next", command=self.enterIngredients).grid(column=2, row=2)
	def enterIngredients(self):
		for child in mainframe.winfo_children(): child.grid_forget()
		ttk.Label(mainframe, text="What will this recipe be called?").grid(column=1, row=1, sticky=(E, W))
		ttk.Entry(mainframe, textvariable=self.recipeName).grid(column=1, row=2, sticky=(N, W))
		ttk.Label(mainframe, text="Enter your ingredient, press TAB, \nthen enter the Quantity followed\nby the Units. Enter each new ingredient\nand Quantity on a new line\n\nFor Example:\nFlour\t200g").grid(column=1, row=3, sticky=(N, E, W, S))
		self.textBox = Text(mainframe, width=16, height=self.numberOfIngredients.get())
		self.textBox.grid(column=1, row=4, sticky=(N, W, E, S))
		ttk.Button(mainframe, text="Submit", command=self.writeIngredients).grid(column=2, row=4, sticky=(S, W))

	def writeIngredients(self):
		recipeFileName = self.recipeName.get() + ".txt"
		ingredients = str(self.textBox.get('1.0', 'end'))
		filePath = self.directory + recipeFileName
		fileSaveTo = open(filePath, "w")
		fileSaveTo.write(ingredients)
		fileSaveTo.write("\nThis Recipe Serves "+self.servePeopleNumber.get()+" people")
		fileSaveTo.write("\nThis Recipe has "+str(self.numberOfIngredients.get())+" ingredients")
		fileSaveTo.close()
		self.startPage()
	def recipeNumberOfPeople(self):
		pass
	
	def recipeEdit(self):
		for child in mainframe.winfo_children(): child.grid_forget()
		global fileSelected
		fileSelected = askopenfile(mode="r", title="Chosse recipe", filetypes=[("Recipe Files",".txt")])
		ttk.Label(mainframe, text="What would you like to do?").grid(column=2, row=1)
		ttk.Button(mainframe, text="View Recipe", command=self.viewRecipe).grid(column=1, row=2, sticky=E)
		ttk.Button(mainframe, text="Edit Recipe", command=self.editRecipeServes).grid(column=3, row=2, sticky=W)
		
	def viewRecipe(self):
		for child in mainframe.winfo_children(): child.grid_forget()
		recipeContents = Text(mainframe)
		recipeFile=open(fileSelected.name, 'r')
		recipeContents.insert(END, recipeFile.read())
		recipeContents.grid(column=1, row=1, sticky=(N,W,E,S))
		ttk.Button(mainframe, text="Back", command=self.recipeEdit).grid(column=1, row=2, sticky=W)
		


	def editRecipeServes(self):
		for child in mainframe.winfo_children(): child.grid_forget()
		recipeFile = open(fileSelected.name)	#finds line "Serves" is on
		i = 1
		lines = recipeFile.readlines()
		global servePeopleNumber
		global ingredientsNumber
		while True:			
			if "Serves" in lines[i]:
				print (lines, lines[i])	
				b = lines[i].split(" ", 5) #i = ("Serves", "2", people")
				print ("b:",b,"i:",i)
				servePeopleNumber = int(b[3]) #b[3] = num of ppl e.g. 3 
				print ("serve People Number:", servePeopleNumber)
				break
			i=i+1
		y = i + 1# y = line after serves so ings
		z = lines[y]	# z = This Recipe has 
		x = z.split(" ", 4)
		ingredientsNumber = int(x[3])
		print ("Ingredients Number", ingredientsNumber, "Serv Num:", servePeopleNumber)
		ttk.Label(mainframe, text="This recipe currently serves %s people\n How many do you want to\nrecalculate for?" % servePeopleNumber).grid(column=1, row=1)
		ttk.Entry(mainframe, textvariable=self.newServePeopleNumber).grid(column=1, row=2)
		ttk.Button(mainframe, text="Next", command=self.changePeopleServed).grid(column=2, row=2)
	
	def changePeopleServed(self):
		for child in mainframe.winfo_children(): child.grid_forget()
		global newFileName
		recipeFile = open(fileSelected.name, "r")
		i = fileSelected.name.split(".", 1) #i = ("lemons", "txt"
		newFileName = i[0] + "New" + ".txt"
		newRecipeFile = open(newFileName, 'w')
		recalculateNumber = int(self.newServePeopleNumber.get())/servePeopleNumber
		lines = recipeFile.readlines()
		i = 0
		while i != (ingredientsNumber):
			print (lines[i].split("\t", 1))	
			digitOnly = re.split('(\d+)',lines[i])
			print ("dig", digitOnly)
			k = 1 #digi = Lemon 200 g so K is array number
			print (digitOnly[k])
			while not digitOnly[k].isdigit(): #checks array part is a number
				print ("Not is dig")
				k=k+1
			newAmount = int(digitOnly[k])*recalculateNumber
			newRecipeFile.write(digitOnly[0]+str(newAmount)+digitOnly[2])
			
			i=i+1
		newRecipeFile.write("This Recipe Serves "+str(self.newServePeopleNumber.get())+" people\nThis Recipe has "+str(ingredientsNumber)+" ingredients")
		

		print (recalculateNumber)
		recipeFile.close()
		newRecipeFile.close()
		self.showNewRecipe()
		
	def showNewRecipe(self):
		for child in mainframe.winfo_children(): child.grid_forget()
		recipeContents = Text(mainframe)
		recipeContents.insert(END, open(newFileName).read())
		recipeContents.grid(column=1, row=1)
		ttk.Button(mainframe, text="Done", command=self.startPage).grid(column=1,row=2)
app = Application()
app.startPage()
root.mainloop()
