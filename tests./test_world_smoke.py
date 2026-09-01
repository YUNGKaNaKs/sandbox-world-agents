from sandbox.world import World

def test_world_smoke():
    world = World(width=200, height=200)
    assert len(world.agents) > 0
    # step several frames programmatically
    for _ in range(5):
        for agent in world.agents:
            agent.step()
        world.space.step(1.0 / 60.0)
