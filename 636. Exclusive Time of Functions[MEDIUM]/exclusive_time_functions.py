from collections import defaultdict

class Solution:
    def __init__(self):
        self.stack = []
        self.tasks2run = []
        
    def exclusiveTime(self, n, logs):
        for i in range(n):
            self.tasks2run.append(0)
            
        for log in logs:
            self.process_logs(log)
        return self.tasks2run
        
    def process_logs(self, log):
        
        fid, action, time = log.split(":")
        fid, time = int(fid), int(time)
        
        if not self.stack: self.stack.append([fid, time])
        elif action == "start":
            p_fid, p_time = self.stack[-1]
            self.tasks2run[p_fid] += time-p_time-1
            self.stack.append([fid, time])
        else:
            p_fid, p_time = self.stack.pop()
            self.tasks2run[fid] +=  time-p_time+1
            if self.stack: self.stack[-1][1] = time
