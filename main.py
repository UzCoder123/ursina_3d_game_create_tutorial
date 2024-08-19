from ursina import *

app=Ursina()

player=Entity(model='cube', scale_x=1, color=color.red, texture='white_cube.png', collider='box')
ground=Entity(model='cube', scale_x=10, scale_z=10, texture='grass.png', y=-1, collider='box')

def update():
    if held_keys['a']:
        player.x-=0.08
    if held_keys['d']:
        player.x+=0.08
    if held_keys['s']:
        player.z-=0.08
    if held_keys['w']:
        player.z+=0.08
    camera.position=player.position
    camera.y=3
    camera.z=player.z-7
    camera.rotation_x=20

app.run()