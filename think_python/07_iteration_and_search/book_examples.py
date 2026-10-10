
# 7.6.Search
# a more general function called uses_any that takes a second parameter that is a string of letters.
# It returns True if the word uses any of the letters and False otherwise.


def uses_any(word, letters):
    for letter in word.lower():
        if letter in letters.lower():
            return True
    return False
