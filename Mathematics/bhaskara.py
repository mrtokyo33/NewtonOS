import math

class Bhaskara:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c
        self.getRoots()

    def getRoots(self):
        if self.a == 0:
            raise ValueError("Coefficient 'a' cannot be zero in a quadratic equation.")
        
        self.discriminant = self.b**2 - 4*self.a*self.c
        
        self.root1 = (-self.b + math.sqrt(self.discriminant)) / (2*self.a)
        self.root2 = (-self.b - math.sqrt(self.discriminant)) / (2*self.a)
        
    def getX1(self):
        if self.discriminant < 0:
            return None  # No real roots

        return self.root1
    
    def getX2(self):
        if self.discriminant < 0:
            return None  # No real roots    
        
        return self.root2
    
    def getDiscriminant(self):
        return self.discriminant
    
    