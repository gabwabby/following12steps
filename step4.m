clear; close; clc;

syms x nu t 
phi = exp(-(x - 4*t)^2 / (4*nu*(t + 1))) + ...
      exp(-(x - 4*t - 2*pi)^2 / (4*nu*(t + 1)));

phiprime = diff(phi,x);

u = -2 * nu * (phiprime / phi) + 4;

ufunc = matlabFunction(u, 'Vars',[t, x , nu]); % wasnt giving me the result 
ufunc(1, 4, 3)

