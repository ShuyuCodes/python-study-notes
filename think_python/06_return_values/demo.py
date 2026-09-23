

#6.6. Recursion with return values
def factorial(n):
    space = ' ' * (4 * n)
    print(space, 'this time n =', n, ', factorial ', n, '\n')

    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        print("n =", str(n), space, "this time n =", str(n), "and recurse = factorial( n - 1 =", str(n-1), ")=", "factorial(", str(n-1), ") =", str(recurse))
        result = n * recurse
        print(space, "returning factorial ( n =", str(n), ") = n * recurse =", " n * ", 'factorial(', str(n-1), ')=', str(result), "\n")
        return result

print('let us run factorial(3) \n')

print('=====================================================================================')

print(factorial(3))

print('=====================================================================================')

def factorial2(n):
    space = ' ' * (4 * n)
    print('n =', n, space, 'header of this function, this time n =', n, ', factorial ', n, ', space is 4*n =', 4*n, '\n')

    if n == 0:
        print('n =', n, space, 'return 1', ', factorial(0)= 1, the first condition in if, and this time n =', n, ', space is 4*n =', 4*n,  '\n')
        return 1
    else:
        recurse = factorial2(n-1)
        print("n =", str(n), space, "the second condition in if, this time n =", str(n), ', space is 4*n =', 4*n)
        print("n =", str(n), space, "the second condition in if,", "and recurse = factorial( n - 1 =", str(n-1), ") = ", "factorial(", str(n-1), ") =", str(recurse), ', space is 4*n =', 4*n)
        result = n * recurse
        print("n =", str(n), space, "returning ", result, ", factorial ( n =", str(n), ") = n * recurse = ", " n * ", 'factorial(', str(n-1), ') =', str(result), "the second condition in if, this time n =", str(n), "\n")
        return result

print('let us run factorial2(3) version 2.0 \n')

print('=====================================================================================')

print(factorial2(3))

print('=====================================================================================')

def factorial3(n):
    space = ' ' * (4 * n)
    print('n =', n, space, 'header,' , 'factorial ', n)

    if n == 0:
        print('n =', n, space, 'returning 1', ', factorial(0)= 1, the first condition in if, and this time n =', n, ', space is 4*n =', 4*n,'\n')
        return 1
    else:
        recurse = factorial3(n-1)
        # print("n =", str(n), space, "the second condition in if, this time n =", str(n), ', space is 4*n =', 4*n)
        # print("n =", str(n), space, "the second condition in if,", "and recurse = factorial( n - 1 =", str(n-1), ") = ", "factorial(", str(n-1), ") =", str(recurse), ', space is 4*n =', 4*n)
        result = n * recurse
        print("n =", str(n), space, "returning ", result, ", factorial ( n =", str(n), ") = n * recurse = ", " n * ", 'factorial(', str(n-1), ') =', str(result), "the second condition in if, this time n =", str(n))
        return result

print('let us run factorial3(3) version 3.0 \n')

print('=====================================================================================')

print(factorial3(3))

print('=====================================================================================')
