w = linspace(0, 10, 500);

G = ((1i.*w).^7 + 10.*(1i.*w).^6 + 60.*(1i.*w).^5 + 140.*(1i.*w).^4 + 200.*(1i.*w).^3 + 125.*(1i.*w).^2 - 1.578.*(1i.*w)) ...
    ./ ((1i.*w).^7 + 10.*(1i.*w).^6 + 60.*(1i.*w).^5 + 140.*(1i.*w).^4 + 200.*(1i.*w).^3 + 121.*(1i.*w).^2 + 27.62.*(1i.*w) + 10.71);

plot(w, abs(G), 'LineWidth', 2);
title('Magnitude of the sensitivity function.')
ylabel('|S(j\omega)|')
xlabel('\omega')
grid on;
