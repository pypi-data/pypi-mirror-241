import numpy as np
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from gym_arenaxlabs.envs.aiarena.aiarena_docker import AIArenaDocker
import subprocess
import os
import time

available_stages = [
    "arena",
    "colosseum",
    "throneroom",
    "treasure"
]

combat_actions_order = [
  "grab",
  "shield",
  "jump",
  "punch",
  "special",
  "nothing"
]

state_space_range = {
    "min":  {
        "0": ["0-15", "32-47", "104", "107-112", "115-129"],
        "-1": ["16-31", "48-103", "105-106", "113-114"]
    },
    "max": {
        "1": ["0-129"]
    }
}

class AIArenaGame:
    def __init__(self, stage_name):
        if self.check_stage_allowed(stage_name):
          self.stage_name = stage_name
        else:
          raise ValueError("Stage name '{}' does not exist".format(stage_name))

        # Start the game if it's not already running
        self.docker_manager = AIArenaDocker()
        self.docker_manager.run_game()
        
        self.session = requests.Session()
        self.headers = { "origin": "ai-arena-gym" }
        
        # Implement custom retry strategy to tackle connection errors 
        retry_strategy = Retry(total=20, connect=5, backoff_factor=0.2)
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.route = "http://localhost:8080/gym/"
        self.session.mount(self.route, adapter) 
        
        response = self.session.post(
            self.route + 'initialize', 
            json = {'stageName': "arena"},
            headers = { "origin": "ai-arena-gym" }
        )
        # response = requests.post(   
        #     self.route + 'initialize', 
        #     json = {'stageName': "arena"},
        #     headers = { "origin": "ai-arena-gym" }
        # )
        data = response.json()
        if not data["success"]:
            raise ValueError("Error initializing environment, please try again")        
    
    @staticmethod
    def check_stage_allowed(stage_name):
        return stage_name in available_stages
    
    @staticmethod
    def get_bounds_values(bound_name, n_features):
        values = np.empty(n_features, dtype=np.float32)    
        for v in state_space_range[bound_name]:
            f = float(v)
            for input_range_str in state_space_range[bound_name][v]:
                input_range = input_range_str.split("-")
                if len(input_range) == 2:
                    values[int(input_range[0]):int(input_range[1])+1] = f
                else:
                    values[int(input_range[0])] = f
        return values    
    
    @staticmethod
    def discrete_combat(combat_selection):
        combat_actions= {}
        for idx, action in enumerate(combat_actions_order):
            combat_actions[action] = combat_selection == idx
        return combat_actions

    @staticmethod
    def discrete_direction(direction_selection):
        # [up (0), up-right (1), right (2), down-right (3), down (4), down-left (5), left (6), up-left (7), nothing (8)]
        return {
            "up": (direction_selection == 0 or direction_selection == 1 or direction_selection == 7),
            "right": (direction_selection == 1 or direction_selection == 2 or direction_selection == 3),
            "down": (direction_selection == 3 or direction_selection == 4 or direction_selection == 5),
            "left": (direction_selection == 5 or direction_selection == 6 or direction_selection == 7),
            "nothing": direction_selection == 8
        }

    @staticmethod
    def transform_state(state):
        return np.array(state[0], dtype=np.float32)
    
    def reset(self, seed, options):
        # Currently we don't do anything with the seed or options
        response = self.session.get(self.route + 'reset', headers = self.headers)
        data = response.json()
        if (data["success"]):
            return self.transform_state(data["observation"]), data['info']
        else:
            raise ValueError("Error resetting the environment")
        
    def step(self, action):
        a = self.discrete_direction(action[0])
        a.update(self.discrete_combat(action[1]))
        response = self.session.post(
            self.route + 'step', 
            json = {'action': a},
            headers = self.headers
        )
        data = response.json()
        if (data["success"]):
            truncated = data['done'] # Placeholder for now
            return self.transform_state(data['observation']), data['reward'], data['done'], truncated, data['info']
        else:
            raise ValueError("Error taking a step in the environment")        

    def close(self):
        self.docker_manager.stop_game()