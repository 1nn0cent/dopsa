class Balance:
    def __init__(self):
        self.left = 0
        self.right = 0
 
    def add_right(self, number):
        self.right += number
 
    def add_left(self, number):
        self.left += number
 
    def result(self):
        if self.left > self.right:
            return 'L'
 
        if self.left < self.right:
            return 'R'
 
        return '='

if __name__ == "__main__":
    balance = Balance()
    balance.add_right(10)
    balance.add_left(5)
    balance.add_left(5)
    print(balance.result())
    balance.add_left(1)
    print(balance.result())