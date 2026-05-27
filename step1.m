clear; close; clc;
nx = 41; dx = 2 / (nx -1); nt = 25; dt = 0.025; c = 1; 

u = ones(1,nx)
%py.u(int(.5 / dx):int(1 / dx + 1)) == 2;
%u(11:21) = 2
u(round(0.5/dx) + 1 : round(1/dx) + 1) = 2;
%its like python, but matlab uses different indexing where is includes the
%endpoint so you have to add + 1 at the start...?
%print(u)

x = linspace(0,2,nx)
y = u
plot(x,y)