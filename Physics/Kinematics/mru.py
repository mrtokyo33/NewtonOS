from Mathematics.vector import * 
import math

class Velocity:
    def __init__(self, velocity: float, theta: float = 90, phi: float = 0):
        self.velocity = velocity
        self.theta = theta
        self.phi = phi
        self.vector = Vector3D(self.velocity, self.theta, self.phi)
        self.getComponents()
        
    def getComponents(self):
        self.vx = self.vector.getX()
        self.vy = self.vector.getY()
        self.vz = self.vector.getZ()
        return (self.vx, self.vy, self.vz)
    
    def getVx(self):
        return self.vx
    
    def getVy(self):
        return self.vy
    
    def getVz(self):
        return self.vz

    def getMagnitude(self):
        return self.velocity
    
#R(t) = R0 + V*t
#V(t) = V 

class Motion:
    def __init__(self, velocity: Velocity, initialPosition: tuple = (0, 0, 0)):
        self.velocity = velocity
        self.initialPosition = initialPosition
        
    def getPositionAfterXSeconds(self, time: float):
        self.rx = self.initialPosition[0] + self.velocity.getVx() * time
        self.ry = self.initialPosition[1] + self.velocity.getVy() * time
        self.rz = self.initialPosition[2] + self.velocity.getVz() * time
        return (self.rx, self.ry, self.rz)
    
    def getDisplacement(self, time: float, type: int=1):
        displacement = self.getPositionAfterXSeconds(time)
        if(type==1):
            return displacement
        elif(type==2):
            self.getPositionAfterXSeconds(time)
            return (displacement[0]**2 + displacement[1]**2 + displacement[2]**2)**0.5
        else:
            raise ValueError("Invalid type")
    
    
    def getVelocity(self):
        return self.velocity.getComponents()
    
