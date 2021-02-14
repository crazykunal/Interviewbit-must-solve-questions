def count(A, e):  # number of elements smallers than e in A
    cnts = 0
    for elem in A:
        # cnts += bisect_right(elem, e)
        # This code is same as using bisect_right
        low = 0
        high = len(elem)
        while low<high:
            mid = (low+high)//2
            if elem[mid]<=e:
                low = mid+1
            else:
                high = mid
        cnts += low
    return cnts
    
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, A):
        c = (len(A) * len(A[0]))//2 + 1 # median is min number for which cnts>=c
        low = 0
        high = 2**31
        while low<high:
            mid = (low+high)//2
            cs = count(A, mid)
            if cs<c:
                low = mid+1
            else:
                high = mid
        return low
