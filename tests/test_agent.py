import random
import pymunk
from sandbox.agent import Agent

def test_agent_step_changes_state():
    random.seed(0)
    space = pymunk.Space()
    space.gravity = (0, 0)
    agent = Agent(space, position=(100, 100))
    initial_pos = (agent.body.position.x, agent.body.position.y)
    initial_vel = (agent.body.velocity.x, agent.body.velocity.y)
    agent.step()
    # advance physics a frame so impulse has effect
    space.step(1.0 / 60.0)
    new_pos = (agent.body.position.x, agent.body.position.y)
    new_vel = (agent.body.velocity.x, agent.body.velocity.y)
    assert new_pos != initial_pos or new_vel != initial_vel
