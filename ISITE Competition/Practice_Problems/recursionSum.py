# Using recursion calculate the sum of a list
def sumList(list_val):
    if len(list_val) == 1:
        return list_val[0]
    
    return list_val[0] + sumList(list_val[1:])

# 0 + 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45
print(sumList([i for i in range(10)]))


# Using recursion sum nested list
def sumListList(list_val):
    total = 0
    for element in list_val:
        if type(element) == type([]):
            total = total + sumListList(element)
        else:
            total = total + element
    
    return total

print(sumListList([1, 2, [3,4], [5,6]]))


# Using recursion get the factorial 
def factorial(val):
    if val <= 1:
        return 1
    
    return val * factorial(val-1)

print(factorial(5))


# Get the sum of the nth term in the fibonacci
def fibonacci(val):
    if val == 1 or val == 2:
        return 1
    else:
        return fibonacci(val-1) + fibonacci(val-2)

print(fibonacci(5))
