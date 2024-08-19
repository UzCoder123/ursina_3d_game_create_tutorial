from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture='white_cube.png'):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            texture=texture,
            color=color.lime,
            scale=1,
        )
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                voxel = Voxel(position=self.position + mouse.normal, texture='white_cube.png')
            if key == 'right mouse down':
                destroy(self)

for z in range(10):
    for x in range(10):
        voxel = Voxel(position=(x, 0, z))
player = FirstPersonController(position_y=2)
sky=Sky()
app.run()
