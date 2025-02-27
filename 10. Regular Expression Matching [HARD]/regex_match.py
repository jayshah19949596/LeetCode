class Solution(object):
    cache = {}
    def isMatch(self, s, p):
        
        if (s, p) in self.cache:
            return self.cache[(s, p)]

        if not p:
            return not s
        
        if p[-1] == "*":
            
            if self.isMatch(s, p[:-2]):
                self.cache[(s, p)] = True
                return True
            
            if s and (s[-1] == p[-2] or p[-2] == '.') and self.isMatch(s[:-1], p):
                self.cache[(s, p)] = True
                return True     
                
        
        if s and (p[-1] == s[-1] or p[-1] == '.') and self.isMatch(s[:-1], p[:-1]):
            self.cache[(s, p)] = True
            return True   
        
        
        
        self.cache[(s, p)] = False
        return False
        
