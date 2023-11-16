# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 17:12:59 2023

@author: brand
"""
import gymnasium as gym
from gymnasium import spaces
import numpy as np
from gym_arenaxlabs.envs.aiarena.aiarena import AIArenaGame

class AIArenaEnv(gym.Env):
    def __init__(self, stage_name="arena"):
        self.game = AIArenaGame(stage_name)
        self.observation_space = spaces.Box(
            self.game.get_bounds_values("min", 130), 
            self.game.get_bounds_values("max", 130),
            dtype=np.float32
        )
        self.action_space = spaces.MultiDiscrete([9, 6]) # [direction, combat]

    def reset(self, seed=None, options={}):
        return self.game.reset(seed, options)

    def step(self, action):
        action = action.tolist() if isinstance(action, np.ndarray) else action
        if (self.action_space.contains(action)):
            return self.game.step(action)
        else:
            raise ValueError("Invalid Action")

    def render(self):
        pass

    def close(self):
        self.game.close()