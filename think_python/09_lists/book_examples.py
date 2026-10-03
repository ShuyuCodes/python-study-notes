# 9.0 Lists
# lists is one of Python's most useful built-in types
# objects
# what can happle when multiple variables refer to the same object

# 9.1. A list is a sequence
# Like a string, a list is a sequence of values. In a string, the values are characters; in a list, they can be any typle.
# The values in a list are called elements.

# The elements of a list don't have to be the same type. The following list contains a string, a float, an integer,
# and even another list.

t = ['spam', 2.0, 5, [10,20]]  # A list within another list is nested.


# 9.2. Lists are mutable
# Unlike strings, Lists are mutable

# 9.3. List slices

# 9.4. List operations

# 9.5. List methods

letters = 'abcd'
print(letters)

li_letters = list(letters)
print(li_letters)  # ['a', 'b', 'c', 'd']

print(type(li_letters))

# Method append add an element to the end of a list
li_letters.append('e')  # Unlike strings, Lists are mutable ['a', 'b', 'c', 'd', 'e']

print(li_letters)  # List is changed from previous code


li_letters_append = li_letters.append('e')
print(type(li_letters_append))  # NoneType
print(li_letters_append)  # None

# extend takes a list as an argument and appends all of the elements
li_letters.extend(['f', 'g'])
print(li_letters)  # List is changed from previous code
print('\n')

li_letters_extend = li_letters.extend(['e', 'f'])
print(li_letters_extend)  # None
print(type(li_letters_extend))  # NoneType

# pop method could remove an element if you know the index of the element
li_letters.pop(0)
print(li_letters)

# remove method could remove an element if you do not know the index of the element
li_letters.remove("b")
print(li_letters)

# 9.6. Lists and strings
# we can use list method to convert from a string to a list of characters

# to break a string into words, you can use the split method

s = 'pining for the fjords'
t = s.split()
print(t, '9.6. Lists and strings')

s_1 = 'ex-parrot'
t_1 = s_1.split('-')
print("t_1", t_1)

print('\n')
# join is a string method which can concatenate strings into a single string,
# you have to invoke it on the delimiter and pass the list as an argument

delimiter = ' '
s_2 = delimiter.join(t)
print("s_2", s_2)

# 9.7. Loop through a list
# we can use for loop
print('\n')
for word in s.split():
    print(word)

# 9.8.Sorting lists

# sorted is a built-in function that sorts the elements of a list
scramble = ['c', 'a', 'b']
print(sorted(scramble))  # ['a', 'b', 'c']
print(scramble)  # the list is not changed after using sorted method

print('\n')
text ="when+I+push+to+github+it+asked+for+my+user+name+for+github.com+and+also+password+for+whatever+I+inputed+what+should+I+fill+in"
l = text.split("+")
print(l)

print(" ".join(l), "\n\nIn the end when I entered my username of my github account and my generated PERSONAL ACCESS TOKEN as a password for it, it SUCCEEDED!!!")

# 9.9. Objects and values
print('\n')
a = 'banana'
b = 'banana'
print(a is b)  # True
# In this example, Python only created one string object, and both a and b refer to it.

# But when you create two lists, you get two objects
print('\n')
a = [1, 3, 3]
b = [1, 3, 3]
print(a is b)  # False

# 9.10. Aliasing

# The association of a variable with an object is called a reference
# There are two references to the same object
print('\n')
a = [1, 2, 3]
b = a
print(b is a)

# An object with more than one reference has more than one name, so we say the object is aliased.
# If the aliased object is mutable, changes made with one name affect the other.
print('\n')
b[0] = 5
print(a)  # [5, 2, 3]

# For immutable objects like strings, aliaaint is not as much of a problem.

# 9.11. List arguments


def pop_first(lst):
    return lst.pop(0)


letters = ['a', 'b', 'c']
pop_first(letters)

print(letters)  # ['b', 'c']

# In this example, the parameter lst and the variable letters are aliases for the same object

# Passing a reference to an object as an argument to a function creates a form of aliasing.
# If the function modifies the object, those changes persist after the function is done.

# 9.12. Making a word list

# We can use read to read the entire file into a string
# string = open('words.txt').read()
# len(string)
# 1016511

# 9.13. Debugging

# Note that most list methods modify the argument and return None. This is the opposite of the string methods,
# which return a new string and leave the original alone.

# 9.14. Glossary

"""
list: An object that contains a sequence of values.

element: One of the values in a list or other sequence.

nested list: A list that is an element of another list.

delimiter: A character or string used to indicate where a string should be split.

equivalent: Having the same value.

identical: Being the same object (which implies equivalence).

reference: The association between a variable and its value.

aliased: If there is more than one variable that refers to an object, the object is aliased.

attribute: One of the named values associated with an object.
"""
