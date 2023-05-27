def shortestWord(licensePlate, words):
    licensePlate = "".join([i.lower() for i in licensePlate if i.isalpha()])
    words = sorted(words,key=len)
    complete = []
    for word in words:
        verify = True
        for letter in licensePlate:
            if licensePlate.count(letter) > word.count(letter) or letter not in word:
                verify = False
                break
        if verify:
            return word
        
licensePlate = "GrC8950"
words = ["measure","other","every","base","according","level","meeting","none","marriage","rest"]

print(shortestWord(licensePlate,words))

def fibobefore(val):
    n = 0
    n2 = 1
    while n < val:
        print(n, end=" ")
        temp = n + n2
        n = n2
        n2 = temp

fibobefore(2)
                    