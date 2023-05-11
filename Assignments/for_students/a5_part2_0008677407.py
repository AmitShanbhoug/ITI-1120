# Family name: Amit Shanbhoug
# Student number:  8677407
# Course: IT1 1120 
# Assignment Number 5


class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'

class Rectangle:

    def __init__(self, lpt, rpt, color):
        self.lpt = lpt
        self.rpt = rpt
        self.rect_color = color

    def get_bottom_left(self):
        return self.lpt

    def get_top_right(self):
        return self.rpt

    def get_color(self):
        return self.rect_color

    def reset_color(self, color):
        self.color = color

    def get_perimeter(self):
        x1, y1 = self.lpt.get()
        x2, y2 = self.rpt.get()

        l = x2-x1
        b = y2-y1
        return 2*(l+b)

    def get_area(self):
        x1, y1 = self.lpt.get()
        x2, y2 = self.rpt.get()

        l = x2-x1
        b = y2-y1
        return l*b

    def move(self, dx, dy):

        self.pt1.move(dx, dy)
        self.pt2.move(dx, dy)

    def intersects(self, rect):
        
        if ((self.rpt.x < rect.lpt.x) or (rect.rpt.x < self.lpt.x)):
            return False
        
        if ((self.rpt.y < rect.lpt.y) or (rect.rpt.y < self.lpt.y)): 

            return False
        else:
            return True

    def contains(self, x, y):
        
        if((self.lpt.x <= x) and (self.rpt.x >= x)):
            
            if((self.lpt.y <= y) and (self.rpt.y >= y)):

                return True

    def __eq__(self, other):
        
        return self.lpt == other.lpt and self.rpt == other.rpt and self.color == other.color

    def __repr__(self):
        
        return "Rectangle(" + repr(self.lpt)+"," + repr(self.rpt)+"," + self.color + ")"

    def __str__(self):
        
        return 'I am a '+ self.rect_color + 'rectangle with bottom left corner at ('+ str(self.lpt.x) + ','+ str(self.lpt.y) +') and top right corner at (' + str(self.rpt.x)+','+ str(self.rpt.y)+')'

class Canvas:

    def __init__(self, a=[]):
        
        self.first = first

    def add_one_rectangle(self, rectangle):
        
        self.first.append(rect)

    def count_same_color(self, color):
        
        i = 0
        for r in self.c:
            if r.color == color:
                i = i + 1
                
        return i

    def total_perimeter(self):
        
        perimeter = 0
        
        for r in self.c:
            
            perimeter = perimeter + r.get_perimeter()
            
        return perimeter

    def min_enclosing_rectangle(self):

        min_x = 1000000000
        max_x = -1000000000
        min_y = 1000000000
        max_y = -1000000000

        for r in self.a:

            if min_y > r.lpt.y:
                
                min_y = r.lpt.y

            if max_y < r.rpt.y:
                
                max_y = r.rpt.y
            
            if min_x > r.lpt.x:
                
                min_x = r.lpt.x
            
            if max_x < r.rpt.x:
                
                max_x = r.rpt.x

        rect = Rectangle(Point(min_x, min_y), Point(max_x, max_y), "red")
        
        return repr(rectangle)

    def common_point(self):
        
        for r1 in self.first:
            
            for r2 in self.first:
                
                if not r1.intersects(r2):
                    
                    return False
                
                else:
                    
                    return True 

    def __len__(self):
        
      return len(self.first)

    def __str__(self):
        
        str = "Canvas"
        
        for r in self.first:
            
            str = str + repr(r) + ","
            
        str = str[:-1]
        
        return str
