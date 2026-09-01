import pymunk
import random


class Agent:
    """A simple agent that applies forces randomly to its body.

    This is a placeholder AI. Replace `decide_action` with a learned policy,
    search, or rule-based behavior as needed.
    """

    def __init__(self, space: pymunk.Space, position=(100, 100)):
        mass = 1
        radius = 18
        moment = pymunk.moment_for_circle(mass, 0, radius)
        self.body = pymunk.Body(mass, moment)
        self.body.position = position
        self.shape = pymunk.Circle(self.body, radius)
        self.shape.elasticity = 0.2
        self.shape.friction = 0.9
        space.add(self.body, self.shape)
        self.space = space

    def perceive(self):
        # Placeholder: return nearby bodies or simple state
        return {
            "pos": tuple(self.body.position),
            "vel": tuple(self.body.velocity),
        }

    def decide_action(self, obs):
        # Placeholder: stochastic small impulses
        fx = (random.random() - 0.5) * 800
        fy = 0
        return (fx, fy)

    def step(self):
        obs = self.perceive()
        fx, fy = self.decide_action(obs)
        self.body.apply_impulse_at_local_point((fx, fy))
