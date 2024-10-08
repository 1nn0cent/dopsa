class BoundingRectangle(object):
    def __init__(self):
        self.points = []
 
    def add_point(self, *point):
        self.points.append([point[0], point[1]])
 
    def width(self):
        x = [i[0] for i in self.points]
        return max(x) - min(x)
 
    def height(self):
        y = [i[1] for i in self.points]
        return max(y) - min(y)
 
    def bottom_y(self):
        return min([i[1] for i in self.points])
 
    def top_y(self):
        return max([i[1] for i in self.points])
 
    def left_x(self):
        return min([i[0] for i in self.points])
 
    def right_x(self):
        return max([i[0] for i in self.points])

if __name__ == "__main__":      
    rect = BoundingRectangle()
    rect.add_point(10, 20)
    rect.add_point(5, 7)
    rect.add_point(6, 3)
    print(rect.left_x(), rect.right_x())
    print(rect.bottom_y(), rect.top_y())
    print(rect.width(), rect.height())