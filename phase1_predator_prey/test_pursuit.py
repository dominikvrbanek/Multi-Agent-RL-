#test_pursuit.py
from pettingzoo import make


def test_pursuit_environment():
    env = make("parallel", "sisl/pursuit-v5")
    try:
        observations, infos = env.reset(seed=42)
        assert len(env.agents) > 0

        agent = env.agents[0]
        assert agent in observations
        assert observations[agent].shape == (7, 7, 3)

        actions = {
            agent: env.action_space(agent).sample()
            for agent in env.agents
        }
        observations, rewards, terminations, truncations, infos = (
            env.step(actions)
        )

        assert isinstance(rewards, dict)
        assert isinstance(terminations, dict)
        assert isinstance(truncations, dict)
    finally:
        env.close()


if __name__ == "__main__":
    test_pursuit_environment()
    print("Pursuit smoke test passed!")