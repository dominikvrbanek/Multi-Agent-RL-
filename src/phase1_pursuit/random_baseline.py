"""Measure the random-action baseline (the floor trained agents must beat).

    python -m phase1_pursuit.random_baseline --episodes 20
"""
import argparse
import statistics

from phase1_pursuit.env import make_pursuit
from phase1_pursuit.random_agent import run_random_episode


def measure_baseline(episodes: int) -> list[float]:
    """Total team reward (summed over all pursuers) for each random episode."""
    env = make_pursuit()
    try:
        return [sum(run_random_episode(env, seed=ep).values()) for ep in range(episodes)]
    finally:
        env.close()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--episodes", type=int, default=20)
    args = parser.parse_args()

    totals = measure_baseline(args.episodes)
    print(f"Random baseline over {args.episodes} episodes:")
    print(f"  mean team reward per episode: {statistics.mean(totals):.2f}")
    print(f"  std:                          {statistics.pstdev(totals):.2f}")


if __name__ == "__main__":
    main()
