class Selector:
    def __init__(self, g):
        self.list = g
        self.even = []
        self.odd = []
        for i in self.list:
            if i % 2 != 0:
                self.odd.append(i)
            else:
                self.even.append(i)
 
    def get_odds(self):
        return self.odd
 
    def get_evens(self):
        return self.even
    
