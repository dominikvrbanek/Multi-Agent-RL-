"""Phase 1 evaluation. For now: report the random baseline.

In Month 2 this will also load a trained checkpoint and compare it to the baseline.
    python phase1_predator_prey/evaluate.py --episodes 100
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
    prey = [run_random_episode(env, seed=i)["agent_0"] for i in range(args.episodes)]
    env.close()
    print(f"Random prey: mean episode reward {statistics.mean(prey):.2f} over {args.episodes} episodes")
    print("TODO (Month 2): load a trained checkpoint and compare against this number.")


if __name__ == "__main__":
    main()
