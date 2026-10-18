from marl_soccer.agents import run_random_episode
from marl_soccer.environments import make_predator_prey


def test_env_has_expected_agents():
    env = make_predator_prey()
    env.reset(seed=0)
    assert set(env.agents) == {"adversary_0", "adversary_1", "adversary_2", "agent_0"}
    env.close()


def test_random_episode_completes_with_reward_per_agent():
    env = make_predator_prey(max_cycles=10)
    totals = run_random_episode(env, seed=0)
    assert set(totals) == {"adversary_0", "adversary_1", "adversary_2", "agent_0"}
    env.close()
