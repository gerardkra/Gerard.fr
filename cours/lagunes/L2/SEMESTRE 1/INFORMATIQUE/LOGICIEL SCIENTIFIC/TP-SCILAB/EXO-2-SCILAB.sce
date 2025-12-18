function [a,b,c,d,cc]=f(n)
    a=-diag(ones(n-1,1),-1)
    d=diag([ones(n-1,1);2])
    c=a+d
    b=-diag(ones(n-1,1),1)
    cc=b+c
endfunction
