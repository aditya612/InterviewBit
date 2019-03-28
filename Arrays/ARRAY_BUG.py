# The following code is supposed to rotate the array A by B positions.

# So, for example,


# A : [1 2 3 4 5 6]
# B : 1

# The output :

# [2 3 4 5 6 1]
# However, there is a small bug in the problem. Fix the bug and submit the problem.

# Link: https://www.interviewbit.com/problems/arraybug/

class Solution:
    # @param a : list of integers
    # @param b : integer
    # @return a list of integers
    def rotateArray(self, a, b):
#         ret = []
#         for i in xrange(len(a)):
#             ret.append(a[(i + b) % len(a)])
        ret = [a[(i + b) % len(a)] for i in xrange(len(a))]
        return ret
        
