size = int(input("Enter the size: "))

# Pyramid
for i in range(size):
    print(" "*(size-i-1),end="")
    print("*"*(2*i+1))

# Inverted Pyramid
print()
for i in range(size-1,-1,-1):
    print(" "*(size-i-1),end="")
    print("*"*(2*i+1))


print()
for i in range(1,size+1):
    for j in range(0,i):
        print("*",end="")
    print()

print()
for i in range(size, -1,-1):
    for j in range(0,i):
        print("*",end="")
    print()

print()
for i in range(1, size+1):
    for j in range(size, 0, -1):
        if j > i:
            print(" ", end='')
        else:
            print("*", end='')

    print()

print()
for i in range(1, size+1):
    for j in range(size, 0, -1):
        if j < i:
            print(" ", end='')
        else:
            print("*", end='')

    print()
