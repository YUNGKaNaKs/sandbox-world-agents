import sys
from sandbox.world import World


def main():
    world = World(width=800, height=600)
    world.run()


if __name__ == "__main__":
    main()
