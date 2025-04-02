__all__ = ['Vector1D', 'Vector2D', 'Vector3D', 'degreeToRadian']

import math 

def degreeToRadian(degree):
    return math.radians(degree)

class Vector1D:
    def __init__(self, module:float, direction:int=1):
        self.module = module
        self.direction = direction # 1 for positive, -1 for negative     

    def getPos(self):
        return self.module * self.direction
    
    def getX(self):
        return self.module * self.direction

#polar cordenates to cartesian
#x = r * cos(theta)
#y = r * sin(theta)

class Vector2D:
    def __init__(self, module:float, angle:float):
        self.module = module 
        self.angle = angle
        self.getPos()
    
    def getPos(self):
        radAngle = degreeToRadian(self.angle)

        self.x = self.module * math.cos(radAngle)
        self.y = self.module * math.sin(radAngle)
        return (self.x, self.y)
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y    

#sphere cordenates to cartesian
#x = r * sin(theta) * cos(phi)
#y = r * sin(theta) * sin(phi)
#z = r * cos(theta)

class Vector3D:
    def __init__(self, module:float, theta:float, phi:float):
        self.module = module
        self.theta = theta
        self.phi = phi
        self.getPos()
    
    def getPos(self):
        radTheta = degreeToRadian(self.theta)
        radPhi = degreeToRadian(self.phi)

        self.x = self.module * math.sin(radTheta) * math.cos(radPhi)
        self.y = self.module * math.sin(radTheta) * math.sin(radPhi)
        self.z = self.module * math.cos(radTheta)

        if abs(self.z + 1) < 1e-9:
            self.z = -1
        
        self.x = self.roundAdjust(self.x)
        self.y = self.roundAdjust(self.y)
        self.z = self.roundAdjust(self.z)

        return (self.x, self.y, self.z)
    
    def roundAdjust(self, value):
        if abs(value - round(value)) < 1e-9:
            return round(value)
        else:
            return round(value, 4)
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getZ(self):
        return self.z
