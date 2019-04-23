
# Permutation and Combination

from itertools import permutations, combinations

perm = permutations([y for y in range(10)], 3)
# for i in list(perm):
#     print(i)
print(len(list(perm)))
print("************************************************")
simple = permutations([1, 2, 3, 4])
for i in list(simple):
    print(i)
print("************************************************")

comb = combinations([y for y in range(4)],2)
for i in list(comb):
    print(i)
print("************************************************")

sim = combinations([1, 2, 3, 4, 5], 3)
for i in list(sim):
    print(i)
print("************************************************")

sim2 = combinations([1, 2, 1, 2, 3], 3)
for i in list(sim2):
    print(i)
print("************************************************")
