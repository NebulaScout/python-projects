#!python3
# tablePrinter.py - creates a well organised table

''' A function named printTable() takes a list of list of strings and displays\ 
it in a well organized table with each each column right-justified.'''

def printTable(table):
	# Initializes a list containing the same number of values as the inner list of the tableData
	colWidths = [0] * len(table)

	# finds the word with the longest string 
	for i, string in enumerate(table):
		width =len(max(string, key=len))
		colWidths[i] = width # stores the length of the string

	for row in zip(*table): # aggregates the lists to form rows
		# aligns the data to the right per the values in colWidths
		for rAlign, datum in zip(colWidths, row):
	    		print(f"{datum:>{rAlign}}", end=' ')
		print()

tableData = [["apples", "oranges", "cherries", "banana"], 
	    	["Alice", "Bob", "Carol", "David"], 
	    	["dogs", "cats", "moose", "goose"]]

printTable(tableData)

