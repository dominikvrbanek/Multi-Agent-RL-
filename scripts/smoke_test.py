"""Install check. Everyone runs this in Week 1 and posts the output in Discord.

    python scripts/smoke_test.py            # headless
    python scripts/smoke_test.py --render   # opens a window so you can watch
"""
import argparse
import sys

try:
    from marl_soccer.environments import make_predator_prey
except ImportError as err:
    sys.exit(
        f"Import failed: {err}\n"
        "Did you activate the conda env and run 'pip install -e .'? See docs/setup.md"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--render", action="store_true", help="show a window")
    args = parser.parse_args()

    env = make_predator_prey(render_mode="human" if args.render else None)
    env.reset(seed=0)
    print("Agents:", env.agents)

    steps = 0
    while env.agents:
        actions = {a: env.action_space(a).sample() for a in env.agents}
        env.step(actions)
        steps += 1
    env.close()

    print(f"Ran {steps} steps with random actions.")
    print("SUCCESS: predator-prey environment is working.")


if __name__ == "__main__":
    main()
