import gym
# https://github.com/openai/gym/wiki/Leaderboard

"""
A pole is attached by an un-actuated joint to a cart, which moves along a frictionless track. 
The system is controlled by applying a force of +1 or -1 to the cart. 
The pendulum starts upright, and the goal is to prevent it from falling over. 
A reward of +1 is provided for every timestep that the pole remains upright. 
The episode ends if:
1. Pole Angle is more than ±12°
2. Cart Position is more than ±2.4 (center of the cart reaches the edge of the display)
3. Episode length is greater than 200
The problem is considered solved when the average reward is greater than or equal to 195 
over 100 consecutive trials.  
"""

env = gym.make('CartPole-v0')
print(env.action_space)       # there are 2 possible actions: push to the left (0) or to the right (1)
print(env.observation_space)  # there are 4 possible states: [Position Velocity Angle Velocity_at_tip]

# show the observation's bound
print(env.observation_space.high)
print(env.observation_space.low)
# position: min = -4.8, max = 4.8
# velocity: min = -3e38, max = 3e38
# angle: min = -0.4, max = +0.4
# velocity at tip: min = -3e38, max = 3e38

# def policy(t):
   # action = 0
   # if t < 20:
       # action = 0 # go left
   # elif t >= 20:
       # action = 1  # go right
   # return action

def policy(t):
    action = 0
    if t%2 == 1:  # if is odd
        action = 1
    return action

nb_episodes = 20
nb_timesteps = 100

for episode in range(nb_episodes):  # iterate over the episodes
    state = env.reset()             # initialise the environment
    rewards = []
    
    for t in range(nb_timesteps):    # iterate over time steps
        env.render()                 # display the environment
        state, reward, done, info = env.step(policy(t))  # implement the action chosen by the policy
        rewards.append(reward)      # add 1 to the rewards list
        
        if done: # the episode ends either if the pole is > 15 deg from vertical or the cart move by > 2.4 unit from the centre
            cumulative_reward = sum(rewards)
            print("episode {} finished after {} timesteps. Total reward: {}".format(episode, t+1, cumulative_reward))  
            break
    
env.close()
