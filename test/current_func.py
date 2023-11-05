#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

def detect_underwater_current(dvl_speed, dvl_direction, adcp_speed, adcp_direction):

    dvl_direction_rad = math.radians(dvl_direction)
    adcp_direction_rad = math.radians(adcp_direction)

    
    dvl_x = dvl_speed * math.cos(dvl_direction_rad)
    dvl_y = dvl_speed * math.sin(dvl_direction_rad)

    
    adcp_x = adcp_speed * math.cos(adcp_direction_rad)
    adcp_y = adcp_speed * math.sin(adcp_direction_rad)

   
    total_x = dvl_x + adcp_x
    total_y = dvl_y + adcp_y

  
    total_speed = math.sqrt(total_x**2 + total_y**2)
    total_direction_rad = math.atan2(total_y, total_x)
    total_direction_deg = math.degrees(total_direction_rad)

    return total_speed, total_direction_deg


# In[5]:


detect_underwater_current(10,2,12,20)[1]


# In[ ]:




