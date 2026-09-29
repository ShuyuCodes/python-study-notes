# 9.0 Lists
# lists is one of Python's most useful built-in types
# objects
# what can happle when multiple variables refer to the same object

# 9.1. A list is a sequence
# Like a string, a list is a sequence of values. In a string, the values are characters; in a list, they can be any typle.
# The values in a list are called elements.

# The elements of a list don't have to be the same type. The following list contains a string, a float, an integer,
# and even another list.

t = ['spam', 2.0, 5, [10,20]] # A list within another list is nested.




#9.8.Sorting lists

text ="when+I+push+to+github+it+asked+for+my+user+name+for+github.com+and+also+password+for+whatever+I+inputed+what+should+I+fill+in"
l = text.split("+")
print(l)

print(" ".join(l), "\n\nIn the end when I entered my username of my github account and my generated PERSONAL ACCESS TOKEN as a password for it, it SUCCEEDED!!!")
