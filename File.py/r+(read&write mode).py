f = open("File.py\Demo.txt", "r+")    # "r+" mode opens the file for both reading and writing.
f.write("hii")   # f.write("hii") writes "hii" at the beginning of the file (overwriting the first 3 characters).
print(f.read())
f.close()