Recipe Book
======

A simple(ish) recipe book program that allows a user to create recipes, store recipes as .txt files, view recipe files, and recalculate the recipe for more or less people


###Problems
The code doesn't create a recipe folder but assumes there is one so if any write errors are experianced. This is because it was written on a restricted computer. To fix this, create a folder called 'recipes' in the directory the program is in

#Requirements
- Python
- Tkinter
- Regex module

##Windows
This was written for Windows so it should run fine


##Mac OS X
The program works on Mac OS X tested on Mountain Lion 10.9 with a few modifications:

1) Change the first line<br>
		<code>from tkinter import * </code> to<br>
		<code>from Tkinter import * </code>
		
2) Change the line<br>
		<code>from tkinter import ttk </code> to<br>
		<code>import ttk</code>
		
		
##Linux
Untested, should in theory work the same as Mac OS X
		
