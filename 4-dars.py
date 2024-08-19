from ursina import*

app=Ursina()

player=Entity(model='cube', color=color.red, texture='white_cube.png', collider='box')
devor1=Entity(model='cube', color=color.red, texture='white_cube.png', scale_y=10, x=5, collider='box')
devor2=Entity(model='cube', color=color.red, texture='white_cube.png', scale_y=10, x=-5, collider='box')

tezlik=0.04

def update():
    global tezlik
    player.x+=tezlik
    if player.intersects(devor2).hit:
        tezlik=-tezlik
        print_on_screen('devor2 ga tegdi', position=(-0.5, .3), scale=2)
    if player.intersects(devor1).hit:
        tezlik=-tezlik
        print_on_screen('devor1 ga tegdi', position=(0.5, .3), scale=2)

app.run()