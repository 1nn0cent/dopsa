class Table(object):
    
    def __init__(self, rows, cols):  
        self.field = [[0 for _ in range(cols)] for _ in range(rows)]
        self.rows = rows
        self.cols = cols
        
    def get_value(self, row, col):
        if row in range(self.rows) and col in range(self.cols):
            return self.field[row][col]
        return None  

    def set_value(self, row, col, value):
        if 0 <= row < self.rows and 0 <= col < self.cols: 
            self.field[row][col] = value
    
    def n_rows(self):
        return self.rows
 
    def n_cols(self):
        return self.cols

    def delete_row(self, row):
        if 0 <= row < self.rows:  
            del self.field[row]
            self.rows -= 1

    def delete_col(self, col):
        if 0 <= col < self.cols:  
            for row in self.field:
                del row[col]
            self.cols -= 1

    def add_row(self, row):
        if 0 <= row <= self.rows:  
            self.field.insert(row, [0] * self.cols)
            self.rows += 1

    def add_col(self, col):
        if 0 <= col <= self.cols:  
            for row in self.field:
                row.insert(col, 0)
            self.cols += 1

tab = Table(3, 5)
tab.set_value(0, 1, 10)
tab.set_value(1, 2, 20)
tab.set_value(2, 3, 30)
for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i,j), end=' ')
    print()
print()
tab.add_row(1)
for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i,j), end=' ')
    print()
print()