#!/usr/bin/env python
# coding: utf-8

# In[10]:


def locater(loc,v,t):
    new_loc=loc+v*t
    return new_loc
def test_locater():
    loc,v,t=map(int,'12/2/4'.split('/'))
    new_loc=locater(loc,v,t)
    assert new_loc==30

