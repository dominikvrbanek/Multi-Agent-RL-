"""Install check. Everyone runs this in Week 1 and posts the output in Discord.

    python -m phase1_pursuit.smoke_test            # headless
    python -m phase1_pursuit.smoke_test --render   # opens a window so you can watch
"""
import argparse

from phase1_pursuit.env import make_pursuit


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--render", action="store_true", help="show a window")
    args = parser.parse_args()

    env = make_pursuit(render_mode="human" if args.render else None)
    env.reset(seed=0)
    print(f"Agents: {len(env.agents)} pursuers, e.g. {env.agents[:3]}")

    steps = 0
    while env.agents:
        actions = {a: env.action_space(a).sample() for a in env.agents}
        env.step(actions)
        steps += 1
    env.close()

    print(f"Ran {steps} steps with random actions.")
    print("SUCCESS: Pursuit environment is working.")


if __name__ == "__main__":
    main()
