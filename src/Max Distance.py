class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, arr):
        maxDiff = 0;
        n=len(arr)
        LMin = [0] * n
        RMax = [0] * n
        LMin[0] = arr[0]
        for i in range(1, n):
            LMin[i] = min(arr[i], LMin[i - 1])
        RMax[n - 1] = arr[n - 1]
        for j in range(n - 2, -1, -1):
            RMax[j] = max(arr[j], RMax[j + 1]);
        i, j = 0, 0
        maxDiff = 0
        while (j < n and i < n):
            if (LMin[i] <= RMax[j]):
                maxDiff = max(maxDiff, j - i)
                j = j + 1
            else:
                i = i + 1
        return maxDiff
