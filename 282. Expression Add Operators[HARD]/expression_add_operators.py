class Solution:
    def addOperators(self, s: str, target: int) -> List[str]:
        results = []

        def dfs(i, path, cur_num, prev_num):
            if i == len(s):
                if cur_num == target:
                    results.append(path)
                return
            
            for j in range(i, len(s)):
                # starting with zero?
                if j > i and s[i] == '0': break
                num = int(s[i:j+1])
                # if cur index is 0 then simple add that number                
                if i == 0:
                    dfs(j + 1, path + str(num), cur_num + num, num)
                else:
                    dfs(j + 1, path + "+" + str(num), cur_num + num, num)
                    dfs(j + 1, path + "-" + str(num), cur_num - num, -num)
                    dfs(j + 1, path + "*" + str(num), cur_num - prev_num + prev_num * num, prev_num * num)
        
        dfs(0, "", 0, 0)
        return results
