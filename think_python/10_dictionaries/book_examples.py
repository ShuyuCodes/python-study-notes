
# 10.2. Creating dictionaries
print('\nthis is book example 10.2')

numbers = {'zero': 0, 'one': 1, 'two': 2}

print(numbers)

# dict is a function
empty = dict()
print(empty)


# 10.3. The in operator
print('\nthis is book example 10.3')

# numbers = {'zero': 0, 'one': 1, 'two': 2}

# in operator works also on dictionaries, it tells whether something appear as a key in the dictionary
t = 'one' in numbers
print('if "one" in numbers:', t)  # True

# the in operator does not check whether something appears as a value
f = 1 in numbers
print('if 1 in numbers:', f)  # False

# to see whether something appears as a value in a dictionary, we can use values method, which returns a sequence of values,
# then use in operator
v = 1 in numbers.values()
print('if 1 in numbers.values():', v)  # True

d = {0: 0, 1: 1}

# a = 0 in d[0]
# print('if 0 in d[0]:', a)  # False --TypeError: argument of type 'int' is not iterable

b = 0 in d
print('if 0 in d:', b)  # True

# 10.4.A collection of counters
# Suppose you are given a string, and you want to count how many times each letter appears.
# A dictionary is a good tool for this job.

# The following function counts the number of times each letter appears in a string.

print('\nthis is book example 10.4')


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
print('\nthis is book example 10.5')

counter = value_counts('banana')
for key in counter:
    print(key)

for value in counter.values():
    print(value)

for key in counter:
    value = counter[key]
    print(key, value)

# 10.7. Accumulating a list
print('\n--this is book example 10.7')
known = {0: 0, 1: 1}


def fibonacci_memo(n):
    if n in known:
        print('1st, this time n =', n, 'known =', known)
        print('1st if condition, return known list with n =', known[n], '\n')
        return known[n]

    print('2nd, this time n =', n, 'known =', known)
    res = fibonacci_memo(n-1) + fibonacci_memo(n-2)
    known[n] = res
    print('2nd, return known list with known[n] = fibonacci_memo(n-1) + fibonacci_memo(n-2) =', res)
    return res


print(fibonacci_memo(4))

print('this is known dictionary=', known)

result = fibonacci_memo(4)
print('result is', result)

