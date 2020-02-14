#!/usr/bin/env python
# coding: utf-8

# In[6]:


#LP:-
# max 40(to + tp) + 15(cp + co)
# s.t.
#     17* to + 5 * co <= 150
#     30* tp + 13 * cp >= 210
#     to, tp, co, cp >=0
#     to, tp, co, cp ∈ N

import gurobipy as gb
from gurobipy import GRB

try:
    m = gb.model("mip1")
    
    to = m.addVar(vtype = GRB.CONTINUOUS, name = "to")
    tp = m.addVar(vtype = GRB.CONTINUOUS, name = "tp")
    co = m.addVar(vtype = GRB.CONTINUOUS, name = "co")
    cp = m.addVar(vtype = GRB.CONTINUOUS, name = "cp")
    
    m.setObjective(40 * (to + tp) + 15 * (cp + co))
    
    m.addConstr(17 * to + 5 * co <= 150, "c0")
    m.addConstr(30 * tp + 13 * cp >= 210, "c1")
    m.addConstr(to >= 0, "c2")
    m.addConstr(tp >= 0, "c3")
    m.addConstr(co >= 0, "c4")
    m.addConstr(cp >= 0, "c5")
    
        #optimizing the model
    m.optimize()
    
    for v in m.getVars():
        print('%s %g' % (v.varName, v.x))
    print('obj %g' % (m.objVal))

except gp.GurobiError as e:
    print('Error code ' + str(e.errno) + ': ' + str(e))

except AttributeError:
    print('Encountered an attribute error')


# In[ ]:




