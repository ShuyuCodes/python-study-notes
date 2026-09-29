# 9.15 exercises

"""
9.15.1. Ask a virtual assistant
In this chapter, I used the words “contrafibularities” and “anaspeptic”, but they are not actually English words. They were used in the British television show Black Adder, Season 3, Episode 2, “Ink and Incapability”.

However, when I asked ChatGPT 3.5 (August 3, 2023 version) where those words came from, it initially claimed they are from Monty Python, and later claimed they are from the Tom Stoppard play Rosencrantz and Guildenstern Are Dead.

If you ask now, you might get different results. But this example is a reminder that virtual assistants are not always accurate, so you should check whether the results are correct. As you gain experience, you will get a sense of which questions virtual assistants can answer reliably. In this example, a conventional web search can identify the source of these words quickly.

If you get stuck on any of the exercises in this chapter, consider asking a virtual assistant for help. If you get a result that uses features we haven’t learned yet, you can assign the VA a “role”.

For example, before you ask a question try typing “Role: Basic Python Programming Instructor”. After that, the responses you get should use only basic features. If you still see features we you haven’t learned, you can follow up with “Can you write that using only basic Python features?”

"""

"""
9.15.2. Exercise
Two words are anagrams if you can rearrange the letters from one to spell the other.
 For example, tops is an anagram of stop.

One way to check whether two words are anagrams is to sort the letters in both words.
 If the lists of sorted letters are the same, the words are anagrams.

Write a function called is_anagram that takes two strings and returns True if they are anagrams.

Using your function and the word list, find all the anagrams of takes.
"""

def is_anagram(string_1, string_2):
    s1_list = list(string_1)
    s1_list.sort()

    s2_list = list(string_2)
    s2_list.sort()

    count = 0
    if len(string_1) == len(string_2):
        for i in range(len(string_1)):
            if s1_list[i] == s2_list[i]:
                count += 1

        if count == len(string_2):
            return True
        else:
            return False
    else:
        print('The length of two strings should be the same!')
        return False

print(is_anagram('tops', 'stop'))
print(is_anagram("hej", "hey"))

print('\n')
print(is_anagram("hi", "hi,"))
print('\n')


# test lines for exercises 9.15.2
print('test lines for exercises 9.15.2')

string_1 = 'tops'
s1_list = list(string_1)
print(s1_list)
s1_list.sort()
print(s1_list)

string_2 = 'stop'
s2_list = list(string_2)
print(s2_list)
s2_list.sort()
print(s2_list)

count = 0
if len(string_1) == len(string_2):
    for i in range(len(string_1)):
        if s1_list[i] == s2_list[i]:
            count += 1

    if count == len(string_2):
        print('True')  # return True
    else:
        print('False')   # return False
else:
    print('The length of two strings should be the same!')
    print('False')  # return False

# 9.15.3. Exercise









