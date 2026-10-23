# 14.11. Exercises

"""14.11.1. Ask a virtual assistant

There is a lot of new
vocabulary in this chapter. A conversation with a virtual assistant can
help solidify your understanding. Consider asking:

“What is the difference between a class and a type?”
“What is the difference between an object and an instance?”
“What is the difference between a variable and an attribute?”
“What are the pros and cons of pure functions compared to impure functions?”

Because we are just getting started with object-oriented programming, the code in this
chapter is not idiomatic – it is not the kind of code experienced programmers write. If you
ask a virtual assistant for help with the exercises, you
will probably see features we have
not covered yet. In particular, you are likely to see a method called __init__ used to
initialize the attributes of an instance.

If these features make sense to you, go ahead and use them. But if not, be patient – we
will get there soon. In the meantime, see if you can solve the following exercises using only
the features we have covered so far.

Also, in this chapter we saw one example of a format specifier. For more information, ask
“What format specifiers can be used in a Python f-string?”"""

# 14.12. Exercises

# 14.12.1. Exercise

# Write a function called subtract_time that takes two Time objects and returns the
# interval between them in seconds – assuming that they are two times during the same day.

class Time:
    """Represents a time of day."""


def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def subtract_time(t1,t2):
    return time_to_int(t1) - time_to_int(t2)

# 14.12.2. Exercise

# Write a function called is_after that takes two Time objects and returns True if the
# first time is later in the day than the second, and False otherwise.


def make_time(hour, minute, second):
    time = Time()
    time.hour = hour
    time.minute = minute
    time.second = second
    return time


def is_after(t1, t2):
    """Checks whether `t1` is after `t2`.
    >>> is_after(make_time(3, 2, 1), make_time(3, 2, 0))
    True
    >>> is_after(make_time(3, 2, 1), make_time(3, 2, 1))
    False
    >>> is_after(make_time(11, 12, 0), make_time(9, 40, 0))
    True
    """

    return time_to_int(t1) > time_to_int(t2)


# 14.12.3. Exercise

# Here’s a definition for a Date class that represents a date – that is, a year, month, and day
# of the month.

class Date:
    """Represents a year, month, and day"""

# 1. Write a function called make_date that takes year , month , and day as
# parameters, makes a Date object, assigns the parameters to attributes, and returns
# the result the new object. Create an object that represents June 22, 1933.


def make_date(year, month, day):
    date = Date()
    date.year = year
    date.month = month
    date.day = day
    return date


d1  = make_date(1993, 6, 22)

# 2. Write a function called print_date that takes a Date object, uses an f-string to
# format the attributes, and prints the result. If you test it with the Date you created,
# the result should be 1933-06-22 .
def print_date(date):
    s = f'{date.year:04d}-{date.month:02d}-{date.day:02d}'
    print(s)

print_date(d1)

# 3. Write a function called is_after that takes two Date objects as parameters and
# returns True if the first comes after the second. Create a second object that
# represents September 17, 1933, and check whether it comes after the first object.

d2 = make_date(1933, 9, 17)

# Hint: You might find it useful to write a function called date_to_tuple that takes a Date
# object and returns a tuple that contains its attributes in year, month, day order.


def date_to_tuple(date):
    return date.year, date.month, date.day


def is_after(date1, date2):
    return date_to_tuple(date1) > date_to_tuple(date2)


print(is_after(d1, d2))



