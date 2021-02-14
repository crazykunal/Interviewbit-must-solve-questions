class Solution:
    # @param A : string
    # @return a list of strings
    def restoreIpAddresses(self, A):
        res = []
        self.dfs(A, 0, "", res)
        return res
    
    def dfs(self, s, idx, path, res):
        if idx > 4:
            return 
        if idx == 4 and not s:
            res.append(path[:-1])
            return 
        for i in range(1, len(s)+1):
            if s[:i]=='0' or (s[0]!='0' and 0 < int(s[:i]) < 256):
                self.dfs(s[i:], idx+1, path+s[:i]+".", res)
