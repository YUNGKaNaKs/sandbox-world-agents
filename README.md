# sandbox-world-agents
A physics-based 2D sandbox world simulation with AI agent inhabitants

## How to run
Requirements: Python 3.10+, pip

Install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate  # or .\.venv\Scripts\activate on Windows
pip install -r requirements.txt
```

Run the demo:

```bash
python -m sandbox.main
```

## What I added
- Minimal Python project scaffold (pygame + pymunk)
- src/sandbox with a simple simulation loop, world, and agent

If you want a web-based frontend instead (HTML/JS), tell me and I will scaffold that instead.
