"""Random-action baseline. This is the performance floor trained agents must beat."""


def run_random_episode(env, seed: int | None = None) -> dict[str, float]:
    """Play one episode with uniformly random actions.

    Returns total reward per agent for the episode.
    """
    env.reset(seed=seed)
    totals = {agent: 0.0 for agent in env.agents}
    while env.agents:
        actions = {agent: env.action_space(agent).sample() for agent in env.agents}
        _, rewards, _, _, _ = env.step(actions)
        for agent, reward in rewards.items():
            totals[agent] = totals.get(agent, 0.0) + reward
    return totals
