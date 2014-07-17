#Created by Jonathan Dimmick
#   Extra Modification added by Damon Edge
from visual import *
"""Modified Sphere Class for the Python Visual Library.
    Move and set functions add for greater ease"""
class PhysSphere:
    def __init__ (self, posx = 0, posy = 0, posz = 0, r = 10, mass = 0.5,
                  Vx = 0, Vy = 0, Vz = 0, color = color.red, make_trail = True,
                  interval = 10):
        self.shape = 1 #if 1, sphere for collision instead of string "sphere"
        self.sphere = sphere(pos = (posx,posy,posz), radius = r, color = color,
                             make_trail = make_trail, interval = interval)
        self.Vx = Vx
        self.Vy = Vy
        self.Vz = Vz
        self.mass = mass
        self.kf = .012

    def getX(self):
        return self.sphere.pos.x
    def getY(self):
        return self.sphere.pos.y
    def getZ(self):
        return self.sphere.pos.z
    def setX(self, x):
        self.sphere.pos = (x, self.sphere.pos.y, self.sphere.pos.z)
    def setY(self, y):
        self.sphere.pos = (self.sphere.pos.x, y, self.sphere.pos.z)
    def setZ(self, z):
        self.sphere.pos = (self.sphere.pos.x, self.sphere.pos.y, z)
    def getVx(self):
        return self.Vx
    def getVy(self):
        return self.Vy
    def getVz(self):
        return self.Vz
    def setVx(self, Vx):
        self.Vx = Vx
    def setVy(self, Vy):
        self.Vy = Vy
    def setVz(self, Vz):
        self.Vz = Vz
    def getMass(self):
        return self.mass
    def getShape(self):
        return self.shape
    def move(self, dx, dy, dz):
        x = self.sphere.pos.x
        y = self.sphere.pos.y
        z = self.sphere.pos.z
        self.sphere.pos = (x + dx, y + dy, z + dz)
    def getRadius(self):
        return self.sphere.radius
    def setColor(self, color):
        self.sphere.color = color
    def getKf(self):
        return self.kf
