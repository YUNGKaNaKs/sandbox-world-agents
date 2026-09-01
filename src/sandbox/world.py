import pygame
import pymunk
import pymunk.pygame_util
import random
from .agent import Agent


class World:
    def __init__(self, width=800, height=600):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sandbox World Agents")
        self.clock = pygame.time.Clock()

        # Physics
        self.space = pymunk.Space()
        self.space.gravity = (0, 900)
        self.draw_options = pymunk.pygame_util.DrawOptions(self.screen)

        # Create static floor
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        shape = pymunk.Segment(body, (0, height - 50), (width, height - 50), 5)
        shape.friction = 1.0
        self.space.add(body, shape)

        # Agents
        self.agents = []
        for i in range(5):
            x = 100 + i * 120
            agent = Agent(self.space, position=(x, 50))
            self.agents.append(agent)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # AI step
            for agent in self.agents:
                agent.step()

            # Physics step
            dt = 1.0 / 60.0
            self.space.step(dt)

            # Draw
            self.screen.fill((30, 30, 30))
            self.space.debug_draw(self.draw_options)
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
