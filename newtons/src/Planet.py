import math
import pygame


class Planet(pygame.sprite.Sprite):
    def __init__(self, background, size, mass, pos, vel=(0, 0), acc=(0, 0)):
        super().__init__()

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
        force_centi = calc_centrifugal(self, other)
        self.acc = (force_newton[0] + force_centi[0], force_newton[1] + force_centi[1])
        return


class SolarSystem:
    def __init__(self, background):
        self.background = background
        self.size = background.get_size()
        self.sun = Planet(background, size=20, mass=100000, pos=(self.size[0] * 0.5, self.size[1] * 0.5))
        self.earth = Planet(background, size=4, mass=10, pos=(self.size[0] * 0.5, 100), vel=(2, 0))
        self.mars = Planet(background, size=5, mass=12, pos=(400, self.size[1] * 0.5), vel=(0, 1))

        self.planets = [self.sun, self.earth, self.mars]

    def step(self):




        self.mars.step()
        self.earth.step()
        self.sun.step()

        self.mars.apply_force(self.sun)
        self.earth.apply_force(self.sun)
        self.sun.apply_force(self.earth)


def calc_newton(plan1, plan2):
    # F = G*M_1*M_2/(r* r^) = C * (1/dx² * x^ + 1/dy² * y^)
    r = calc_distance(plan1.pos, plan2.pos)
    C = plan1.mass * plan2.mass * math.pow(r, -3) * 6.67 * (10 ** -11)
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
