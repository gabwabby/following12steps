clear; close; clc;

nx = 41; dx = 2 / (nx - 1); nt = 20; nu = 0.3; sigma = 0.2; dt = sigma * dx^2 / nu; 

u = ones(1,nx); 
u(round(0.5/dx) + 1 : round(1/dx) + 1) = 2;

un = ones(1,nx);

for n = 1:nt 
    un = u; 
    for i = 2:nx-1 % note to self 
        % python nx - 1 stops before nx-1 so nx -2, but matlab stops @ nx -
        % 1
        % giwecer, the shift on the left makes them cancel each other
        % out...
        u(i) = un(i) + nu * dt/dx^2 * (un(i+1) - 2*un(i) + un(i-1));
    end
end

x = linspace(0,2,nx);
y = u;
plot(x,y)


