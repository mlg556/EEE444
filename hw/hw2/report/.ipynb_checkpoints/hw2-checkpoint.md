---
papersize: a4
geometry: margin=2cm
fontsize: 12pt
title: |
	| EEE444 Homework \#2
author: Miraç Lütfullah Gülgönül
date: 4 March 2020
header-includes:
   - \usepackage{xcolor}
   - \usepackage{fancyhdr}
   - \pagestyle{fancy}
   - \lhead{Miraç L. Gülgönül}
   - \rhead{EEE444 Homework \#2}
---

# PART I

We can write $\delta$ as:
$$
\delta = P_{\delta} - P = \frac{e^{-hs}}{\tau s - 1} - \frac{1}{0.2s-1}
$$
After this, we can plot $|\delta(j\omega)|$ for the possible values of $\tau \in [0.2,0.25]$ and $h \in [0,0.05]$.

![$|\delta|$ vs $\omega$](p0.pdf)

\newpage

By numerical trial/error I can also plot
$$
|W_a(j\omega)| = \left|\frac{a_1j\omega} {(a_2j\omega + 1)^2}\right|
$$
for different values of $a_1,a_2 >0$ and check if $|W_a| > |\delta|$ for all $\omega$ and also $|W_a|$ is minimal. I have found this to happen at $a_1 = 0.045$ and $a2 = 0.066$. Below is the result:

![$|\delta| \text{ and } |W_a|$](p1.pdf)

\newpage

And here is the plot when the x axis is logarithmic:

![$|\delta| \text{ and } |W_a|$ with logarithmic x axis.](p2.pdf)

# PART II

For the controller
$$
C(s) = \frac{15s+1}{\beta s}
$$
to be robustly stabilizing $(C,P_{\Delta})$ for all $P_{\Delta} \in P$: it has to satisfy the following conditions:

1. $(C,P)$ must be stable

2. $|WCS| < 1$ for all $\omega$.

For the first condition we have:
$$
\begin{gathered}
P(s) = \frac{1}{0.2s-1}, \quad C(s) = \frac{15s+1}{\beta s}
\\
G(s) = \frac{PC}{1+PC} = \frac{15 s + 1}{B s \left(0.2 s - 1\right) + 15 s + 1}
\\
D(s) = 0.2 B s^{2} + \left(15.0 - 1.0 B\right) s + 1.0
\end{gathered}
$$

Constructing the Routh-Hurwitz array for $D(s)$:
$$
\left[\begin{matrix}0.2 B & 1.0\\15.0 - 1.0 B & 0\\1 & 0\end{matrix}\right]
$$

For the first column to be greater than $0$, we have the condition
$$
0 < \beta < 15
$$

For the second robustness condition, we can construct $|WCS|$ as:
$$
\begin{gathered}
W = \frac{a_1j\omega} {(a_2j\omega + 1)^2} = \frac{0.045 j w}{\left(0.066 j w + 1\right)^{2}}
\\
P = \frac{1}{0.2j\omega-1}, \quad C = \frac{15j\omega+1}{\beta s}
\\
S = (1 + PC)^{-1} = \frac{\beta w \left(0.2 j w - 1\right)}{\beta w \left(0.2 j w - 1\right) + 15 w - i}
\\
|WCS| = \frac{0.045 w \sqrt{9.0 w^{4} + 225.04 w^{2} + 1} \sqrt{\frac{1}{0.04 \beta^{2} w^{4} + \beta^{2} w^{2} - 30.4 \beta w^{2} + 225 w^{2} + 1}}}{\sqrt{1.8974736 \cdot 10^{-5} w^{4} + 0.008712 w^{2} + 1}}
\end{gathered}
$$
By numerically plugging in different values for $\beta$, we can see when the condition $|WCS| < 1$ is satisfied.

![|WCS| for different values of $\beta$](p3.pdf)

As can be seen, somewhere between $\beta=4$ and $5$ the magnitude seems to start getting lower than 1. More precisely, I have found this value to be $\beta = 4.261$.

Combining both conditions, for the controller to be robustly stabilizing $(C,P_{\Delta})$ for all $P_{\Delta} \in P$, I have found that $4.261 < \beta < 15$.

\newpage

# PART III

## Padé Approximation Approach

Noting that $P_1$ is a time-delayed plant, we can deconstruct it as:
$$
P_1 = \frac{e^{- h s}}{0.25 s - 1} = P_0P_d
$$
where
$$
P_0 = \frac{1}{0.25 s - 1}, \qquad P_d = e^{-hs}
$$
The term $P_d$ is non-polynomial, and thus has to be approximated by a polynomial using *Padé approximation*. Just to be on the safe side, let us use the 10th order approximation:
$$
P_d = e^{-hs} \approx P_a
$$
where
$$
P_a = \frac{\frac{h^{10} s^{10}}{670442572800} - \frac{h^{9} s^{9}}{6094932480} + \frac{h^{8} s^{8}}{112869120} - \frac{h^{7} s^{7}}{3255840} + \frac{7 h^{6} s^{6}}{930240} - \frac{7 h^{5} s^{5}}{51680} + \frac{7 h^{4} s^{4}}{3876} - \frac{h^{3} s^{3}}{57} + \frac{9 h^{2} s^{2}}{76} - \frac{h s}{2} + 1}{\frac{h^{10} s^{10}}{670442572800} + \frac{h^{9} s^{9}}{6094932480} + \frac{h^{8} s^{8}}{112869120} + \frac{h^{7} s^{7}}{3255840} + \frac{7 h^{6} s^{6}}{930240} + \frac{7 h^{5} s^{5}}{51680} + \frac{7 h^{4} s^{4}}{3876} + \frac{h^{3} s^{3}}{57} + \frac{9 h^{2} s^{2}}{76} + \frac{h s}{2} + 1}
$$


Choosing $\beta = 4.5$, we can construct the system with :
$$
C(s) = \frac{15s+1}{4.5s}, \qquad P(s) = P_0P_a, \qquad G  = \frac{PC}{1+PC}
$$

The denominator polynomial $D(s)$ of the system is:

$$
\small
\begin{gathered}
D(s) = 3.64148451940312 \cdot 10^{-26} s^{12} + 8.04525313153463 \cdot 10^{-23} s^{11} + \\ 8.51330851197038 \cdot 10^{-20} s^{10} + 6.07958237746093 \cdot 10^{-17} s^{9} + \\ 2.83545747745511 \cdot 10^{-14} s^{8} + 1.08562400350004 \cdot 10^{-11} s^{7} + \\ 2.63845814580706 \cdot 10^{-9} s^{6} + 5.74573497162023 \cdot 10^{-7} s^{5} + \\ 6.45127422313955 \cdot 10^{-5} s^{4} + 0.00694030214424951 s^{3} + 0.141732456140351 \\ s^{2} + 2.32777777777778 s + 0.222222222222222
\end{gathered}
$$



Constructing the Routh-Hurwitz array for $D(s)$:
$$
\small
\left[\begin{matrix}3.64148451940312 \cdot 10^{-26} & 8.51330851197038 \cdot 10^{-20} & 2.83545747745511 & \dots
\\
8.04525313153463 \cdot 10^{-23} & 6.07958237746093 \cdot 10^{-17} & 1.08562400350004 \cdot 10^{-11}  & \dots
\\
5.76153616248595 \cdot 10^{-20} & 2.3440766671805 \cdot 10^{-14} & 2.37839168662087 & \dots
\\
2.80637717396288 \cdot 10^{-17} & 7.53511826726918 \cdot 10^{-12} & 4.8887615452316 & \dots
\\
4.23708643387235 \cdot 10^{-10} & 2.8995689473794 \cdot 10^{-5} & 0.129019148023105 & \dots
\\
1.37114900321653 \cdot 10^{-7} & 0.00544473196071004 & 2.32527158375522 & \dots
\\
1.21705305212096 \cdot 10^{-5} & 0.121833658583602 & 0.222222222222222 & \dots
\\
0.00407213691044493 & 2.32276799709594 & 0 & \dots
\\
0.114891524901938 & 0.222222222222222 & 0 & \dots
\\
2.31489170409517 & 0 & 0 & \dots
\\
0.222222222222222 & 0 & 0 & \dots
\end{matrix}\right]
$$
As can be seen, all of the elements of the first column are $>0$, albeit barely, as the first entry is in the order of $10^{-26}$. By the Routh-Hurwitz theorem, this proves $(C,P)$ is stable where:
$$
C(s) = \frac{15s+1}{4.5s}, \qquad P(s) = \frac{e^{- h s}}{0.25 s - 1}
$$

\newpage



## Bode Plot Approach

As an alternative approach, I directly constructed and analyzed the Bode plot of the system to judge stability of the system where:
$$
C(s) = \frac{15s+1}{4.5s}, \qquad P(s) = \frac{e^{- h s}}{0.25 s - 1}
$$

![Bode plot of the system.](bode.pdf)

Defining the phase crossover frequency $\omega_{pc}$ as the frequency where phase shift is equal to -180, The *Bode Stability Criterion* states that if at $|H(j\omega_{pc})| < 0{dB}$, then the system is stable.

Figure 5 shows that this is indeed the case where $\omega_{pc} = 28.6286$ and $|H(j\omega_{pc})| = -1.34{dB}$.

Both approaches agree that the system is robustly stable.

\newpage

# PART IV

By plugging in the values the robust performance condition at $\gamma_r = 10$:
$$
\left|\frac{W_r}{\gamma_r}S\right| + |WCS| \leq 1 \quad \forall \omega
$$
the condition becomes:
$$
\footnotesize
\begin{gathered}
\frac{\left(\beta \sqrt{7.59 \cdot 10^{-7} w^{6} + 0.0003 w^{4} + 0.05 w^{2} + 1} + 0.45 w \sqrt{9.0 w^{4} + 225 w^{2} + 1}\right) \sqrt{\frac{1}{0.04 \beta^{2} w^{4} + \beta^{2} w^{2} - 30.4 \beta w^{2} + 225 w^{2} + 1}}}{10 \sqrt{1.9 \cdot 10^{-5} w^{4} + 0.008 w^{2} + 1}} \leq 1
\end{gathered}
$$
As done in the previous parts, we can plot this magnitude using different values of $\beta$:

![Robust performance condition for different values of $\beta$.](p4.pdf)



\newpage

Zooming in further, we can see that at the higher values of $\beta$, the magnitude stays high at very low frequencies so they do not satisfy the performance condition.

![Robust performance condition, zoomed in.](p5.pdf)

More specifically the range of acceptable values for $\beta$ while $\gamma_r = 10$ is $4.44 < \beta < 9.88$.

I have also found that for $\gamma_r = 4.445$ this range reduces to $4.42 < \beta <4.45$. So the smallest value of $\gamma_r$ the corresponding value of $\beta$ for which there exists a $\beta$ satisfying the robust performance condition are:
$$
\gamma_r = 4.445, \quad \beta = 4.43
$$

# Notes

All related files can be found at:

https://github.com/mlg556/EEE444
