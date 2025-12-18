// EXERCICE-1
function[a,b,x]=f(a,b)
    x=a
    a=b
    b=x
    disp("a",a,"b",b)
endfunction
    
//EXERCICE-2
function [A, n, a, b, c]=matrice(n)
    a=diag([ones(n-1,1);2])
    b=-diag(ones(n-1,1),-1)
    c=-diag(ones(n-1,1),+1)
    A=(a+b+c )
end
function [A, T]=matric(n)
A=rand(n,n)
T=triu(A)-diag(diag(A))+eye(n,n)
disp(T)
end
function [y]=mt(x)
y= (2*x*x)-(3*x) + 1
disp(x)
end
function [b, y]=Sl(A, C)
    b=triu(A)
    y=b \C  
    disp(y) 
  end
