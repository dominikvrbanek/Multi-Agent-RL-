"""Phase 1 evaluation. For now: report the random baseline.

In Month 2 this will also load a trained checkpoint and compare it to the baseline.

    python -m phase1_pursuit.evaluate --episodes 20
"""
import argparse
import statistics

from phase1_pursuit.random_baseline import measure_baseline


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--episodes", type=int, default=20)
    args = parser.parse_args()

    totals = measure_baseline(args.episodes)
    print(f"Random baseline: mean team reward {statistics.mean(totals):.2f} over {args.episodes} episodes")
    print("TODO (Month 2): load a trained checkpoint and compare against this number.")


if __name__ == "__main__":
    main()
