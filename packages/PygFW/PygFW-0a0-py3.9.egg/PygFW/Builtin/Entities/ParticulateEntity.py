from PygFW.Entity import Entity
from random import randint
from PygFW import Eventifies
from PygFW.Image.ImageObject import ImageObject

class ParticulateEntity(Entity):

    def __init__(self, scene, sprites, spawn,
                 fall_velocity: [int, int] = None,
                 wind_velocity: [int, int] = None,
                 justify_existence: [[int, int], [int, int]] = None,
                 initial_position_radius: [[int, int], [int, int]] = None,
                 tick_position_radius: [[int, int], [int, int]] = None,
                 rumble_angle: [int, int] = None,
                 initial_dimensions: [[int, int], [int, int]] = None,
                 initial_scale: [int, int] = None,
                 tick_dimensions: [[int, int], [int, int]] = None,
                 tick_scale: [int, int] = None,
                 rotate_sprite_gallery: bool = False
                 ):

        Entity.__init__(self, scene_surface=scene, sprites=sprites, spawn=spawn, rotate_sprites=rotate_sprite_gallery)

        self.fall_velocity = (0, 0) if fall_velocity is None else fall_velocity
        self.wind_velocity = (0, 0) if wind_velocity is None else wind_velocity

        if justify_existence == 'window':

            self.justify_existence = ((0, 0), (self.scene.engine_surface.window_width, self.scene.engine_surface.window_height))

        elif justify_existence is None:

            self.justify_existence = None

        else:

            self.justify_existence = justify_existence

        self.initial_position_radius = ((self.x, self.y), (self.x, self.y)) if initial_position_radius is None else initial_position_radius
        self.x, self.y = randint(self.initial_position_radius[0][0], self.initial_position_radius[1][0]), randint(self.initial_position_radius[0][1], self.initial_position_radius[1][1])

        self.tick_position_radius = None if tick_position_radius is None else tick_position_radius

        self.rumble_angle = (0, 0) if rumble_angle is None else rumble_angle

        self.initial_dimensions = ((self.sprite.width, self.sprite.height), (self.sprite.width, self.sprite.height)) if initial_dimensions is None else initial_dimensions
        self.sprite.change_dimensions((randint(self.initial_dimensions[0][0], self.initial_dimensions[1][0]), randint(self.initial_dimensions[0][1], self.initial_dimensions[1][1])))

        self.initial_scale = (1, 1) if initial_scale is None else initial_scale
        self.sprite.change_scale(randint(self.initial_scale[0], self.initial_scale[1]))

        self.tick_dimensions = ((self.sprite.width, self.sprite.height), (self.sprite.width, self.sprite.height)) if tick_dimensions is None else tick_dimensions

        self.tick_scale = (1, 1) if tick_scale is None else tick_scale

    def update(self):

        if self.tick_position_radius:

            self.x, self.y = randint(self.tick_position_radius[0][0], self.tick_position_radius[1][0]), randint(self.tick_position_radius[0][1], self.tick_position_radius[1][1])

        self.sprite.change_dimensions((randint(self.tick_dimensions[0][0], self.tick_dimensions[1][0]), randint(self.tick_dimensions[0][1], self.tick_dimensions[1][1])))
        self.sprite.change_scale(randint(self.tick_scale[0], self.tick_scale[1]))
        self.sprite.change_rotation(randint(self.rumble_angle[0], self.rumble_angle[1]))

        if self.justify_existence:

            if not self.justify_existence[0][0] < self.x < self.justify_existence[1][0] or not self.justify_existence[0][1] < self.x < self.justify_existence[1][1]:

                @Eventifies(scene=self.scene, listener=None)
                def remove_self(scene, event):
                    scene.entities.remove(scene.entities.get_tag(self), True)

                self.scene.engine_surface.single_events.add(remove_self)
