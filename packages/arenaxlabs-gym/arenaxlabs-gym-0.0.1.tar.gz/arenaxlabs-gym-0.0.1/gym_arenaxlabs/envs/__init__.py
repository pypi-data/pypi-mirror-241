from typing import Any

from gymnasium import register

register(
    id="AIArena-v0",
    entry_point="gym_arenaxlabs.envs.aiarena:AIArenaEnv",
    max_episode_steps=10800
)

register(
    id="HumanoidObstacle-v0",
    entry_point="gym_arenaxlabs.envs.mujoco:HumanoidObstacleEnv",
    max_episode_steps=1000
)