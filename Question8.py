#   WAP to enter marks of 3 subjects from the user and store them in a dictionary. 
#   Start with an empty dictionary & and add one by one. User subjects name ass key & marks as value.

marks = {}

x = int(input("Enter your maths marks : "))
marks.update({"maths" : x})

x = int(input("Enter your phy marks : "))
marks.update({"phy" : x})

x = int(input("Enter your chem marks : "))
marks.update({"chem" : x})

print(marks)