from tkinter import *
from tkinter import messagebox
def onclick():
   pass

root = Tk()
text = Text(root)
text.pack()

def helloCallBack():
	value=str(text.get(1.0,END))

	singleQ = singleQuotaiton(value)
	text.delete(1.0,END)
	text.insert(INSERT,singleQ)
	# messagebox.showinfo( "Hello Python", singleQ)

def singleQuotaiton(val):
	arr = val.split('\n');
	rVal = ''
	for i,x in enumerate(arr):
		if i == 0:
			rVal = rVal + "'"+x+"'\n"
		else:
			rVal = rVal + ",'"+x+"'\n"
	return rVal

def logCallBack():
	value=str(text.get(1.0,END))

	returnVal = logBuild(value)
	text.delete(1.0,END)
	text.insert(INSERT,returnVal)
	# messagebox.showinfo( "Hello Python", singleQ)

def logBuild(a):
	toIdx = 0

	fromText = "parameter value ["
	toText = "]"

	replaceText = "?"

	paramCount = a.count("?")
	paramArr = [];

	while len(paramArr) != a.count("?"):
	  fromIdx = a.find(fromText,toIdx)
	  fromIdxEnd = fromIdx + len(fromText)
	  toIdx = a.find(toText,fromIdxEnd)
	  param = a[fromIdxEnd:toIdx]
	  paramArr.append(param)

	prevIdx = 0
	idx=0
	result = ""
	for val in paramArr:
	  idx = a.find("?",prevIdx+1)
	  result = result + a[prevIdx+1:idx] + "'"+val+"'"
	  prevIdx = idx
	result = result + a[idx+1:]

	excFromText = "Executing prepared SQL statement ["
	excToText = """]
	["""
	excFromIdx = result.find(excFromText)
	excFromIdxEnd = excFromIdx + len(excFromText)
	excToIdx = result.find(excToText,excFromIdxEnd)
	resultQuery = result[excFromIdxEnd:excToIdx]
	return resultQuery


B = Button(root, text ="SingleQ", command = helloCallBack) #Submit button
B.pack() #create Submit button

B2 = Button(root, text ="LogBuild", command = logCallBack) #Submit button
B2.pack() #create Submit button

root.mainloop()