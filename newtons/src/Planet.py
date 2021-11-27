import copy
import math
import pygame

SCALE_FACTOR = 5 * 10 ** -15

sun_mass = 1.989 * 10 ** 30

mercury_mass = 3.3011 * 10 ** 23
mercury_distance = 70 + 150

venus_mass = 4.867 * 10 ** 24
venus_distance = 108 + 150

earth_mass = 5.972 * 10 ** 24
earth_distance = 147 + 150

mars_mass = 6.39 * 10 ** 23
mars_distance = 237 + 150

jupiter_mass = 1.898 * 10 ** 27 * 10**-2
jupiter_distance = 500


class SolarSystem:
    def __init__(self, background):
        self.background = background
        self.size = background.get_size()
        self.sun = Planet('sun', background, size=10, mass=sun_mass,
                          pos=(self.size[0] * 0.5, self.size[1] * 0.5))

        self.planets = [
            Planet('mercury', background, size=2, mass=mercury_mass,
                   pos=(self.size[0] * 0.5, self.size[1] * 0.5 - mercury_distance), vel=(1, 0)),
            Planet('venus', background, size=3, mass=venus_mass,
                   pos=(self.size[0] * 0.5, self.size[1] * 0.5 - venus_distance), vel=(3, 0)),
            Planet('earth', background, size=3, mass=earth_mass,
                   pos=(self.size[0] * 0.5, self.size[1] * 0.5 - earth_distance), vel=(3, 0)),
            Planet('mars', background, size=2, mass=mars_mass,
                   pos=(self.size[0] * 0.5, self.size[1] * 0.5 - mars_distance),
                   vel=(1, 0)),
            Planet('jupiter', background, size=2, mass=jupiter_mass,
                   pos=(self.size[0] * 0.5, self.size[1] * 0.5 - jupiter_distance),
                   vel=(3, 0))
        ]

    def step(self):
        [planet.apply_force(self.sun) for planet in self.planets]
        [planet.step() for planet in self.planets]
        self.sun.draw()

    def get_planet(self, name):
        for planet in self.planets:
            if planet.name == name:
                return planet


class Planet(pygame.sprite.Sprite):
    def __init__(self, name, background, size, mass, pos, vel=(0, 0), acc=(0, 0)):
        super().__init__()
        self.name = name

        self.background = background
        self.size = size
        self.mass = mass
        self.pos = pos
        self.old_pos = None
        self.vel = vel
        self.acc = acc

    def move(self):
        self.old_pos = self.pos
        self.vel = addition(self.vel, self.acc)
        self.pos = addition(self.pos, self.vel)

    def draw(self):
        if self.old_pos is not None:
            pygame.draw.circle(self.background, pygame.Color("BLACK"), self.old_pos, self.size)
        pygame.draw.circle(self.background, pygame.Color("WHITE"), self.pos, self.size)
        self.rect = self.background.get_rect()

    def step(self):
        self.draw()
        self.move()

    def apply_force(self, other):
        force_newton = calc_newton(self, other)
        self.acc = (force_newton[0], force_newton[1])
        return


def calc_newton(plan1, plan2):
    # F = G*M_1*M_2/(r* r^) = C * (1/dx² * x^ + 1/dy² * y^)
    r = calc_distance(plan1.pos, plan2.pos)
    r = r * 10 ** 9
    C = plan1.mass * plan2.mass * math.pow(r, -3) * 6.67 * (10 ** -11) * SCALE_FACTOR
    fx = C * (plan2.pos[0] - plan1.pos[0])
    fy = C * (plan2.pos[1] - plan1.pos[1])
    return fx, fy


def calc_centrifugal(plan1, plan2):
    # a = w²r = v²/r
    r_2 = calc_distance(plan1.pos, plan2.pos) ** 2
    v_2 = plan1.vel[0] ** 2 + plan1.vel[1] ** 2
    dx = plan1.pos[0] - plan2.pos[0]
    dy = plan1.pos[1] - plan2.pos[1]
    ax = - v_2 * dx / r_2
    ay = - v_2 * dy / r_2
    return ax, ay


def calc_distance(pos1, pos2):
    dx = pos2[0] - pos1[0]
    dy = pos2[1] - pos1[1]
    return math.sqrt(dx * dx + dy * dy)


def addition(x1, x2):
    return x1[0] + x2[0], x1[1] + x2[1]
