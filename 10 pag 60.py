import itertools
A=[1,2,3,4]
for i in range(len(A)):
    sub=itertools.combinations(A, i+1)
print(set(sub))