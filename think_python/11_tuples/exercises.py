# 11.11. Exercises

# xmode Verbose

# 11.11.1. Ask a virtual assistant

# One strategy you might consider is to break a big problems into pieces that can be solved with simple functions.
# Ask the virtual assistant to write the functions and test them. Then, once they are working,
# ask for a solution to the original problem.

# 11.11.2. Exercise

list0 = [1, 2, 3]
list1 = [4, 5]

t = (list0, list1)
print(t)

list1.append(6)
print(t)

# d = {t: 'this tuple contains two lists'}
# print(d)  # TypeError: unhashable type: 'list'

# “Are Python tuples always hashable?”
"""
No, Python tuples are not always hashable. Whether a tuple is hashable depends on the elements it contains.
1. What does “hashable” mean?
An object is hashable if Python can calculate a hash value for it using hash().
 Hashable objects can be used as dictionary keys or set elements.
 
 2. Example 1: A hashable tuple
"""
t = (1, 2, 3)
print(hash(t))  # This works because all three elements are integers, which are hashable.

d = {(1, 2, 3): "hello"}
print(d[(1, 2, 3)])  # hello

# 3. Example 2: An unhashable tuple

t = (1, 2, [3, 4])
# print(hash(t))  # TypeError: unhashable type: 'list'

# This raises a TypeError because the tuple contains a list, and lists are unhashable.
# Although the tuple itself cannot have its elements reassigned, the list inside it can be modified.
# This is why Python cannot hash this tuple.

# 4. What about a tuple containing another tuple?

t = (1, (2, 3))
print(hash(t))  # This works because integers and tuples containing only hashable elements are hashable.

# The rule to remember: A tuple is hashable only if all its elements are hashable.

# 11.11.3. Exercise

# We can use letter_map and letters to encode and decode words using a Caesar cipher.
#
# A Caesar cipher is a weak form of encryption that involves shifting each letter
# by a fixed number of places in the alphabet, wrapping around to the beginning if necessary.
# For example, 'a' shifted by 2 is 'c' and 'z' shifted by 1 is 'a'.
#
# Write a function called shift_word that takes as parameters a string and an integer,
# and returns a new string that contains the letters from the string shifted by the given number of places.

# To test your function, confirm that “cheer” shifted by 7 is “jolly” and “melon” shifted by 16 is “cubed”.
letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = range(len(letters))
print(len(letters))
letter_map = dict(zip(letters, numbers))


def shift_word(s, n):
    cipher = []

    for letter in s:
        new_index = (letter_map[letter] + n) % len(letters)
        cipher.append(letters[new_index])

    return ''.join(cipher)


# note
print(letter_map['a'])  # 0
print(letters[1])  # b

print(shift_word('cheer', 7))

print(shift_word('melon', 16))

print(22 % 26)
print(28 % 26)

# 11.11.4. Exercise

# In a previous exercise, we tested whether two strings are anagrams by sorting the letters # from chapter 9 lists exercises is_anagram(string_1, string_2)
# in both words and checking whether the sorted letters are the same. Now let’s make the problem a little more challenging.

# We’ll write a program that takes a list of words and prints all the sets of words that are anagrams.
# Here is an example of what the output might look like:

# ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
# ['retainers', 'ternaries']
# ['generating', 'greatening']
# ['resmelts', 'smelters', 'termless']

# Hint: For each word in the word list, sort the letters and join them back into a string.
# Make a dictionary that maps from this sorted string to a list of words that are anagrams of it.


# create a word set with unique words
with open('../words.txt') as reader:
    word_list = []
    d = {}

    for line in reader:  # create word list then word set
        word = line.strip()
        word_list.append(word)
    word_set = set(word_list)


# create a dictionary that maps from this sorted string to a list of words that are anagrams of it
d_anagram = {}
for word in word_set:

    s_l = sorted(list(word))
    s_s = ''.join(s_l)

    if s_s in d_anagram:
        d_anagram[s_s].append(word)
    else:
        d_anagram[s_s] = [word]

# create a dict that has the length of list more than 1 as value
d = {}
for s, l in d_anagram.items():
    if len(l) > 1:
        d[s] = l


print('\n1')
# show 10 word lists in d_anagram
i = 0
for s, wl in d.items():
    if i >= 10:
        break
    print(wl)
    i += 1

# 11.11.6. Exercise

# Write a function called word_distance that takes two words with the same length
# and returns the number of places where the two words differ.
#
# Hint: Use zip to loop through the corresponding letters of the words.


def word_distance(word1, word2):
    n = 0
    if len(word1) == len(word2):
        d = dict(zip(word1, word2))
        for key, value in d.items():
            if key != d[key]:
                n += 1
    return n


print(dict(zip('abc','def')))
print(word_distance('hey', 'hej'))

# 11.11.7. Exercise

# “Metathesis” is the transposition of letters in a word.
# Two words form a “metathesis pair” if you can transform one into the other by swapping two letters,
# like converse and conserve. Write a program that finds all of the metathesis pairs in the word list.

# Hint: The words in a metathesis pair must be anagrams of each other.


def find_metathesis_pairs():
    m_p = []
    for word_list in d.values():
        for word in word_list:
            for i in range(word_list.index(word) + 1, len(word_list)):
                if word_distance(word, word_list[i]) == 1:
                    m_p.append((word, word_list[i]))

    return m_p


l = find_metathesis_pairs()
print(l[:10])










