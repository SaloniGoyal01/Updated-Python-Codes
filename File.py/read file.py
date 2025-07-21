# f = open("File.py\Demo.txt", "r")
# data = f.read()            #  reads the entire content of the file at once and stores it in the variable data
# print(data)
# print(type(data))

# f = open("File.py\Demo.txt", "r")
# data = f.read(2)           # Read only the first 10 characters (or bytes) from the file.
# print(data)
# print(type(data))
# print(len(data))

# f = open("File.py\Demo.txt", "r")
# line1 = f.readline()            # reads only the first line from the file.
# print(line1)
# print(type(line1))




f = open("File.py\Demo.txt", "r")
line1 = f.readline()            # reads only the first line from the file.
print(line1)
line2 = f.readline()            # reads only the second line from the file.
print(line2)

f.close()



