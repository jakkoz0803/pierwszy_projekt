// Kozicki Jakub, informatyka, IO1, kolokwium 2, wersja B
clear;
clc;

// Dane testowe
n = 5;
a = -3.2;
b = 2.0;
xw = [-3.12, -2.09, -1.07, 0.01, 1.37, 1.91];
xp = 0.11;
xq = 1.1;
m = 13;

disp("n = "+string(n), "a = "+string(a), "b = "+string(b), "xw:", xw, "xp = "+string(xp), "xq = "+string(xq), "m = "+string(m));
disp("--------------");

function y = f(x);
    y = sin(x);
endfunction;

function y = fp(x);
    y = sin(x);
endfunction;

// omega, h
function y = omega(x,n,xw);
    for i = 0:n
        tw(i+1) = x - xw(i+1);
    end;
    y = prod(tw);
endfunction;

omega_xp = omega(xp,n,xw);
omega_xq = omega(xq,n,xw);

disp("omega_xp = "+string(omega_xp));
disp("omega_xq = "+string(omega_xq));

h = (b-a)/m;
disp("h = "+string(h));

// M(n+1)
for i = 1:m
    fptw(i) = abs(fp(a+i*h));
end;
M=max(fptw);
disp("M = "+string(M));

//
wynik_xp = (M/factorial(n+1)) * abs(omega(xp,n,xw)) ;
wynik_xq = (M/factorial(n+1)) * abs(omega(xq,n,xw)) ;
disp("wynik_xp = "+string(wynik_xp), "wynik_xq = "+string(wynik_xq));
