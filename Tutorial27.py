f = open('firstFile.txt')

#content = f.read(2)
#print(content)
#content = f.read(2)
line = f.readline()
print(line)


lines = f.readlines()
print(lines)
f.close()
