# This tool computes the cartesian product of input iterables.
# It is equivalent to nested for-loops.

# >>> from itertools import product >>> >>> print list(product([1,2,3],repeat = 2)) [(1, 1), (1, 2), (1, 3), (2, 1),
# (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)] >>> >>> print list(product([1,2,3],[3,4])) [(1, 3), (1, 4), (2, 3), (2, 4),
# (3, 3), (3, 4)] >>> >>> A = [[1,2,3],[3,4,5]] >>> print list(product(*A)) [(1, 3), (1, 4), (1, 5), (2, 3), (2, 4),
# (2, 5), (3, 3), (3, 4), (3, 5)] >>> >>> B = [[1,2,3],[3,4,5],[7,8]] >>> print list(product(*B)) [(1, 3, 7), (1, 3,
# 8), (1, 4, 7), (1, 4, 8), (1, 5, 7), (1, 5, 8), (2, 3, 7), (2, 3, 8), (2, 4, 7), (2, 4, 8), (2, 5, 7), (2, 5, 8),
# (3, 3, 7), (3, 3, 8), (3, 4, 7), (3, 4, 8), (3, 5, 7), (3, 5, 8)]
from itertools import product
A = map(int, input().split())
B = map(int, input().split())

for Product in product(A, B):
    print(Product, end =" ")


# Question 2
# You are given a string .
# Your task is to print all possible permutations of size of the string in lexicographic sorted order.
# >>> from itertools import permutations
# >>> print permutations(['1','2','3'])
# <itertools.permutations object at 0x02A45210>
# >>>
# >>> print list(permutations(['1','2','3']))
# [('1', '2', '3'), ('1', '3', '2'), ('2', '1', '3'), ('2', '3', '1'), ('3', '1', '2'), ('3', '2', '1')]
# >>>
# >>> print list(permutations(['1','2','3'],2))
# [('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
# >>>
# >>> print list(permutations('abc',3))
# [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
from itertools import permutations
input_string = input().split()

for word in sorted(list(permutations(input_string[0], int(input_string[1])))):
    print("".join(word))
