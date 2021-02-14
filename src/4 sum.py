class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def fourSum(self, A, B):
        A.sort()
        result = set()
        
        # O(N ^ 2) Time
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                lo, hi = j + 1, len(A) - 1
                
                # O(N) Time
                while lo < hi:
                    x = A[i] + A[j] + A[lo] + A[hi]
                    
                    if x == B:
                        result.add((A[i], A[j], A[lo], A[hi]))
                        hi -= 1
                        lo += 1

                    elif x > B:
                        hi -= 1
                    else:
                        lo += 1

        return sorted(result)
    
