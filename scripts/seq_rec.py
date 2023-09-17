#!/usr/bin/env python
# coding: utf-8

# In[20]:


def pattern_rec(array):
    if array.shape=(n,m):
        if n==m:
            obj='square'
        else:
            obj='reactangle'
    return obj
def test_pattern_rec():
        array=np.array[[1,2,4],[5,6,7]]
        obj=pattern_rec(array)
        assert obj=='rectangle'

