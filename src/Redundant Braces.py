class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        st = []  
        for ch in A:  
            if (ch == ')'):  
                top = st[-1]  
                st.pop()  
                flag = True
                while (top != '('):  
                    if (top == '+' or top == '-' or top == '*' or top == '/'):  
                        flag = False
                    top = st[-1]  
                    st.pop() 
                if (flag == True): 
                    return 1
            else: 
                st.append(ch)
        return 0
