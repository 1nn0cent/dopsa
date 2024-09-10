import datetime as dt

class Date:
    def __init__(self, month, day):
        self.month = month
        self.day = day

    def __sub__(self, other):
        date1 = dt.date(2024, self.month, self.day)
        date2 = dt.date(2024, other.month, other.day)
        total_date = str(date1 - date2).split()
        if len(total_date) != 1:
            return total_date[0]
        else:
            return 0
        
