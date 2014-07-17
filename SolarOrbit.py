#x = center.x + R * cos(theta)
#y = center.y + R * sin(theta)

from visual import *
from math import *
from random import randrange

def findBall(Planet, OrbitCenter, LengthArc, Clockwise):
    r = sqrt((Planet.x-OrbitCenter.x)**2 + (Planet.y-OrbitCenter.y)**2)
    angle = atan2(Planet.y-OrbitCenter.y, Planet.x-OrbitCenter.x)
    if Clockwise:
        angle = angle - LengthArc/r
    else:
        angle = angle + LengthArc/r
    Bx = OrbitCenter.x + (r*cos(angle))
    By = OrbitCenter.y + (r*sin(angle))
    Bz = OrbitCenter.z + (r*sin(angle))
    return (Bx, By, Bz)

def findBnoY(Planet, OrbitCenter, LengthArc, Clockwise):
    r = sqrt((Planet.x-OrbitCenter.x)**2 + (Planet.z-OrbitCenter.z)**2)
    angle = atan2(Planet.z-OrbitCenter.z, Planet.x-OrbitCenter.x)
    if Clockwise:
        angle = angle - LengthArc/r
    else:
        angle = angle + LengthArc/r
    Bx = OrbitCenter.x + (r*cos(angle))
    Bz = OrbitCenter.z + (r*sin(angle))
    return (Bx, Planet.y, Bz)

def findBnoZ(Planet, OrbitCenter, LengthArc, Clockwise):
    r = sqrt((Planet.x-OrbitCenter.x)**2 + (Planet.y-OrbitCenter.y)**2)
    angle = atan2(Planet.y-OrbitCenter.y, Planet.x-OrbitCenter.x)
    if Clockwise:
        angle = angle - LengthArc/r
    else:
        angle = angle + LengthArc/r
    Bx = OrbitCenter.x + (r*cos(angle))
    By = OrbitCenter.y + (r*sin(angle))
    return (Bx, By, Planet.z)

def main():
    sun = sphere(pos=(0,0,0), radius = 10, color = color.yellow,
                 make_trail = False, interval = 10)
    planets = []
    colors = [color.red,color.blue,color.green,color.white]
    dist = 30
    for x in range(8):
        plt = sphere(pos = (dist,0,0), radius = 3,
                        color = colors[randrange(0,len(colors))],
                        make_trail = True, interval = 10)
        planets.append(plt)
        dist += 10
    help(sphere)
    while True:
        rate(1000)
        for planet in planets:
            planet.pos = findBnoY(planet, sun, .1, False)
        sun.rotate(angle = .1)

main()