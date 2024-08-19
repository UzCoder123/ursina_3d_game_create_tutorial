from ursina import*

app=Ursina()

player=Entity(model='cube', color=color.red, texture='white_cube.png', collider='box', y=2)
ground=Entity(model='cueb', scale=(7,1,1), color=color.blue, texture='white_cube.png', y=-2, collider='box')

tezlik=0.1
tezlik2=0.04

def update():
    global tezlik
    global tezlik2
    player.y-=tezlik
    if player.intersects(ground).hit:
        tezlik=0
    else:
        tezlik=0.1
    if held_keys['a']:
        player.x-=tezlik2
    if held_keys['d']:
        player.x+=tezlik2
    

app.run()