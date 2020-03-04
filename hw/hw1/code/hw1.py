#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sympy as sp
from itertools import chain
from routh import routh


# In[3]:


def kh_gen(n):
    kh = [[0, 0, 1, 1], [1, 1, 0, 0], [0, 1, 1, 0], [1, 0, 0, 1]]
    out = [[],[],[],[]]

    w, r = divmod(n, 4)
        
    for j in range(4):
        for i in range(w):
            out[j] = out[j] + kh[j]
        for i in range(r):
            out[j].append(kh[j][i])
    return out


# In[4]:


q = list(sp.symbols('q_0:2'))
r = sp.symbols('r_0:7')
s = sp.symbols('s')
K = sp.symbols('K', positive=True)
delta = sp.symbols('\delta')
q = [sp.symbols((str(e)+'^-', str(e)+'^+')) for e in q]
r = [sp.symbols((str(e)+'^-', str(e)+'^+')) for e in r]

qv = [[0.95, 1], [0.35, 0.4]]
rv = [[0.9, 1], [9, 12], [50, 100], [120, 150], [195, 200], [120, 130], [-delta, delta]]


N_kh = kh_gen(2)
N = [[q[1-x][N_kh[i][x]]*s**x for x in range(2)]for i in range(4)]
N = [[sum(n)] for n in N]

D_kh = kh_gen(7)
D = [[r[6-x][D_kh[i][x]]*s**x for x in range(7)]for i in range(4)]
D = [[sum(d)] for d in D]

NC = K - 4*s
DC = s

e = []
for i in range(4):
    for j in range(4):
        e.append(NC*N[i][0] + DC*D[j][0])
        
e = [ sp.Poly(sp.collect(sp.expand(elem), s), s) for elem in e]


# In[5]:


# substitute numeric values
for x in range(16):
    for i in range(len(qv)):
        for sign in range(2):
            e[x] = e[x].subs(q[i][sign], qv[i][sign])
    for i in range(len(rv)):
        for sign in range(2):
            e[x] = e[x].subs(r[i][sign], rv[i][sign])
            
e = [sp.Poly(expr, s) for expr in e]
rouths = [routh(poly) for poly in e]
rouths = [sp.simplify(routh.evalf(2)) for routh in rouths]


# In[5]:


# -- CHANGE DELTA


# In[44]:


DELTA = 0

rouths_delta = [routh.subs(delta, DELTA) for routh in rouths]
rngs = [sp.solve([l > 0 for l in rr[:, 0]], K) for rr in rouths_delta]
rngs_wf = [str(rng).replace("&", "&&") for rng in rngs]
rngs_wf = [str(rng).replace("|", "||") for rng in rngs_wf]
rngs_wf = [f'({rng})' for rng in rngs_wf]
rngs_wf_appnd = ' && '.join(rngs_wf)
rngs_p1 = rngs[:8]
rngs_p2 = rngs[8:]

rngs_wf_p1 = [str(rng).replace("&", "&&") for rng in rngs_p1]
rngs_wf_p1 = [str(rng).replace("|", "||") for rng in rngs_wf_p1]

rngs_wf_p2 = [str(rng).replace("&", "&&") for rng in rngs_p2]
rngs_wf_p2 = [str(rng).replace("|", "||") for rng in rngs_wf_p2]


rngs_wf_p1 = [f'({rng})' for rng in rngs_wf_p1]
rngs_wf_p2 = [f'({rng})' for rng in rngs_wf_p2]

rngs_wf_p1 = ' && '.join(rngs_wf_p1)
rngs_wf_p2 = ' && '.join(rngs_wf_p2)

print(rngs_wf_p1)
print()
print(rngs_wf_p2)


# In[ ]:


# by calling reduce on this on Mathematica:

# DELTA = 0
# 6.53978 < K < 47.1073

# DELTA = 5
# no solution

# DELTA = 2.5
# 20.5856 < K < 39.083

# DELTA = 3
# 25.9814 < K < 34.8391

# DELTA = 3.3
# no solution

# DELTA = 3.1
# 27.8532 < K < 33.2605

# DELTA = 3.2
# no solution

# DELTA = 3.15
# 29.7281 < K < 31.5061

# DELTA = 3.175
# no sol

# DELTA = 3.1625
# no sol

# DELTA = 3.15625
# no sol

# DELTA = 3.153125
# 30.0021 < K < 31.2396

# DELTA = 3.1546875
# 30.1995 < K < 31.0459

# DELTA = 3.15546875
# 30.3458 < K < 30.9016

# DELTA = 3.155859375
# 30.462 < K < 30.7863

# DELTA = 3.1560546875 -- MAX DELTA
# 30.5957 < K < 30.653

# DELTA = 3.15615234375
# no solution





# In[45]:


sp.latex(rouths[0])


# In[33]:


sp.latex(D[3][0])


# In[29]:


sp.latex(N[3][0])


# In[39]:


sp.latex(e[0])


# In[ ]:




