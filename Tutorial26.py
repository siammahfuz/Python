#File handling - working with file programmatically using python

f = open('firstFile.txt') #create a file pointer
content = f.read() #read the contents of the file
print(content) #Print the content of the file
f.close()
f = open("firstFile.txt", 'W') #Create a file pointer
f.write("This is a good boy")

#Modes of opening a file
#1. read mode - 'r' : read the content of the file
#2.Append mode - 'a' : add content to the end of the file
#3.Write mode - 'W' : clears the content of the file and writes content of the file
#4. Create mode - 'X' : Create the file and return error if the file already exists.


