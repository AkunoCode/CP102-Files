given = [int(x) for x in input("Enter list elements: ").split(" ")]

even_list = given[::2]
odd_list = given[1::2]

sums = []
combined = list(zip(odd_list, even_list))
for i in combined:
    sums.append([f"{i[0]} + {i[1]}", sum(i)])

sums = sorted(sums, key=lambda x: x[1])

negatives = [i for i in sums if i[1] < 0]
positives = [i for i in sums if i[1] > 0]

print(negatives[-1])
print(positives[1])
