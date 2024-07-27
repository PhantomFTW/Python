class Point:
    def __init__(self,a,b):
        self.x = a
        self.y = b
        
    def translate(self,deltax,deltay):
        self.x += deltax
        self.y += deltay
        
    def odistance(self):
        import math
        d = math.sqrt(self.x*self.x +
        self.y*self.y)
    
        return(d)

p = Point(3,4)
q = Point(7,10)

p.odistance(), q.odistance()

p.translate(3,4)
p.odistance()

print(p)
#print(p+q)
#p < q

import math
class Point:
    def __init__(self,a,b):
        self.r = math.sqrt(a*a + b*b)
        if a == 0:
            if b >= 0:
                self.theta = math.pi/2
            else:
                self.theta = 3*math.pi/2
        else:
            self.theta = math.atan(b/a)
            
    def translate(self,deltax,deltay):
        x = self.r*math.cos(self.theta)
        y = self.r*math.sin(self.theta)
        x += deltax
        y += deltay
        self.r = math.sqrt(x*x + y*y)
        if x == 0:
            if y >= 0:
                self.theta = math.pi/2
            else:
                self.theta = 3*math.pi/2
        else:
            self.theta = math.atan(y/x)
        
    def odistance(self):
        return(self.r)

p = Point(3,4)
q = Point(7,10)

p.odistance(), q.odistance()

p.translate(3,4)
p.odistance()

print(p)
#print(p+q)
#p < q

class Point:
    def __init__(self,a,b):
        self.x = a
        self.y = b
        
    def translate(self,deltax,deltay):
        self.x += deltax
        self.y += deltay
        
    def odistance(self):
        import math
        d = math.sqrt(self.x*self.x +
        self.y*self.y)
        return(d)
    
    def __str__(self):
        return('('+str(self.x)+','
        +str(self.y)+')')
    
    def __add__(self,p):
        return(Point(self.x + p.x,
        self.y + p.y))

p = Point(3,4)
q = Point(7,10)

p.odistance(), q.odistance()

p.translate(3,4)
p.odistance()

print(p)
str(p)
print(p+q)
print(p,q)

#p < q


class Point:
    def __init__(self,a,b):
        self.x = a
        self.y = b
        
    def translate(self,deltax,deltay):
        self.x += deltax
        self.y += deltay
        
    def odistance(self):
        import math
        d = math.sqrt(self.x*self.x +
        self.y*self.y)
        return(d)
    
    def __str__(self):
        return('('+str(self.x)+','
        +str(self.y)+')')
    
    def __add__(self,p):
        return(Point(self.x + p.x,self.y + p.y))
    
    def __lt__(self,p):
        return(self.x < p.x and self.y < p.y)


p = Point(3,4)
q = Point(7,10)
p < q, q < p

Point.translate(p,9,10)
print(p)

l = [1,2,3]
list.append(l,4)
l
p.x, p.y

class Experiment:
    def __init__(self,a):
        x = a
    def __str__(self):
        return(str(x))
        z = Experiment(5)
        str(z)

class Experiment2:
    def __init__(self,a):
        self.x = a
    def __str__(self):
        return(str(self.x))
        y = Experiment2(7)
        str(y)

class Experiment3:
    def __init__(self,a):
        self.x = a
    def __str__(this):
        return(str(this.x))
    
x = Experiment3(17)
print(x)
