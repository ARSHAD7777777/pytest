#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import seq_func
def test_pattern_rec():
        array=np.array[[1,2,4],[5,6,7]]
        obj=seq_func.pattern_rec(array)
        assert obj=='rectangle'

