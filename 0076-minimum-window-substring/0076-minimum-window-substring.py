class Solution(object):
    def minWindow(self, s, t):
        n, counter = len(s), len(t)
        begin, end, head = 0, 0, 0 
        
        min_len = n+1        
        
        dic = dict()
        for ch in t:
            dic[ch] = dic.get(ch, 0)+1        
                
        while end < n:
            if s[end] in dic:
                if dic[s[end]] > 0:
                    counter -= 1
                dic[s[end]] -= 1
                
            end += 1            

            while counter == 0:
                if end - begin < min_len:
                    min_len = end-begin
                    head = begin
                    
                if s[begin] in dic:
                    dic[s[begin]] += 1
                    if dic[s[begin]] > 0: 
                        counter += 1                
                begin += 1
                
        if min_len == n+1:
            return ""
        return s[head: head+min_len]