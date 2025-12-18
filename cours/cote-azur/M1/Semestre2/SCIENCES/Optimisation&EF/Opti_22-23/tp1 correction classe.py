funcprot(0)

//------------------------------------------------------------------------------
//------------------------------------------------------------------------------
//EXO 1
//------------------------------------------------------------------------------
//------------------------------------------------------------------------------

 function [u, fu, nit] = newton( u0, f, df, nitmax, eps )
   
   u = u0 ; 
   nit = 0 ;
   fu = f(u) ;
   dfu = df(u) ;
   us = u + ones(u) ;
   while( norm( u - us ) > eps & nit < nitmax )
       us = u ;
       u = u - dfu\fu ;
       fu = f(u) ;
       dfu = df(u) ;
       nit = nit + 1 ; 
   end
       
 endfunction

function y=f(x)
    y = exp(-x) - x ;
endfunction
function y=df(x)
    y = -exp(-x) - ones(x) ;
endfunction

//Un graphique pour se faire une idée du comportement de f
x = linspace(-5,5)
scf(0);clf() ; title('Exo 1, question 1') 
plot(x,f(x))
plot(x,zeros(x),'r')
//on reserre l'intervalle
x = linspace(0,1) 
scf(1); clf() ; title('Exo 1, question 1') 
plot(x,f(x))
plot(x,zeros(x),'r')
//--> on voit que la fonction s'annule en un point x compris entre 0.55 et 0.6

//Appel a la méthode de Newton pour le calculer
u0 = 0.0
nitmax = 100
eps = 1e-8 
[u, fu, nit] = newton( u0, f, df, nitmax, eps )
printf( 'La methode de Newton renvoie x = %f en %d iterations. La fonction f vaut %.1e en ce point.\n', u, nit, fu )

//Avec un point de départ u0 différent
u0 = 10.0
[u, fu, nit] = newton( u0, f, df, nitmax, eps )
printf( 'La methode de Newton renvoie x = %f en %d iterations. La fonction f vaut %.1e en ce point.\n', u, nit, fu )

//Dans cet exemple, la méthode de Newton semble converger rapidement quel que soit le point de départ.
printf('\n')

function y=g(x)
    y = x.^2 - 2*ones(x) ;
endfunction
function y=dg(x)
    y = 2*x ;
endfunction

//Il n'est pas nécessaire de faire de graphique. La fonction s'annulle en + ou - sqrt(2)

//Appel a la méthode de Newton pour le calculer
u0 = 1e-6 // il ne faut pas mettre 0, la dérivée s'annule en ce point
nitmax = 100
eps = 1e-8 
[u, fu, nit] = newton( u0, g, dg, nitmax, eps )
printf( 'La methode de Newton renvoie x = %f en %d iterations. La fonction f vaut %.1e en ce point.\n', u, nit, fu )

//Avec un point de départ u0 différent
u0 = -1e-6
[u, fu, nit] = newton( u0, g, dg, nitmax, eps )
printf( 'La methode de Newton renvoie x = %f en %d iterations. La fonction f vaut %.1e en ce point.\n', u, nit, fu )

//Selon le point de départ la méthode de Newton converge vers l'une ou l'autre des racines
printf('\n')

function y=h(x)
    y = zeros(2,1)
    y(1) = exp(x(1)) - x(2) ;
    y(2) = x(1)^2+x(2)^2- 16 ;
endfunction
function y=dh(x)
    y = zeros(2,2)
    y(1,1) = exp(x(1)) ;
    y(1,2) = - 1 ;
    y(2,1) = 2*x(1) ;
    y(2,2) = 2*x(2) ;
endfunction

//Nous cherchons les zeros de h, c'est a dire les points tels que
//exp(x)=y et x^2+y^2=16 ils sont a l'intersection de deux courbes
scf(2) ; clf() ; title('Exo 1, question 3') 
x = linspace(-4,4)
plot(x,sqrt(16-x.^2),'b')
plot(x,-sqrt(16-x.^2),'b')
x=linspace(-4.5,2)
plot(x,exp(x),'r')
ha = gca()
ha.isoview='on'

//On voit sur le graphique qu'il y a deux couples à trouver ~(-4,0) et ~(1.4,3.7)
//on peut choisir des données initiales appropriees pour converger vers chacune des solutions

//Appel a la méthode de Newton pour les calculer
u0 = [-4;0]
nitmax = 100
eps = 1e-8 
[u, fu, nit] = newton( u0, h, dh, nitmax, eps )
printf( 'La methode de Newton renvoie x = (%6.4f,%6.4f) en %d iterations. La fonction f vaut %.1e en ce point.\n', u(1), u(2), nit, fu )

u0 = [1;4]
nitmax = 100
eps = 1e-8 
[u, fu, nit] = newton( u0, h, dh, nitmax, eps )
printf( 'La methode de Newton renvoie x = (%6.4f,%6.4f) en %d iterations. La fonction f vaut %.1e en ce point.\n', u(1), u(2), nit, fu )


//------------------------------------------------------------------------------
//------------------------------------------------------------------------------
//EXO 2
//------------------------------------------------------------------------------
//------------------------------------------------------------------------------

scf(3) ; clf() ; title('Exo 2, f1')
x = linspace(-5,5)
plot(x,x./(x.^2+ones(x)))
//Sur [-5,5] pour f1 : 2 minima locaux (en ~-1 et 5), 2 maxima locaux (en ~1 et -5),
//1 miminum global en ~-1 et 1 maximum global en ~1
scf(4) ; clf() ; title('Exo 2,f2')
x = linspace(-5,5)
plot(x,2*x.^3-3*x.^2-12*x+4*ones(x))
//Sur [-5,5] pour f2 : 2 minima locaux (en ~-2 et -5), 2 maxima locaux (en ~-1 et 5),
//1 miminum global en -5 et 1 maximum global en 5
scf(5) ; clf() ; title('Exo 2,f3')
x = linspace(-5,5)
plot(x,x.*( sin(x)-(sin(1)+cos(1))*ones(x)) )
//Sur [-5,5] pour f3 : 2 minima locaux (en ~--4.5 et 5), 2 maxima locaux (en ~-2.5 et -5),
//1 miminum global en ~-5 et 1 maximum global en ~-2.5
//ce qui se passe autour de 1 est difficile a identifier sur le graphique
//on dirait qu'il n'y a ni minimum, ni maximum locaux

//NB : sur [-5,5], les trois fonctions ont des miminum et maximum globaux. 
//Une fonction continue sur un compact atteint ses bornes.

//On elargit un peu les graphes pour intuiter ce qui se passe sur R
scf(6) ; clf() ; title('Exo 2, f1')
x = linspace(-10,10)
plot(x,x./(x.^2+ones(x)))
//Sur R pour f1 : 1 minimum local et global en ~-1, 1 maximum local et global en ~1,
scf(7) ; clf() ; title('Exo 2,f2')
x = linspace(-10,10)
plot(x,2*x.^3-3*x.^2-12*x+4*ones(x))
//Sur [-5,5] pour f2 : 1 minimum local (en ~-2 ), 1 maximum local (en ~-1),
//pas de miminum ou maximum global
scf(8) ; clf() ; title('Exo 2,f3')
x = linspace(-10,10)
plot(x,x.*( sin(x)-(sin(1)+cos(1))*ones(x)) )
//une infinité de maxima et minima globaux
//pas de miminum ou maximum global

scf(9) ; clf() ; title('Exo 2, f1')
x = linspace(-5,5)
plot(x,x./(x.^2+ones(x)),'b')
plot(x,(1-x.^2)./(1+x.^2).^2,'r')
plot(x,zeros(x),'k')
legend(['f1' 'f1'''])
scf(10) ; clf() ; title('Exo 2,f2')
x = linspace(-5,5)
plot(x,2*x.^3-3*x.^2-12*x+4*ones(x),'b')
plot(x,6*x.^2-6*x-12,'r')
plot(x,zeros(x),'k')
legend(['f2' 'f2'''])
scf(11) ; clf() ; title('Exo 2,f3')
x = linspace(-5,5)
plot(x,x.*( sin(x)-(sin(1)+cos(1))*ones(x)),'b' )
plot(x,x.*cos(x) + (sin(x)-(sin(1)+cos(1))*ones(x)),'r' )
plot(x,zeros(x),'k')
legend(['f3' 'f3'''])

//Si f une fonction C^1 definie sur [a,b] possède un extremum local en c dans ]a,b[ alors
//f'(c)=0. 
//NB: cet enoncé n'est pas valable aux bornes de l'intervalle
//Une autre facon de le fomuler est que si l'on recherche un extremum local d'une
//fonction f C^1 il suffit de chercher les candidats soit aux endroits ou la derivee s'annule
//soit aux bornes de l'intervalle.

scf(12) ; clf() ; title('Exo 2, f1')
x = linspace(-5,5)
plot(x,x./(x.^2+ones(x)),'b')
plot(x,(1-x.^2)./(1+x.^2).^2,'r')
plot(x,(2*x.*(x.^2-3)./(1+x.^2).^3),'m')
plot(x,zeros(x),'k')
legend(['f1' 'f1''' 'f1'''''])
scf(13) ; clf() ; title('Exo 2,f2')
x = linspace(-5,5)
plot(x,2*x.^3-3*x.^2-12*x+4*ones(x),'b')
plot(x,6*x.^2-6*x-12,'r')
plot(x,12*x-6,'m')
plot(x,zeros(x),'k')
legend(['f2' 'f2''' 'f2'''''])
scf(14) ; clf() ; title('Exo 2,f3')
x = linspace(-5,5)
plot(x,x.*( sin(x)-(sin(1)+cos(1))*ones(x)),'b' )
plot(x,x.*cos(x) + (sin(x)-(sin(1)+cos(1))*ones(x)),'r' )
plot(x, 2*cos(x) - x.*sin(x),'m' )
plot(x,zeros(x),'k')
legend(['f3' 'f3''' 'f3'''''])

//Si f est une fonction C^2 definie sur [a,b] et c dans ]a,b[ tel que
//f'(c)=0 alors si f''(c) n'est pas nul son signe nous permet de conclure en 
//l'existence d'un extrememum local en c et s'il s'agit d'un miminum ou d'un maximum
//Si f''(c)>0 alors il s'agit d'un minimum
//Si f''(c)<0 alors il s'agit d'un maximum
//Si f''(c)=0 alors on ne peut pas conclure, il peut très bien y avoir un extremum en c ou non.

//NB : lorsque la dimension est strictement plus grande que 1, il y a aussi la possibilité d'avoir des points selle. 

//Il est possible d'identifier les zeros de f' a l'aide de la méthode de Newton.

printf('\n')

function y=f1(x)
   y=x./(x.^2+ones(x)) 
endfunction
function y=df1(x)
   y= (1-x.^2)./(1+x.^2).^2
endfunction
function y=d2f1(x)
   y=(2*x.*(x.^2-3)./(1+x.^2).^3)
endfunction
//Identifions les deux zeros de f1p
u0 = -1.1
nitmax = 100
eps = 1e-8 
[z1, fz1, nit] = newton( u0, df1, d2f1, nitmax, eps )
u0 = 1.1 
[z2, fz2, nit] = newton( u0, df1, d2f1, nitmax, eps )
zvec = [ z1 z2 ]
for z=zvec
if( d2f1(z) > 1e-14 ) then
    printf( 'f1 atteint un minimum en %f\n', z )
elseif( d2f1(z) < -1e-14 ) then
    printf( 'f1 atteint un maximum en %f\n', z )
else
    printf( 'Difficile de conclure a l''existence d''un extrememum, la derivee seconde en %f est nulle\n', z)
end
end

printf('\n')

function y=f2(x)
    y=2*x.^3-3*x.^2-12*x+4*ones(x)
endfunction
function y=df2(x)
    y=6*x.^2-6*x-12
endfunction
function y=d2f2(x)
    y=12*x-6
endfunction

//Identifions les deux zeros f2p
u0 = -2
nitmax = 100
eps = 1e-8 
[z1, fz1, nit] = newton( u0, df2, d2f2, nitmax, eps )
u0 = 3
[z2, fz2, nit] = newton( u0, df2, d2f2, nitmax, eps )
zvec = [ z1 z2 ]
for z=zvec
if( d2f1(z) > 1e-14 ) then
    printf( 'f2 atteint un minimum en %f\n', z )
elseif( d2f1(z) < -1e-14 ) then
    printf( 'f2 atteint un maximum en %f\n', z )
else
    printf( 'Difficile de conclure a l''existence d''un extrememum, la derivee seconde en %f est nulle\n', z)
end
end

//------------------------------------------------------------------------------
//------------------------------------------------------------------------------
//EXO 3
//------------------------------------------------------------------------------
//------------------------------------------------------------------------------

//Ce sont toutes des formes quadratiques
A1 = [ 2 0.5 ; 0.5 2 ]
A2 = [ 1 .05 ; 0.5 -2 ]
A3 = [ 6 1.5 ; 1.5 2 ]
A4 = [ -2 0.5 ; 0.5 -3.5 ]

sp1 = spec(A1) ; sp2 = spec(A2) ; sp3 = spec(A3) ; sp4 = spec(A4) ;
//Les matrices A1 et A3 ont deux vp positives
//La matrice A4 a deux vp negatives
//La matrice A2 a une valeur propre positive et une négative.

x = linspace(-1,1) ; y = x ;
[xx,yy]=meshgrid(x,y) ;

scf(15) ; clf() ; title('Exo 3, question 3 f1')
zz1 = xx.^2 + xx.*yy+2*yy.^2 ;
surf( xx,yy, zz1 )
scf(16) ; clf() ; title('Exo 3, question 3 f1')
contour( x,y, zz1', 20 )


scf(17) ; clf() ; title('Exo 3, question 3 f2')
zz1 = xx.^2 + xx.*yy-2*yy.^2 ;
surf( xx,yy, zz1 )
scf(18) ; clf() ; title('Exo 3, question 3 f2')
contour( x,y, zz1', 20 )


scf(19) ; clf() ; title('Exo 3, question 3 f3')
zz1 = 6*xx.^2 + 3*xx.*yy+2*yy.^2 ;
surf( xx,yy, zz1 )
scf(20) ; clf() ; title('Exo 3, question 3 f3')
contour( x,y, zz1', 20 )


scf(21) ; clf() ; title('Exo 3, question 3, f4')
zz1 = -2*xx.^2 + xx.*yy-7/2*yy.^2 ;
surf( xx,yy, zz1 )
scf(22) ; clf() ; title('Exo 3, question 3, f4')
contour( x,y, zz1', 20 )

//Les formes quadratiques sont de la forme f(x) = (Ax,x).
//La derivee s'ecrit alors f'(x) = 2 Ax
//etla derivee seconde f''(x) = 2A.

//Le seul candidat pour etre un extrememum local est x = 0 (solution  de 2Ax=0 avec
//A inversible)
//Les signes des valeurs propres de A permettent d'identifier leur nature.

//f1 et f3 atteignent en 0 un minimum global
//f4 atteint en 0 un maximum global
//f2 a un point selle en 0, dans une direction la fonction est maximale alors 
//que dans l'autre elle est minimale

//------------------------------------------------------------------------------
//------------------------------------------------------------------------------
//EXO 4
//------------------------------------------------------------------------------
//------------------------------------------------------------------------------

//La fonction admet un minimum global en (0,0)


x = linspace(-2,2) ; y = x ;
[xx,yy]=meshgrid(x,y) ;

scf(23) ; clf() ; title('Exo 4, question 2')
zz1 = xx.^2 + yy.^2 ;
surf( xx,yy, zz1 )
scf(24) ; clf() ; title('Exo 4, question 2')
contour( x,y, zz1', [ 1 2 3 ] )

//grad g(x,y) = 2*(x,y)

plot( [0 0], [1 1.5], 'k' )
plot( [ 1 1.5 ], [ 1 1.5 ], 'b' )
plot( [ sqrt(3) 1.5*sqrt(3) ], [ 0 0 ], 'g' )

//Suivre l'oppposé du gradient permet de trouver une direction suivant laquelle
//la fonction diminue.