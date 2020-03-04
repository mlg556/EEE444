s = tf('s');

DELTA_MAX = 3.156;
K = 30.6;

P = (s + 0.35) / (s^6 + 10*s^5 + 60*s^4 + 140*s^3 + 200*s^2 + 125*s - (DELTA_MAX/2));
C = (K - 4*s)/s;

G = P*C;


bode(G)
