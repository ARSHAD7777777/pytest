#!/usr/bin/env python
# coding: utf-8

# In[1]:


def make_directional_decision(total_speed, total_direction_deg):
    
    speed_threshold = 0.5  

    
    desired_direction = 30  

   
    direction_difference = abs(total_direction_deg - desired_direction)

   
    if total_speed > speed_threshold:
        if direction_difference <= 20:  
            decision = "Continue Forward"
        else:
            decision = "Change Direction"
    else:
        decision = "Maintain Current Direction"

    return decision


# In[3]:


make_directional_decision(21.731395811379368,11.824921174995373)

