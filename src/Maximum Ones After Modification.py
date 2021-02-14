class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        i = j = besti = bestj = 0
        while j < len(A):
            if A[j] == 0:
                B -= 1
                while i <= j and B < 0:
                    B += 1 if A[i] == 0 else 0
                    i += 1
            j += 1
            if j-i > bestj-besti:
                besti, bestj = i, j
        return bestj-besti
