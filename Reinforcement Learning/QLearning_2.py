import gym
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

np.bool8 = np.bool_

environment = gym.make("FrozenLake-v1", is_slippery=False, render_mode="ansi")
environment.reset()

nb_states = environment.observation_space.n
nb_actions = environment.action_space.n
qtable = np.zeros((nb_states,nb_actions))


print("Q-table:") 
print(qtable) # ajanın beyni

episodes = 1000
alpha = 0.5
gama = 0.9

outcomes = []

#training
for _ in tqdm(range(episodes)):
    
    state, _ = environment.reset()
    done = False #Ajanın basarı duurumu
    
    outcomes.append("Failure")
    
    while not done:
        
        if np.max(qtable[state])>0:
            action = np.argmax(qtable[state])
        else:
            action = environment.action_space.sample()
            
        new_state, reward, done, info, _ = environment.step(action)
        
        qtable[state, action] = qtable[state,action] + alpha * (reward + gama * np.max(qtable[new_state]- qtable[state, action]))  
        
        state = new_state
        
        if reward:
            outcomes[-1] = "Success"        
        
        
print("Qtable After Training: ")
print(qtable)

plt.bar(range(episodes),outcomes)


#test



episodes = 100
nb_success = 0


for _ in tqdm(range(episodes)):
    
    state, _ = environment.reset()
    done = False #Ajanın basarı duurumu
    

    
    while not done:
        
        if np.max(qtable[state])>0:
            action = np.argmax(qtable[state])
        else:
            action = environment.action_space.sample()
            
        new_state, reward, done, info, _ = environment.step(action)
        
        state = new_state
        
        nb_success += reward
        
print("Success rate:", 100*nb_success/episodes)











































        
        
        