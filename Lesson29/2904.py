class MinStat(object):
    def __init__(self):
        self.lst = [ ]
    def add_number(self,x):
        self.lst.append(x)
    def result(self):
        return min(self.lst) if self.lst else None
 
class MaxStat(MinStat):
    
    def result(self):
        return max(self.lst) if self.lst else None
    
class AverageStat(MinStat):
    
    def result(self):
        return sum(self.lst) / len(self.lst) if self.lst else None
