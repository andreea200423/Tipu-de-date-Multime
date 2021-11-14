import itertools
A=['A','B','C','D']
for i in range(len(A)):
    sub=itertools.combinations(A, i+1)
print(set(sub))