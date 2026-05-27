clear; close; clc;
nx = 41; dx = 2 / (nx -1); nt = 20; dt = 0.025; c = 1; 

u = ones(1,nx)
u(round(0.5/dx) + 1 : round(1/dx) + 1) = 2;

un = ones(1,nx);

for n = 1:nt
    un = u;
    for i = 2:nx
        u(i) = un(i) - un(i) * dt/dx *  (un(i) - un(i-1)) % this is again following
        % that one based index difference seen in step 1 
    end
end

x = linspace(0,2,nx);
y = u;
plot(x,y)