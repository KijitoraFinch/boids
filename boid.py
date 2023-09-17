import math
import random   
import numpy as np
from typing import List, Tuple

# Note for copilot: You should use variable name which is easy to understand for non-programmers

# CONSTANTS
BOID_NUM = 20
WIDTH, HEIGHT = 1000, 1000


def main():
    boids=[Boid(random.random()*WIDTH,random.random()*HEIGHT,random.random()*2-1,random.random()*2-1) for i in range(BOID_NUM)]


class Boid:
    def __init__(self, x:float, y: float, vx: float, vy: float, efficiency: float = 1.0):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def update(self,dx,dy):
        self.x += dx
        self.y += dy