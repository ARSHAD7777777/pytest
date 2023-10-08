#!/usr/bin/env python
# coding: utf-8

# In[1]:


def pattern_rec(array):
    if array.shape[0]==array.shape[1]:
        obj='square'
    else:
        obj='reactangle'
    return obj

