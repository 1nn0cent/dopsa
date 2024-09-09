class OddEvenSeparator:
    def __init__(self):  
        self.even_num = []
        self.odd_num = []
 
    def add_number(self, number):
        if number % 2 == 0:
            self.even_num.append(number)
        else:
            self.odd_num.append(number)
 
    def get_even(self):  
        return self.even_num
 
    def get_odd(self):  
        return self.odd_num

if __name__ == "__main__":  
    separator = OddEvenSeparator()
    separator.add_number(1)
    separator.add_number(5)
    separator.add_number(6)
    separator.add_number(8)
    separator.add_number(3)
    print(' '.join(map(str, separator.get_even())))  
    print(' '.join(map(str, separator.get_odd())))   
