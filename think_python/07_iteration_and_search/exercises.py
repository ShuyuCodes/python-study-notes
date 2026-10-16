# 7.9. Exercises

# xmode = Verbose

# 7.9.1. Ask a virtual assistant

# When people first write functions like this, it is a common error to put both return statements inside the loop,
# like this.


def uses_any_incorrect(word, letters):
    for letter in word.lower():
        if letter in letters.lower():
            return True
        else:
            return False     # INCORRECT! return inside loop, might end function to end earlier


# 7.9.2. Exercise

# Write a function named uses_none that takes a word and a string of forbidden letters,
# and returns True if the word does not use any of the forbidden letters.
#
# Here’s an outline of the function that includes two doctests.
# Fill in the function so it passes these tests, and add at least one more doctest.


def uses_none(word, forbidden):
    """Checks whether a word avoid forbidden letters.

    >>> uses_none('banana', 'xyz')
    True
    >>> uses_none('apple', 'efg')
    False
    """
    for letter in forbidden:
        if letter in word:
            return False

    return True

# 7.9.3. Exercise

# Write a function called uses_only that takes a word and a string of letters,
# and that returns True if the word contains only letters in the string.
#
# Here’s an outline of the function that includes two doctests.
# Fill in the function so it passes these tests, and add at least one more doctest.


def uses_only(word, available):
    """Checks whether a word uses only the available letters.

    >>> uses_only('banana', 'ban')
    True
    >>> uses_only('apple', 'apl')
    False
    >>> uses_only('shuyu','suyh')
    True
    """
    wl = list(word)
    word_set = set(wl)

    al = list(available)
    available_set = set(al)

    if word_set == available_set:
        return True
    else:
        return False


# # note
# wl = list('banana')
# word_set = set(wl)
# print(word_set)
#
# al = list('ban')
# available_set = set(al)
# print(available_set)
#
# if word_set == available_set:
#     print('True')
# else:
#     print('False')
#
# # --note


# 7.9.4. Exercise

# Write a function called uses_all that takes a word and a string of letters,
# and that returns True if the word contains all of the letters in the string at least once.
#
# Here’s an outline of the function that includes two doctests.
# Fill in the function so it passes these tests, and add at least one more doctest.


def uses_all(word, required):
    """Checks whether a word uses all required letters.

    >>> uses_all('banana', 'ban')
    True
    >>> uses_all('apple', 'api')
    False
    >>> uses_all('shuyu', 'shyu')
    True
    """
    count = 0
    for letter in required.lower():
        if letter in word.lower():
            count += 1
    if count >= len(required):
        return True
    return False


# 7.9.5. Exercise

# The New York Times publishes a daily puzzle called “Spelling Bee” that challenges readers to spell
# as many words as possible using only seven letters, where one of the letters is required.
# The words must have at least four letters.
#
# For example, on the day I wrote this, the letters were ACDLORT, with R as the required letter.
# So “color” is an acceptable word, but “told” is not, because it does not use R,
# and “rat” is not because it has only three letters. Letters can be repeated, so “ratatat” is acceptable.
#
# Write a function called check_word that checks whether a given word is acceptable.
# It should take as parameters the word to check, a string of seven available letters,
# and a string containing the single required letter. You can use the functions you wrote in previous exercises.
#
# Here’s an outline of the function that includes doctests. Fill in the function and then check that all tests pass.

def check_word(word, available, required):
    """Check whether a word is acceptable.

    >>> check_word('color', 'ACDLORT', 'R')
    True
    >>> check_word('ratatat', 'ACDLORT', 'R')
    True
    >>> check_word('rat', 'ACDLORT', 'R')
    False
    >>> check_word('told', 'ACDLORT', 'R')
    False
    >>> check_word('bee', 'ACDLORT', 'R')
    False
    """
    if len(word) >= 4 and required in available and required.lower() in word and set(word) <= set(available.lower()):
        return True
    return False


# note
print(set('color'))
print(set('ACDLORT'.lower()))
print(set('color') <= set('ACDLORT'.lower()))
# --note


# According to the “Spelling Bee” rules,
#
# Four-letter words are worth 1 point each.
#
# Longer words earn 1 point per letter.
#
# Each puzzle includes at least one “pangram” which uses every letter. These are worth 7 extra points!
#
# Write a function called score_word that takes a word and a string of available letters and returns its score.
# You can assume that the word is acceptable.
#
# Again, here’s an outline of the function with doctests.


def word_score(word, available):
    """Compute the score for an acceptable word.

    >>> word_score('card', 'ACDLORT')
    1
    >>> word_score('color', 'ACDLORT')
    5
    >>> word_score('cartload', 'ACDLORT')
    15
    """
    if len(word) > 4 and set(word) == set(available.lower()):
        return len(word) + 7
    elif len(word) > 4:
        return len(word)
    elif len(word) == 4:
        return 1

    return 0


# 7.9.6. Exercise

# You might have noticed that the functions you wrote in the previous exercises had a lot in common.
# In fact, they are so similar you can often use one function to write another.
#
# For example, if a word uses none of a set forbidden letters, that means it doesn’t use any.
# So we can write a version of uses_none like this.


def uses_any(word, letters):
    for letter in word.lower():
        if letter in letters.lower():
            return True
    return False


def uses_none(word, forbidden):
    """Checks whether a word avoids forbidden letters.

    >>> uses_none('banana', 'xyz')
    True
    >>> uses_none('apple', 'efg')
    False
    >>> uses_none('', 'abc')
    True
    """
    return not uses_any(word, forbidden)


# There is also a similarity between uses_only and uses_all that you can take advantage of.
# If you have a working version of uses_only, see if you can write a version of uses_all that calls uses_only.
print('\n796')


def uses_all(word, required):
    """Checks whether a word uses all required letters.

    >>> uses_all('banana', 'ban')
    True
    >>> uses_all('apple', 'api')
    False
    >>> uses_all('shuyu', 'shyu')
    True
    """
    return uses_only(word, required)


# 7.9.7. Exercise

# If you got stuck on the previous question, try asking a virtual assistant,
# “Given a function, uses_only, which takes two strings and checks that the first uses only the letters in the second,
# use it to write uses_all, which takes two strings and checks whether the first uses all the letters in the second,
# allowing repeats.”
#
# Use run_doctests to check the answer.

# 7.9.8. Exercise

# Now let’s see if we can write uses_all based on uses_any.
#
# Ask a virtual assistant, “Given a function, uses_any,
# which takes two strings and checks whether the first uses any of the letters in the second,
# can you use it to write uses_all, which takes two strings and checks
# whether the first uses all the letters in the second, allowing repeats.”
#
# If it says it can, be sure to test the result!


def uses_all(word, letters):
    """Checks whether a word uses all required letters.

    >>> uses_all('banana', 'ban')
    True
    >>> uses_all('apple', 'api')
    False
    >>> uses_all('shuyu', 'shyu')
    True
    """
    for letter in letters:
        if not uses_any(word, letter):
            return False
    return True


