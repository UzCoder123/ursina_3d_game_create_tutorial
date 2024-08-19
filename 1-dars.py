from ursina import *

app=Ursina()

object=Entity(model='cube', scale=(2,2,2), position=(3,2,4), color=color.blue, texture='white_cube.png', rotation=(12,31,32))

app.run()