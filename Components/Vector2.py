import math

class Vector2():
    def __init__(self, X,Y):
        
        self.x = X
        self.y = Y

    #Adição
    def __add__(self,other):
        return Vector2(self.x + other.x, self.y + other.y)  
    
    #subtração
    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)
    
    #Multiplicação
    def __mul__(self, other):
        return Vector2(self.x * other.y,self.y * other.y)
    
    #Divisão
    def __truediv__(self, other):
        return Vector2(self.x / other.x, self.y / other.y)

    def __str__(self):
        return f"{self.x,self.y}"
    
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def normalized(self):
        mag = self.magnitude()
        return Vector2(self.x / mag, self.y / mag)
    
    def tuple(self):

        return (self.x,self.y)
    

