import random

states = ["Sunny", "Rainy"]
actions = ["Walk", "Shop", "Clean"]

# Transition probabilities
transitions = {
    "Sunny": {"Sunny": 0.8, "Rainy": 0.2},
    "Rainy": {"Sunny": 0.4, "Rainy": 0.6}
}

rewards = {
    ("Sunny", "Walk"): 10,
    ("Rainy", "Walk"): -5,
    ("Rainy", "Clean"): 5,
    ("Sunny", "Shop"): 2
}

def simulate(state, steps=5):
    total_reward = 0
    for _ in range(steps):
        action = random.choice(actions)
        reward = rewards.get((state, action), 0)
        total_reward += reward
        state = random.choices(states, weights=transitions[state].values())[0]
        print(f"Action: {action}, State: {state}, Reward: {reward}")
    print("Total Reward:", total_reward)

simulate("Sunny")
