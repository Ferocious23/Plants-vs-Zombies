class RewardFunction:
    def __init__(self):
        self.prev_score = 0
        self.prev_plant_count = 0

    def calculate_reward(self, game_state, action):
        current_score = game_state.score
        current_plant_count = game_state.plant_count

        # Calculate immediate rewards based on different actions
        if action == "move_up":
            reward = -0.1
        elif action == "move_down":
            reward = -0.1
        elif action == "move_left":
            reward = -0.1
        elif action == "move_right":
            reward = -0.1
        elif action == "place_plant":
            reward = 1.0 if current_plant_count > self.prev_plant_count else -1.0
        else:
            reward = 0.0
        
        # Additional rewards based on changes in score
        score_change = current_score - self.prev_score
        reward += score_change * 0.1

        self.prev_score = current_score
        self.prev_plant_count = current_plant_count

        return reward