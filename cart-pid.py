#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 07:25:20 2023

@author: coleschuelke
"""

# use physics sim to implement a PID controller
import time

import gymnasium as gym
import cartpole as cp
import pid 

       
# initialize the environment and controller
env = cp.CartPoleEnv(render_mode="human")

observation, info = env.reset()
cont = pid.PID(-4,-1,-0.25)

cont.errSum = -0.45

        
# counter to measure progress
n = 0
# the control loop
for i in range(5000):
    n += 1
    theta = observation[2] # ultimately the input to PID
    cont.input = theta
    cont.Compute()
    
    
    # discretize the PID output
    if cont.output > 0.5:
        action = 1 
    else:
        action = 0
    # take a step
    observation, reward, terminated, truncated, info = env.step(action)
    
    if terminated or truncated:
        print(n, ' steps', cont.errSum, ' error sum')
        n = 0
        observation, info = env.reset()
        time.sleep(0.5)

    if i == 4999:
        print(n, ' steps', cont.errSum, ' error sum')
    
    
        

env.close()
        
        
        
        
        