import pytest

from ..Planet import Planet
from ..Planet import calc_distance, calc_newton


def test_apply_force():
    p1 = Planet(10, 1, (10, 10))
    p2 = Planet(10, 1, (15, 20))
    vel1 = p1.vel
    p1.apply_force(p2)
    vel2 = p1.vel
    return
