import book_examples as be

# 10.11. Exercises

# Because %xmode Verbose only works on IPython REPL, ultratb module reproduces the same effect as %xmode Verbose
# import sys
# from IPython.core import ultratb
#
# sys.excepthook = ultratb.FormattedTB(
#     mode='Verbose',
#     call_pdb='False'
# )

# 10.11.1. Ask a virtual assistant
"""
In this chapter, I said the keys in a dictionary have to be hashable and I gave a short explanation.
If you would like more details, ask a virtual assistant, “Why do keys in Python dictionaries have to be hashable?”

In a previous section, we stored a list of words as keys in a dictionary so that we could use an efficient version of the in operator.
We could have done the same thing using a set, which is another built-in data type. Ask a virtual assistant,
“How do I make a Python set from a list of strings and check whether a string is an element of the set?”
"""

# Why do keys in Python dictionaries have to be hashable?
"""
### Core idea

When you do `d[key] = value`:

1. Python calls `hash(key)` to get an integer, the **hash value**.
2. This integer is used to compute an index into the underlying table array.
3. It stores the (key, value) pair at that computed slot.
4. When you later look up `d[key]`, compute hash again to find the slot quickly.
"""

# 1. Create set from list of strings
string_list = ["apple", "banana", "orange"]
my_set = set(string_list)   # convert list to set
print(my_set)

# 2. Check if a string is inside the set: use `in` operator
# test membership
search_str = "banana"
if search_str in my_set:
    print(f"'{search_str}' is in the set")
else:
    print(f"'{search_str}' is NOT in the set")

"""
## What is a Python `set` (built‑in type)

A **set** is built‑in unordered collection.

- Stores **unique values**: duplicates get automatically discarded
- Mutable (you can add/remove elements)
- **Very fast membership test**: `in` operator
- Elements must be hashable (strings, numbers; cannot use lists as set items)
- No indexing: you cannot do `my_set[0]`, sets are unordered.
"""

# 1. Create a set from list of strings
""" 
string_list = ["apple", "banana", "orange", "apple"]
my_set = set(string_list)
print(my_set)
# duplicate "apple" only appears once in the set
"""

# Way 2: set literal curly braces `{ }`
# Cannot make empty set with `{}`, that is empty dict. Empty set needs `set()`.
# my_set = {"apple", "banana", "orange"}


# 10.11.2. Exercise

# functon in book_examples:
"""
def value_counts(string):
    counter = {}
    for letter in string:
        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter] += 1
    return counter
"""
"""
Dictionaries have a method called get that takes a key and a default value.
 If the key appears in the dictionary, get returns the corresponding value; 
 otherwise it returns the default value. For example, 
 here’s a dictionary that maps from the letters in a string to the number of times they appear.
"""
print('\n')
print('This is exercise 10.11.2')

counter = be.value_counts('brontosaurus')

print(counter.get('b', 0))
print(counter.get('o', 0))

# Use get to write a more concise version of value_counts. You should be able to eliminate the if statement.

print('\n')


def value_counts(string):
    counter = {}
    for letter in string:
        counter[letter] = counter.get(letter, 0) + 1
    return counter


counter2 = value_counts('brontosaurus')

print(counter2.get('b', 0))
print(counter2.get('o', 0))

# This is note for exercise 10.11.2
counter2 = {}
s = 'Shuyu'

for letter in s:
    counter2[letter] = counter2.get(letter, 0) + 1  # add 1 as keys value if key does not exist, and add 1 to value if key exists

print(counter2)

# --This is note for exercise 10.11.2

# 10.11.3. Exercise
"""
What is the longest word you can think of where each letter appears only once? 
Let’s see if we can find one longer than unpredictably.

Write a function named has_duplicates that takes a sequence – like a list or string – as a parameter 
and returns True if there is any element that appears in the sequence more than once.
"""
print('\n')
print('This is exercise 10.11.2')

def has_duplicates(items):
    """items: sequence like a list or a string"""
    count_dict = value_counts(items)
    re = 0
    for e in items:
        re += count_dict.get(e, 0)

    if re == len(items):
        return False
    else:
        return True


print("this is test part for exerciese 10.11.3")

# Case1: word with repeated letters → expect True
print(has_duplicates("hello"))
# 'l' occurs twice → True

# Case2: short all‑unique word → expect False
print(has_duplicates("abcde"))
# no repeated letters → False

# Case3: the example word from problem: "unpredictably"
print(has_duplicates("unpredictably"))
# check: does this word have all unique letters? Should return False

# Case4: list test, duplicate numbers
print(has_duplicates([1,2,3,2,4]))
# 2 repeats → True

# Case5: list with all unique values
print(has_duplicates([5,6,7,8]))
# no duplicates → False

# Case6: empty string edge case
print(has_duplicates(""))
# empty sequence, no duplicates → False

# Case7: single character
print(has_duplicates("z"))
# only one element → False



# This is note for exercise 10.11.3
print('this is note test for exercise 10.11.3')
s2 = 'avoid'
count_dict = value_counts(s2)

re = 0
for e in s2:
    re += count_dict.get(e, 0)

if re == len(s2):
    print("False")
else:
    print("True")

l = ['a', 'b', 'c', 'a']
count_dict = value_counts(l)

re = 0
for e in l:
    re += count_dict.get(e, 0)

if re == len(l):
    print("False")
else:
    print("True")

# --This is note for exercise 10.11.3

# 10.11.4. Exercise
"""
Write a function called find_repeats that takes a dictionary that maps from each key to a counter, 
like the result from value_counts.
  It should loop through the dictionary and return a list of keys that have counts greater than 1. 
  You can use the following outline to get started.
"""

print('\n')

print('this is note test for exercise 10.11.4')
# This is note for exercise 10.11.4

ct = value_counts('wofneioagnfeifnwlivurhfgywvqbca')
ls = []
for key in ct:
    if ct[key] > 1:
        ls.append(key)
print(ls)

# --This is note for exercise 10.11.4

print('\n')

print('this is exercise 10.11.4')
def find_repeats(counter):
    """Makes a list of keys with values greater than 1.

    counter: dictionary that maps from keys to counts

    returns: list of keys
    """
    ls = []
    for k in counter:
        if counter[k] > 1:
            ls.append(k)
    return ls


print("this is test part for exerciese 10.11.4")
# Test case 1: some repeated items
# source list
data1 = ["cat", "dog", "cat", "bird", "dog", "dog"]
counts1 = value_counts(data1)
print(counts1)
# {'cat':2, 'dog':3, 'bird':1}
print(find_repeats(counts1))
# expected output: ['cat', 'dog']

print('\n')
# Test case 2: no repeats at all (empty list return)
data2 = ["apple", "banana", "orange"]
counts2 = value_counts(data2)
print(find_repeats(counts2))
# expected output: []

print('\n')
# Test case3: only one element repeated many times
data3 = ["pen","pen","pen"]
counts3 = value_counts(data3)
print(find_repeats(counts3))
# expected output: ["pen"]

print('\n')
# Test case4: empty input dictionary, edge case
counts4 = {}
print(find_repeats(counts4))
# expected output: []

print('\n')
# Test case5: string as source data (value_counts on string characters)
data5 = "abracadabra"
counts5 = value_counts(data5)
print(find_repeats(counts5))
# expected: ['a','b','r']


print('\n')

# 10.11.5. Exercise
"""
Suppose you run value_counts with two different words and save the results in two dictionaries.

counter1 = value_counts('brontosaurus')
counter2 = value_counts('apatosaurus')
Each dictionary maps from a set of letters to the number of times they appear. 
Write a function called add_counters that takes two dictionaries like this 
and returns a new dictionary that contains all of the letters and the total number of times they appear in either word.

There are many ways to solve this problem. Once you have a working solution, 
consider asking a virtual assistant for different solutions.

"""

counter1 = value_counts('brontosaurus')
counter2 = value_counts('apatosaurus')

# This is note for exercise 10.11.5
print('this is note for exercise 10.11.5')
d = {}

for k in counter1:
    d[k] = counter1[k]
for k in counter2:
    d[k] = counter2.get(k, 0) + d.get(k, 0)

print(d)

# --This is note for exercise 10.11.5


print('this is exercise 10.11.5')
def add_counters(dict1, dict2):
    """Combine two letter‑count dictionaries, sum counts for each letter.

    args:
        dict1, dict2: two dictionaries that has a set of keys and their responding values,
         which represents the times they appear.

    Returns:
        dict: new merged dictionary with summed counts
    """
    d = {}

    for key in dict1:
        d[key] = dict1[key]
    for key in dict2:
        d[key] = dict2.get(key,0) + d.get(key, 0)

    return d

# Test case 1: the example from problem statement: brontosaurus and apatosaurus
combined = add_counters(counter1, counter2)
print(combined)

# Test case 2: simple small words, some overlapping letters
c1 = value_counts("aab")   # {'a':2, 'b':1}
c2 = value_counts("bbc")  # {'b':2, 'c':1}
res = add_counters(c1, c2)
print(res)
# expected result: {'a':2, 'b':3, 'c':1}

# Test case3: no shared letters between two counters
c1 = value_counts("xyz")
c2 = value_counts("abc")
res = add_counters(c1, c2)
print(res)
# expected: {'x':1, 'y':1, 'z':1, 'a':1, 'b':1, 'c':1}

# Test case4: one empty counter (edge case)
c1 = {}
c2 = value_counts("hello")
res = add_counters(c1, c2)
print(res)
# expected same as value_counts("hello")

# Test case5: both empty dictionaries
c1 = {}
c2 = {}
res = add_counters(c1, c2)
print(res)
# expected: {}

# Reference sample implementation (from virtual assistant):

def add_counters_va(c1, c2):
    """Combine two letter‑count dictionaries, sum counts for each letter.

    Args:
        c1 (dict): first counter dict from value_counts
        c2 (dict): second counter dict from value_counts
    Returns:
        dict: new merged dictionary with summed counts
    """
    new_dict = {}
    # collect all unique keys from both dictionaries
    all_keys = set(c1.keys()).union(c2.keys())
    for k in all_keys:
        val1 = c1.get(k, 0)
        val2 = c2.get(k, 0)
        new_dict[k] = val1 + val2
    return new_dict


print('\n')
# 10.11.6. Exercise
"""
A word is “interlocking” if we can split it into two words by taking alternating letters.
 For example, “schooled” is an interlocking word because it can be split into “shoe” and “cold”.

To select alternating letters from a string, you can use a slice operator with three components 
that indicate where to start, where to stop, and the “step size” between the letters.

In the following slice, the first component is 0, so we start with the first letter.
 The second component is None, which means we should go all the way to the end of the string.
  And the third component is 2, so there are two steps between the letters we select.
  
word = 'schooled'
first = word[0:None:2]
first

'shoe'

Instead of providing None as the second component, we can get the same effect by leaving it out altogether.
 For example, the following slice selects alternating letters, starting with the second letter.
 
second = word[1::2]
second

'cold'

Write a function called is_interlocking that takes a word as an argument and returns True
 if it can be split into two interlocking words.
"""


def load_words(filename):
    """Load words‑txt file into a list of words.

    Args:
        filename(str): path to words.txt
    Returns:
        list: word_list, each element is one word string
    """
    word_list = []
    fin = open(filename)
    for line in fin:
        # strip() removes newline character at end of each line
        word = line.strip()
        word_list.append(word)
    fin.close()
    return word_list


# load the file into variable word_list
word_list = load_words("words.txt")
word_set = set(word_list)
# Look‑up in a set is faster than in a list. Set uses hash‑table; elements must be hashable.

# Write a function called is_interlocking that takes a word as an argument and returns True
# if it can be split into two interlocking words.


def is_interlocking(word):
    if len(word) % 2 != 0:
        return False
    return word[0::2] in word_list and word[1::2] in word_set


# for word in word_list:
#     if len(word) >= 8 and is_interlocking(word):
#         first = word[0::2]
#         second = word[1::2]
#         print(word, first, second)

# get how many words you want to print
num_needed = int(input("Enter number of interlocking words to find: "))
found_count = 0

for word in word_set:
    if len(word) >= 8 and is_interlocking(word):
        first = word[0::2]
        second = word[1::2]
        print(word, first, second)
        found_count += 1
        if found_count >= num_needed:
            break   # stop loop after we get enough words

