#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from directional_decision import make_directional_decision
from current_func import detect_underwater_current

def test_current_det():
    current = detect_underwater_current(10,2,12,20)
    speed=current[0]
    direction=current[1]
    assert speed>20 and direction>10

def test_decision():
    decision = make_directional_decision(10, 4)
    assert result == "Change Direction"

def test_printing_result(capsys):
    current = detect_underwater_current(10,2,12,20)
    speed=current[0]
    direction=current[1]
    make_directional_decision(speed, direction)
    captured = capsys.readouterr()
    assert "Continue Forward" in captured.out

