#*******************************************************************************
#**************************** Created by Nick Lucid ****************************
#*********************************** Dec 2022 **********************************
#************* Note: All Kepler orbits are approximated as circles *************
#*******************************************************************************
from vpython import *
import numpy as np

#---------------------- Scene Information -----------------------
scene = canvas()
scene.range = 500 #x10^6 km
scene.height = 1080
scene.width = 1920
scene.fov = pi/6
scene.lights = []
scene.ambient = color.gray(0.1)

#------------------- Astronomical Objects -----------------------
R_Earth = 5
Kepler = [
    #Sun
    sphere( radius = 5 * R_Earth , a = 0 , T = 0 , Path = color.white ,
            color = color.white , emissive = True ) ,
    #Mercury
    sphere( radius = R_Earth , a = 57.9 , T = 0.241 , Path = color.gray(0.5) ,
            texture = 'Maps/MercuryMap.png' ) ,
    #Venus
    sphere( radius = R_Earth , a = 108 , T = 0.615 , Path = color.yellow ,
            color = vector(1,1,0.2) ) ,
    #Earth
    sphere( radius = R_Earth , a = 150 , T = 1 , Path = color.cyan ,
            texture = 'Maps/EarthMap.png' ) ,
    #Mars
    sphere( radius = R_Earth , a = 228 , T = 1.88 , Path = color.red ,
            texture = 'Maps/MarsMap.png' ) ,
    #Jupiter
    sphere( radius = R_Earth , a = 778 , T = 11.9 , Path = color.orange ,
            texture = 'Maps/JupiterMap.png' ) ,
    #Saturn
    sphere( radius = R_Earth , a = 1432 , T = 29.4 , Path = color.purple ,
            texture = 'Maps/SaturnMap.png' ) ,
         ]
for i in arange( 0 , len(Kepler) , 1 ):
    if Kepler[i].T == 0:
        Sun = i
    if Kepler[i].T == 1:
        Earth = i

for Planet in Kepler:
    Planet.pos = vector( Planet.a , 0 , 0 )
    Planet.rotate( angle = pi/2. , axis = vector(1,0,0) )
    Planet.shininess = 0.1
    Planet.visible = 0

#--------------- Coordinate Transformed Objects ----------------
Ptolemy = []
for Planet in Kepler:
    P = Planet.clone( pos = Planet.pos - Kepler[Earth].pos , visible = 1 )
    P.Path = Planet.Path
    Ptolemy.append(P)
SunLight = local_light( pos = Ptolemy[Sun].pos , color = color.white )

Paths = []
for Planet in Ptolemy:
    P = curve( color = Planet.Path , emissive = True , radius = 2 )
    P.append( Planet.pos )
    Paths.append(P)

#------------------------- Animation --------------------------
scene.waitfor('click')
while 1:
    rate(50)
    for i in arange( 0 , len(Kepler) , 1 ):
        #---Kepler Increments---
        if i != Sun:
            Kepler[i].rotate( angle = (pi/200.) / Kepler[i].T ,
                              axis = vector(0,0,1) ,
                              origin = Kepler[Sun].pos )
        #---Ptolemy Increments---
        Ptolemy[i].pos = Kepler[i].pos - Kepler[Earth].pos
        SunLight.pos = Ptolemy[Sun].pos
        #---Draw Paths---
        Paths[i].append( Ptolemy[i].pos )
