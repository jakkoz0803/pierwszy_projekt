// Kozicki Jakub, informatyka, informatyka ogólna, grupa IO1, kolokwium nr 1 wersja A
clear;
clc;
disp("Jakub Kozicki, informatyka, rok 3, informatyka ogólna");

// 5
for i=0:4
    x(i+1)=cos(i-1);
end;

// 6
y=x';
disp(y);

// 7
for i=0:6
    z(2*i+2)=exp(sin(i));
    disp(z(2*i+2));
end;

// 8
function a=f(x,y);
    a=sin(x)^2+cos(y)^2;
endfunction;

// 9
disp(f(0.15,1.15));

// 10
for i=1:3
    for j=1:3
        M(i,j)=1/(i+j)
    end;
end;

// 11
function y=det2(M);
    y=M(1,1)*M(2,2)-M(2,1)*M(1,2);
endfunction;

// 12
A=[1 2; 2 3];
wyznacznik=det2(A);
disp(wyznacznik);

// 13
function y=g(x);
    if x<0 then
        y=exp(x);
    else
        y=cos(x)+sin(x);
    end;
endfunction;

// 14
// wykres pokazuje tylko y=cos(x)+sin(x), coś jest źle
punkty=linspace(-5,5,100);
plot(punkty,g);

// 15
/*function y=fi(x);
    licznik=
endfunction;*/
