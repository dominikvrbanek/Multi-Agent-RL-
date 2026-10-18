"""Factory for the Phase 1 environment: MPE2 Simple Tag (predator-prey).

Default setup: 3 predators ("adversary_*", slower) chase 1 prey ("agent_0", faster)
around 2 obstacles. Note: we import from `mpe2`, not `pettingzoo.mpe`, because the
MPE environments were moved out of PettingZoo and the old path is deprecated.
"""
from mpe2 import simple_tag_v3


def make_predator_prey(
    num_good: int = 1,
    num_adversaries: int = 3,
    num_obstacles: int = 2,
    max_cycles: int = 25,
    continuous_actions: bool = False,
    render_mode: str | None = None,
):
    """Return a PettingZoo *parallel* environment (all agents act each step)."""
    return simple_tag_v3.parallel_env(
        num_good=num_good,
        num_adversaries=num_adversaries,
        num_obstacles=num_obstacles,
        max_cycles=max_cycles,
        continuous_actions=continuous_actions,
        render_mode=render_mode,
    )
