from ursina import*

app=Ursina()

player=Entity(model='cube', color=color.red, texture='white_cube.png')

def update():
    if held_keys['a']:
        player.x-=0.05
    if held_keys['d']:
        player.x+=0.05
    if held_keys['w']:
        player.y+=0.05
    if held_keys['s']:
        player.y-=0.05

app.run()