

# 11.3. Tuple assignment

d = {'one': 1, 'two': 2}
for key, value in d.items():
    print(key, '->', value)

# 11.5. Argument packing


# pack all arguments as a single argument
def mean(*args):
    return sum(args)/len(args)


print(mean(1, 3, 3, 1))

# unpack a tuple two multiple arguments
t = (7, 3)
# print(divmod(t))  # TypeError: divmod expected 2 arguments, got 1
print(divmod(*t))  # unpack a tuple into multiple arguments


def trimmed_mean(*args):
    trimmed = list(args)
    trimmed.remove(min(args))
    trimmed.remove(max(args))

    return mean(*trimmed)


print(mean(1, 2, 3, 10))
print(trimmed_mean(1, 2, 3, 10))

# 11.6. Zip

scores1 = [1, 2, 4, 5, 1, 5, 2]
scores2 = [5, 5, 2, 2, 5, 2, 3]

for pair in zip(scores1, scores2):
    print(pair)

wins = 0
for team1, team2 in zip(scores1, scores2):
    if team1 > team2:
        wins += 1

print(wins)

letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = range(1, len(letters) + 1)
letter_map = dict(zip(letters, numbers))

print(letter_map['a'])
print(letter_map['z'])

for index, element in enumerate('abc'):
    print(index, element)

# 11.7. Comparing and Sorting


def value_counts(string):
    counter = {}
    for letter in string:
        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter] += 1
    return counter


counter = value_counts('banana')
print(counter)

items = counter.items()
print(items)

print(sorted(items))


def second_element(t):
    """a function that takes a tuple and returns the second element"""
    return t[1]


sorted_items = sorted(items, key=second_element)
print(sorted_items)

t1 = ('b', 1)
print(second_element(t1))

print(sorted_items[-1])

print(max(items, key=second_element))

# 11.8. Inverting a dictionary

d = value_counts('parrot')
print(d)


def invert_dict(d):
    """This function takes a dictionary and returns its inverse as a new dictionary."""
    new = {}
    for key, value in d.items():
        if value not in new:
            new[value] = [key]
        else:
            new[value].append(key)
    return new


print(invert_dict(d))

# 11.9. Debugging
"""
Lists, dictionaries and tuples are data structures.
 In this chapter we are starting to see compound data structures,
  like lists of tuples, or dictionaries that contain tuples as keys and lists as values.
   Compound data structures are useful, but they are prone to errors caused when a data structure has the wrong type,
    size, or structure. 
"""

# 11.10. Glossary

"""
pack: Collect multiple arguments into a tuple.

unpack: Treat a tuple (or other sequence) as multiple arguments.

zip object: The result of calling the built-in function zip, can be used to loop through a sequence of tuples.

enumerate object: The result of calling the built-in function enumerate, can be used to loop through a sequence of tuples.

sort key: A value, or function that computes a value, used to sort the elements of a collection.

data structure: A collection of values, organized to perform certain operations efficiently.
"""
