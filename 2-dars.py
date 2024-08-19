from ursina import*

app=Ursina()

player=Entity(model='cube', color=color.red, texture='white_cube.png')

def update():
    player.rotation_y+=0.40
    player.rotation_z+=0.40
    player.rotation_x+=0.40

app.run()