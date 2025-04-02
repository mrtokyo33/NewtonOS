from Mathematics.vector import * 
from Mathematics.bhaskara import *
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
    
    def getDisplacement(self, time: float):
        displacement = self.getPositionAfterXSeconds(time)
        return (displacement[0]**2 + displacement[1]**2 + displacement[2]**2)**0.5
        
    def getTimeToReachPosition(self, finalPosition: tuple):
        dx = finalPosition[0] - self.initialPosition[0]
        dy = finalPosition[1] - self.initialPosition[1]
        dz = finalPosition[2] - self.initialPosition[2]

        vx = self.velocity.getVx()
        vy = self.velocity.getVy()
        vz = self.velocity.getVz()

        dotProduct = dx * vx + dy * vy + dz * vz
        if dotProduct <= 0:
            return math.inf 

        times = []
        if vx != 0: times.append(dx / vx)
        if vy != 0: times.append(dy / vy)
        if vz != 0: times.append(dz / vz)

        if len(times) > 0 and all(t == times[0] for t in times) and times[0] >= 0:
            return times[0]
        else:
            return math.inf 
    
    def getTimeToReachDistance(self, targetDistance: float):
        x0, y0, z0 = self.initialPosition

        vx = self.velocity.getVx()
        vy = self.velocity.getVy()
        vz = self.velocity.getVz()

        # distance over time: ||R(t)|| = targetDistance
        # R(t) = (x0 + vx*t, y0 + vy*t, z0 + vz*t)
        # Eq: (x0 + vx*t)^2 + (y0 + vy*t)^2 + (z0 + vz*t)^2 = targetDistance^2

        a = vx**2 + vy**2 + vz**2
        b = 2 * (x0*vx + y0*vy + z0*vz)
        c = x0**2 + y0**2 + z0**2 - targetDistance**2

        equation = Bhaskara(a, b, c)

        if a == 0 or equation.getDiscriminant() < 0:
            return math.inf
        else:
            t1 = equation.getX1()
            t2 = equation.getX2()

        validTimes = [t for t in [t1, t2] if t >= 0]
        return min(validTimes) if validTimes else math.inf

    def getTimeToReachDisplacement(self, targetDisplacement: float):
        x0, y0, z0 = self.initialPosition

        vx = self.velocity.getVx()
        vy = self.velocity.getVy()
        vz = self.velocity.getVz()

        # distance over time: ||R(t)|| = targetDisplacement
        # R(t) = (x0 + vx*t, y0 + vy*t, z0 + vz*t)
        # Eq: (x0 + vx*t)^2 + (y0 + vy*t)^2 + (z0 + vz*t)^2 = targetDisplacement^2

        a = vx**2 + vy**2 + vz**2
        b = 0
        c = -targetDisplacement**2

        equation = Bhaskara(a, b, c)

        if a == 0 or equation.getDiscriminant() < 0:
            return math.inf
        else:
            t1 = equation.getX1()
            t2 = equation.getX2()

        validTimes = [t for t in [t1, t2] if t >= 0]
        return min(validTimes) if validTimes else math.inf


    def getVelocity(self):
        return self.velocity.getComponents()
    
    def getVelocityMagnitude(self):
        return self.velocity.getMagnitude()

