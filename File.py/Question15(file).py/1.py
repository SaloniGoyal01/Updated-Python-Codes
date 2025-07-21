#  Create a new file "practice.txt" using python. Add the following data in it:
#  Hi everyone
#  we are learning File I/O
#  using Java.
#  I like programming in Java.


# f = open("File.py/Question15(file).py/practice.txt", "w")
# f.write("Hi everyone \n we are learning File I/O \n using Java. \n I like programming in Java.")
# f.close()


#  WAP that replaces all occurrences of "java" with "python" in above file.

# with open("File.py/Question15(file).py/practice.txt", "r") as f :
#     data = f.read()

# new_data = data.replace("Java", "python")
# print(new_data)

# with open("File.py/Question15(file).py/practice.txt", "w") as f :
#     f.write(new_data)


#  Search if the word "learning" exists in the file or not

word = "learning"
with open("File.py/Question15(file).py/practice.txt", "r") as f :
    data = f.read()
    if(data.find(word) != -1):
        print("Found")
    else :
        print("not found")