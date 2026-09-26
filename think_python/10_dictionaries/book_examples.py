# 10.4. A collection of counters
# Suppose you are given a string and you want to count how many times each letter appears.
# A dictionary is a good tool for this job.

# The following function counts the number of times each letter appears in a string.
def value_counts(string):
    counter = {}
    for letter in string:
        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter] += 1
    return counter

# Each time through the loop, if letter is not in the dictionary, we create a new item with key letter and value 1.
# If letter is already in the dictionary we increment the value associated with letter.

counter = value_counts('brontosaurus')

for key in counter:
    print(key)

for value in counter.values():
    print(value)

for key in counter:
    value = counter[key]
    print(key, value)

# 10.5. Looping and dictionaries

counter = value_counts('banana')
for key in counter:
    print(key)

for value in counter.values():
    print(value)

for key in counter:
    value = counter[key]
    print(key, value)
