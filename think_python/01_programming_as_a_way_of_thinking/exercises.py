#1.9.1 exercises
# Ask a virtual assistance
# from what I understood, ask AI or website.

"""
1.9.2. Exercise
You might wonder what round does if a number ends in 0.5.
The answer is that it sometimes rounds up and sometimes rounds down.
Try these examples and see if you can figure out what rule it follows.
"""
print("1.9.2 exercises")
print(round(42.5))

print(round(43.5))

print(round(0.5))

print(round(2.5))
print(round(3.5))
print(round(4.5))
print(round(5.5))

print("rule: Python uses bankers rounding (round‑to‑nearest‑even) "
      "\nCommon misconception many people expect: `2.5 → 3` (school‑style round half up). "
      "\nPython’s built‑in `round()` does not work that way.")

"""
1.9.3. Exercise
When you learn about a new feature, you should try it out and make mistakes on purpose. 
That way, you learn the error messages, and when you see them again, you will know what they mean. 
It is better to make mistakes now and deliberately than later and accidentally.

You can use a minus sign to make a negative number like -2. 
What happens if you put a plus sign before a number? What about 2++2?

What happens if you have two values with no operator between them, like 4 2?

If you call a function like round(42.5), what happens if you leave out one or both parentheses?
"""

print("\n1.9.3. Exercise")

n = +2
n2 = 2++2
print(n)
print(n2)

#n3 = 4 2
#print(n3) # ok, invalid syntax

print(25.5)

"""1.9.4. Exercise
Recall that every expression has a value, every value has a type, 
and we can use the type function to find the type of any value.

What is the type of the value of the following expressions? 
Make your best guess for each one, and then use type to find out.
"""
print("\n1.9.4. Exercise")

print(type(765)) # int

print(type(2.718)) # float number,RIGHT ANSWER: FLOAT

print(type('2 pi')) # str

print(type(abs(-7))) # int

print(type(abs(-7.0))) # int,RIGHT ANSWER : FLOAT

print(type(abs)) # type, key word,RIGHT ANSWER: BUILTIN_FUNCTION_OR_METHOD

print(type(int)) # type, key word,RIGHT ANSWER: TYPE

print(type(type)) # type, key word,RIGHT ANSWER: TYPE


"""
1.9.5. Exercise
The following questions give you a chance to practice writing arithmetic expressions.

If you already know about variables, you can use them for this exercise. 
If you don’t, you can do the exercise without them – and then we’ll see them in the next chapter.
"""
print("\n1.9.5. Exercise")

# How many seconds are there in 42 minutes 42 seconds?
def count_seconds(minutes, seconds):
    return minutes*60 + seconds

print(count_seconds(minutes=1, seconds=40)) # return values should be 100 (seconds)
print(count_seconds(minutes=42, seconds=42)) #2562

# How many miles are there in 10 kilometers?
# Hint: there are 1.61 kilometers in a mile.
def km_to_miles(mile):
    kilometers = 1.61*mile
    return kilometers

print(km_to_miles(1)) # return value should be 1.61
print(km_to_miles(10)) #16.1

# If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace in seconds per mile?

def seconds_per_mile(kilometer, minutes, seconds):
    mile = km_to_miles(kilometer)
    seconds = count_seconds(minutes=minutes, seconds=seconds)
    speed = seconds / mile
    return speed

print(seconds_per_mile(kilometer=10, minutes=42, seconds=42)) # 2562/16.1
print(2562/16.1)

# What is your average pace in minutes and seconds per mile?
# I don't run, but my friend mika runs half-marathon in 1 hour 50 minutes in 2026 in Helsinborg, let's see.
#**Half marathon：half‑marathon distance = 21.0975 km**
# Full marathon is 42.195km, half is exactly one‑half of that.

half_marathon_distance_in_km = 21.0975 # in km
half_marathon_distance_in_m = 21097.5 # in meter

mika_used_time_in_minutes = 110 # 1 h 50 minutes in minutes

def seconds_per_100_meter(meters, minutes, seconds):
    one_hundred_meter=meters/100
    s = count_seconds(minutes=minutes,seconds=seconds)
    speed = s/one_hundred_meter
    return speed

print("mika run half marathon's speed(seconds per mile) is ", seconds_per_mile(kilometer=half_marathon_distance_in_km,minutes=mika_used_time_in_minutes, seconds=0))
print("mika run half marathon's speed(seconds per 100 meter) is ",  seconds_per_100_meter(meters=half_marathon_distance_in_m,minutes=110,seconds=0))
print("bolt_100m_time =", 9.58, ", it is still a record, and marathon do is a mild activity.")

# What is your average speed in miles per hour?
# Let's see my friend mika's half-marathon's record for this example again, I love you, mika.
def time_in_hours(hours, minutes):
    total_hours = hours + minutes/60
    return total_hours

mika_used_time_in_hours = time_in_hours(1,50)

print("mika runs half marathon for 1h 50 m, and it is", mika_used_time_in_hours, "hours")

mikas_speed_miles_per_hour = half_marathon_distance_in_m/mika_used_time_in_hours

print("mika runs", mikas_speed_miles_per_hour, "m/h")



