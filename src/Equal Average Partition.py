class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def possible(self,index, curr_sum, curr_size):
        if curr_size == 0:
            return (curr_sum == 0)
        if index >= total_size:
            return False
        if dp[index][curr_sum][curr_size] == False:
            return False
        if curr_sum >= original[index]:
            res.append(original[index])
            if self.possible(index + 1, 
                        curr_sum - original[index],
                        curr_size - 1):
                return True
            res.pop()
        if self.possible(index + 1, curr_sum, curr_size):
            return True
        dp[index][curr_sum][curr_size] = False
        return False
    
    
    def avgset(self, Vec):
        global dp, original, res, total_size
        dp = [] 
        res = []
        original = []
        total_size = 0
        Vec.sort()
        original = Vec
        total_sum = 0
        total_size = len(Vec)
        for i in range(total_size):
            total_sum += Vec[i]
        dp = [[[True for _ in range(total_size)] 
                     for _ in range(total_sum + 1)]
                     for _ in range(total_size)]
        for i in range(1, total_size):
            if (total_sum * i) % total_size != 0:
                continue
            Sum_of_Set1 = (total_sum * i) / total_size
            if self.possible(0, Sum_of_Set1, i):
                ptr1 = 0
                ptr2 = 0
                res1 = res
                res2 = [] 
                while ptr1 < len(Vec) or ptr2 < len(res):
                    if (ptr2 < len(res) and
                        res[ptr2] == Vec[ptr1]):
                        ptr1 += 1
                        ptr2 += 1
                        continue
                    res2.append(Vec[ptr1])
                    ptr1 += 1
                ans = []
                ans.append(res1)
                ans.append(res2)
                return ans
        ans = []
        return ans

