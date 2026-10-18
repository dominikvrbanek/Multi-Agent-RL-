"""Measure the random-action baseline (the floor trained agents must beat).

    python scripts/random_baseline.py --episodes 100
"""
import argparse
import statistics

from marl_soccer.agents import run_random_episode
from marl_soccer.environments import make_predator_prey


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--episodes", type=int, default=100)
    args = parser.parse_args()

    env = make_predator_prey()
    per_agent: dict[str, list[float]] = {}
    for ep in range(args.episodes):
        for agent, total in run_random_episode(env, seed=ep).items():
            per_agent.setdefault(agent, []).append(total)
    env.close()

    print(f"Random baseline over {args.episodes} episodes (mean total reward per episode):")
    for agent, totals in sorted(per_agent.items()):
        print(f"  {agent:12s} {statistics.mean(totals):8.2f}")


if __name__ == "__main__":
    main()
