import sympy as sp

from sympy import I as j
from sympy import latex
from sympy import gcdex

# Problem 1

## Part A

s, k, Q = sp.symbols('s k Q')
P = (4 * (s - 2)) / (s**2 - 2*s + 2) 

# Transform $P(s)$ to $\bar{P}(k)$ under the mapping $s = \frac{1-k}{k}$ 

P_bar = P.subs({s: (1-k)/k}).factor().cancel() 

n = P_bar.as_numer_denom()[0] 
d = P_bar.as_numer_denom()[1] 

# Using Euclid’s algorithm, find polynomials $x(k)$, $y(k)$ such that $nx + dy = 1$
x, y, _ = gcdex(n.as_poly(), d.as_poly())

x = (35/8)*k - 13/8 
y = (21/2)*k + 1 

N = n.subs({k: 1/(s+1)}).simplify() 
D = d.subs({k: 1/(s+1)}).simplify() 

X = x.subs({k: 1/(s+1)}).simplify() 
Y = y.subs({k: 1/(s+1)}).simplify() 

# by the Youla-Kucera parametrization theorem:
_C = (X + D*Q) / (Y - N*Q) 
C = _C.cancel().simplify().collect(Q) 


## Part B

q0, q1, q2 = sp.symbols('q0 q1 q2')

Q_ = (q2*s**2 + q1*s + q0) / ((s+3)**2) 

Psi = Y - N*Q_ 

eq1 = Psi.subs({s: 0}) 
eq2 = Psi.subs({s: 3*j}) 
eq3 = Psi.subs({s: -3*j}) 

sol = sp.solve([eq1, eq2, eq3], [q0, q1, q2]) 

Q_sol = Q_.subs({q0: -12.9375, q1: 12.4038, q2: -4.61058}) 

C_ = sp.N(C.subs(Q, Q_sol).cancel().collect(s), 4)
C_sol = C_.as_numer_denom()[0] / C_.as_numer_denom()[1] 

# Problem 2

## Part 1

Q_c = sp.symbols('Q_c')

W = (s+1)*X*N.collect(s) 
W.subs(s, 1-j).simplify()

term2 = (s+1)*N*(D*Q_c).factor() 

M = (s**2 - 2*s + 2) / (s**2 + 2*s + 1) 

Q_opt = (3.4495*(s - 0.4495)) / (s + 0.4495) 
Q_copt = Q_opt * ((s+1)/(-4*(s-2))).cancel() 

Q = sp.symbols('Q')
Copt = sp.N(C.subs(Q, Q_copt).simplify(), 3) 




