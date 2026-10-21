import subprocess
import sys

from phase1_pursuit.env import make_pursuit
from phase1_pursuit.random_agent import run_random_episode


def test_pursuit_environment():
    env = make_pursuit()
    try:
        observations, infos = env.reset(seed=42)
        assert len(env.agents) > 0

        agent = env.agents[0]
        assert agent in observations
        assert observations[agent].shape == (7, 7, 3)

        actions = {a: env.action_space(a).sample() for a in env.agents}
        observations, rewards, terminations, truncations, infos = env.step(actions)

        assert isinstance(rewards, dict)
        assert isinstance(terminations, dict)
        assert isinstance(truncations, dict)
    finally:
        env.close()


def test_random_episode_runs_to_completion():
    env = make_pursuit(max_cycles=50)
    try:
        totals = run_random_episode(env, seed=0)
        assert len(totals) > 0
        assert all(name.startswith("pursuer_") for name in totals)
    finally:
        env.close()


def test_phase1_is_self_contained():
    """Phase 1 must not pull in Phase 2 code (or its dependencies)."""
    code = (
        "import sys, phase1_pursuit.env, phase1_pursuit.random_agent, "
        "phase1_pursuit.random_baseline, phase1_pursuit.evaluate\n"
        "bad = [m for m in sys.modules if m.split('.')[0] in ('phase2_unity_soccer', 'marl_soccer')]\n"
        "sys.exit(1 if bad else 0)"
    )
    assert subprocess.run([sys.executable, "-c", code]).returncode == 0
