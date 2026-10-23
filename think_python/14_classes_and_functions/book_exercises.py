# Classes and Functions

"""
At this point you know how to use f
unctions to organize code and how to use built-in types
to organize data. The next step is object-oriented programming, which uses
programmer-defined types to organize both code and data.
O
bject-oriented programming is a big topic, so we will proceed gradually. In this chapter,
we’ll start with code that is not idiomatic – that is, it is not the kind of code experienced
programmers write – but it is a good place to start. In the next two chapters, we will use
additional features to write more idiomatic code.

"""

# 14.1. Programmer-defined types

# We have used many of Python’s built-in types – now we will define a new type. As a first
# example, we’ll create a type called Time that represents a time of day. A programmer-
# defined type is also called a class. A class definition looks like this:

class Time:
    """Represents a time of day."""

# The header indicates that the new class is called Time . The body is a docstring that
# explains what the class is for. Defining a class creates a class object.

# The class object is like a factory for creating objects. To create a Time object, you call
# Time as if it were a function.

lunch = Time()

# The result is a new object whose type is __main__.Time , where __main__ is the name of
# the module where Time is defined.

print(type(lunch))

# When you print an object, Python tells you
# what type it is and where it is stored in memory
# (the prefix 0x means that the following number is in hexadecimal).

print(lunch)

# Creating a new object is called instantiation, and the object is an instance of the class.

# 14.2. Attributes

# An object can contain variables, which are called attributes and pronounced with the
# emphasis on the first syllable, like “AT-trib-ute”, rather than the second syllable, like “a-
# TRIB-ute”. We can create attributes using dot notation.

lunch.hour = 11
lunch.minute = 59
lunch.second = 1

# This example creates attributes called hour , minute , and second , which contain the
# hours, minutes, and seconds of the time 11:59:01 , which is lunch time as far as I am
# concerned.

# The variable lunch refers to a Time object, which contains three attributes. Each
# attribute refers to an integer. A state diagram like this – which shows an object and its
# attributes – is called an object diagram.
# You can read the value of an attribute using the dot operator.

print(lunch.hour)

# You can use an attribute as part of any expression.
total_minutes = lunch.hour * 60 + lunch.minute
print(total_minutes)

# And you can use the dot operator in an expression in an f-string.
print(f'{lunch.hour}:{lunch.minute}:{lunch.second}')

# But notice that the previous example is not in the standard format. To fix it, we have to
# print the minute and second attributes with a leading zero. We can do that by extending
# the expressions in curly braces with a format specifier. In the following example, the
# format specifiers indicate that minute and second should be displayed with at least two
# digits and a leading zero if needed.

print(f'{lunch.hour}:{lunch.minute:02d}:{lunch.second:02d}')

# We’ll use this f-string to write a f
# unction that displays the value of a Time object. You can
# pass an object as an argument in the usual way. For example, the following f
# unction takes
# a Time object as an argument.


def print_time(time):
    s = f'{time.hour:02d}:{time.minute:02d}:{time.second:02d}'
    print(s)


# When we call it, we can pass lunch as an argument.
print_time(lunch)

# 14.3.Objects as return values

# Functions can return objects. For example, make_time takes parameters called hour ,
# minute , and second , stores them as attributes in a Time object, and returns the new
# object.


def make_time(hour, minute, second):
    time = Time()
    time.hour = hour
    time.minute = minute
    time.second = second
    return time

# It might be surprising that the parameters have the same names as the attributes, but
# that’s a common way to write a f
# unction like this. Here’s how we use make_time to create
# a Time object.

time = make_time(11, 59, 1)
print_time(time)

# 14.4.Objects are mutable

# Suppose you are going to a screening of a movie, like Monty Pyth
# on and the Holy Grail,
# which starts at 9:20 PM and runs for 92 minutes, which is one hour 32 minutes. What
# time will the movie end?

# First, we’ll create a Time object that represents the start time
start = make_time(9, 20, 0)
print_time(start)

# To find the end time, we can modify the attributes of the Time object, adding the duration
# of the movie.
start.hour += 1
start.minute += 32
print_time(start)

# The movie will be over at 10:52 PM.
# Let’s encapsulate this computation in a f
# unction and generalize it to take the duration of
# the movie in three parameters: hours , minutes , and seconds .


def increment_time(time, hours, minutes, seconds):
    time.hour += hours
    time.minute += minutes
    time.second += seconds


# Here is an example that demonstrates the effect.
start = make_time(9, 20, 0)
increment_time(start, 1, 32, 0)
print_time(start)

# Inside the function, time is an alias for start , so when time is modified, start changes

# This function works, but after it runs, we’re left with a variable named start that refers to
# an object that represents the end time, and we no longer have an object that represents
# the start time. It would be better to leave start unchanged and make a new object to
# represent the end time. We can do that by copying start and modifying the copy.

# 14.5. Copying

# The copy module provides a function called copy that can duplicate any object. We can
# import it like this.

from copy import copy

# To see how it works, let’s start with a new Time object that represents the start time of
# the movie.

start = make_time(9, 20, 0)

# Then make a copy
end = copy(start)

# Now start and end contain the same data.
print('------14.5. Copying')
print_time(start)
print_time(end)

# But the is operator confirms that they are not the same object.
print(start is end)

# Let’s see what the == operator does.
print(start == end)

# You might expect == to yield True because the objects contain the same data. But for
# programmer-defined classes, the default behavior of the == operator is the same as the
# is operator – it checks identity, not equivalence.

# 14.6. Pure functions

print('---14.6. Pure functions')

# We can use copy to write pure functions that don’t modify their parameters. For example,
# here’s a function that takes a Time object and a duration in hours, minutes and seconds.
# It makes a copy of the original object, uses increment_time to modify the copy, and
# returns it.


def add_time(time, hours, minutes, seconds):
    total = copy(time)
    increment_time(total, hours, minutes, seconds)
    return total

end = add_time(start, 1, 32, 0)
print_time(end)

# The return value is a new object representing the end time of the movie. And we can
# confirm that start is unchanged.

print_time(start)

"""
add_time is a pure function because it does not modify any of the objects passed to it
as arguments and its only effect is to return a value.
Anything that can be done with impure functions can also be done with pure functions. In
fact, some programming languages only allow pure f
unctions. Programs that use pure
functions might be less error-prone, but impure functions are sometimes convenient and
can be more efficient.
In general, I suggest you
write pure functions whenever it is reasonable and resort to
impure functions only if there is a compelling advantage. This approach might be called a
functional programming style.
"""

# 14.7. Prototype and patch
print('---14.7. Prototype and patch')

# In the previous example, increment_time and add_time seem to work, but if we try
# another example, we’ll see that they are not quite correct.
# Suppose you arrive at the theater and discover that the movie starts at 9:40 , not 9:20 .
# Here’s what happens when we compute the updated end time.

start = make_time(9, 40, 0)
end = add_time(start, 1, 32, 0)
print_time(end)

# The result is not a valid time. The problem is that increment_time does not deal with
# cases where the number of seconds or minutes adds up to more than 60 .
# Here’s an improved version that checks whether second exceeds or equals 60 – if so, it
# increments minute – then checks whether minute exceeds or equals 60 – if so, it
# increments hour .

def increment_time(time, hours, minutes, seconds):
    time.hour += hours
    time.minute += minutes
    time.second += seconds
    if time.second >= 60:
        time.second -= 60
        time.minute += 1
    if time.minute >= 60:
        time.minute -= 60
        time.hour += 1


# Fixing increment_time also fixes add_time , which uses it. So now the previous example
# works correctly.

end = add_time(start, 1, 32, 0)
print_time(end)

# But this function is still not correct, because the arguments might be bigger than 60 . For
# example, suppose we are given the run time as 92 minutes, rather than 1 hours and 32
# minutes. We might call add_time like this.

end = add_time(start, 0, 92, 0)
print_time(end)

# The result is not a valid time. So let’s try a different approach, using the divmod function.
# We’ll make a copy of start and modify it by incrementing the minute attribute.

end = copy(start)
end.minute = start.minute + 92
print(end.minute)

# Now minute is 132 , which is 2 hours and 12 minutes. We can use divmod to divide
# by 60 and return the number of whole hours and the number of minutes left over.

carry, end.minute = divmod(end.minute, 60)
print(carry, end.minute)

# Now minute is correct, and we can add the hours to hour .

end.hour += carry
print_time(end)

# The result is a valid time. We can do the same thing with hour and second , and
# encapsulate the whole process in a function.


def increment_time(time, hours, minutes, seconds):
    time.hour += hours
    time.minute += minutes
    time.second += seconds

    carry, time.second = divmod(time.second, 60)
    carry, time.minute = divmod(time.minute + carry, 60)
    carry, time.hour = divmod(time.hour + carry, 60)


# With this version of increment_time , add_time works correctly, even if the arguments
# exceed 60 .

end = add_time(start, 0, 90, 120)
print_time(end)

"""This section demonstrates a program development plan I call prototype and patch. We
started with a simple prototype that worked correctly for the first example. Then we tested
it with more difficult examples – when we found an error, we modified the program to fix it,
like putting a patch on tire with a puncture.
This approach can be effective, especially if you don’t yet have a deep understanding of
the problem. But incremental corrections can generate code that is unnecessarily
complicated – since it deals with many special cases – and unreliable – since it is hard to
know if you have found all the errors."""

# 14.8. Design-first development
"""An alternative plan is design-first development, which involves more planning before
prototyping. In a design-first process, sometimes a high-level insight into the problem
makes the programming much easier.
In this case, the insight is that we can think of a Time object as a three-digit number in
base 60 – also known as sexagesimal. The second attribute is the “ones column”, the
minute attribute is the “sixties column”, and the hour attribute is the “thirty-six
hundreds column”. When we wrote increment_time , we were effectively doing addition
in base 60, which is why we had to carry from one column to the next.
This observation suggests another approach to the whole problem – we can convert
Time objects to integers and take advantage of the fact that Python knows how to do
integer arithmetic.
Here is a f
unction that converts from a Time to an integer.
"""
print('---14.8. Design-first development')


def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


# The result is the number of seconds since the beginning of the day. For example,
# 01:01:01 is 1 hour, 1 minute and 1 second from the beginning of the day, with is the
# sum of 3600 seconds, 60 seconds, and 1 second.

time = make_time(1, 1, 1)
print_time(time)
print(time_to_int(time))

# And here’s a function that goes in the other direction – converting an integer to a Timeobject – using the divmod function.


def int_to_time(seconds):
    minute, second = divmod(seconds, 60)
    hour, minute = divmod(minute, 60)
    return make_time(hour, minute, second)


# We can test it by converting the previous example back to a Time .
time = int_to_time(3661)
print_time(time)

# Using these functions, we can write a more concise version of add_time .


def add_time(time, hours, minutes, seconds):
    duration = make_time(hours, minutes, seconds)
    seconds = time_to_int(time) + time_to_int(duration)
    return int_to_time(seconds)

# The first line converts the arguments to a Time object called duration . The second line
# converts time and duration to seconds and adds them. The third line converts the sum
# to a Time object and returns it.
# Here’s how it works.

start = make_time(9, 40, 0)
end = add_time(start, 1, 32, 0)
print_time(end)

"""In some ways, converting from base 60 to base 10 and back is harder than just dealing
with times. Base conversion is more abstract; our intuition for dealing with time values is
better.
But if we have the insight to treat times as base 60 numbers – and invest the effort to
write the conversion f
unctions time_to_int and int_to_time – we get a program that
is shorter, easier to read and debug, and more reliable.
It is also easier to add features later. For example, imagine subtracting two Time objects
to find the duration between them. The naive approach is to implement subtraction with
borrowing. Using the conversion f
unctions is easier and more likely to be correct.
Ironically, sometimes making a problem harder – or more general – makes it easier,
because there are fewer special cases and fewer opportunities for error.
"""

# 14.9. Debugging
print('---14.9. Debugging')
# Python provides several built-in functions that are useful for testing and debugging
# programs that work with objects. For example, if you are not sure what type an object is,
# you can ask.

print(type(start))

# You can also use isinstance to check whether an object is an instance of a particular
# class.

print(isinstance(end, Time))

# If you are not sure whether an object has a particular attribute, you can use the built-in
# function hasattr

print(hasattr(start, 'hour'))

# To get all of the attributes, and their values, in a dictionary, you can use vars .
print(vars(start))

# The structshape module, which we saw in Chapter 11, also works with programmer-
# defined types.

# from structshape import structshape
# t = start, end
# structshape(t)

# 14.10. Glossary

# object-oriented programming: A style of programming that uses objects to organize
# code and data.

# class: A programmer-defined type. A class definition creates a new class object.

# class object: An object that represents a class – it is the result of a class definition.

# instantiation: The process of creating an object that belongs to a class.

# instance: An object that belongs to a class.

# attribute: A variable associated with an object, also called an instance variable.

# object diagram: A graphical representation of an object, its attributes, and their values.

# format specifier: In an f-string, a format specifier determines how a value is converted to
# a string.

# pure function: A function that does not modify its parameters or have any effect other
# than returning a value.
# functional programming style: A way of programming that uses pure functions
# whenever possible.

# prototype and patch: A way of developing programs by starting with a rough draft and
# gradually adding features and fixing bugs.

# design-first development: A way of developing programs with more careful planning that
# prototype and patch.


