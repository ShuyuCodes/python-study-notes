

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
