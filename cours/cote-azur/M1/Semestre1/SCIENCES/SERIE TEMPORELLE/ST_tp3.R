#setwd("/le/chemin/de/mon/script");
#source("ST_tp3.R")

#DonnÃ©es passager
#1b 
t=1:144
x=AirPassengers
n=length(x)
y=t*x
#On utilise les formules des moindres carrÃ©s.
a=(6/(n*(n-1)))*(-sum(y)+(2*n+1)*n*mean(x)/3)
b=(12/(n*(n^2-1)))*(sum(y)-(n+1)*n*mean(x)/2)
print(a)
print(b)
z=b*t+a
xn=as.numeric(x) #on transforme en vecteur pour contrÃ´ler l'Ã©chelle en abscisse
plot(t,xn,type='l')
lines(t,z,type='l',col='red')

#1c
xvect=as.numeric(x) #On met x sous forme vectorielle pour simplifier les manipulations.
residu=xvect-a-b*t
plot(t,residu,'l')
print(mean(residu))

#1d
autoco=acf(residu,lag.max=40,type=c("correlation"))
plot(autoco)
 
#2a
T=12
x1=diff.ts(x,lag=T,difference=1)
x2=diff.ts(x,lag=T,difference=2)
x3=diff.ts(x,lag=T,difference=3)
print(mean(x1))
print(mean(x2))
print(mean(x3))
# mean(x2) et mean(x3) sont du mÃªme ordre donc on en dÃ©duit que x2 est de moyenne nulle, donc la tendance est un polynÃ´me d'ordre 1 et que la pÃ©riode est 12 (on peut aussi regarder les graphiques pour s'en convaincre)
par(mfrow=c(3,1))
plot(x1)
plot(x2)
plot(x3)
 
#2b
Oui.

#3a
x_dec=decompose(x,type=c("multiplicative"))

#3b
plot(x_dec$random)
xrw=window(x_dec$random,c(1949,7),c(1960,6)) #On enlÃ¨ve les valeurs non dÃ©finies.
#Effectuons un test de niveau 0,95
Box.test(xrw,lag=20)
#On voit que la valeur de la statistique est au-dessus du seuil (0,05) donc on rejette l'hypothÃ¨se "bruit blanc".
autoco=acf(xrw,lag.max=40,type=c("correlation"))


#----------------------------------------------------------------------#


#DonnÃ©es simulÃ©es

#1
data=scan(file="http://math.unice.fr/~rubentha/enseignement/simulation.dat")
x=ts(data,frequency=1)
plot(x)

#2
T=20
x1=diff.ts(x,lag=T,difference=1)
x2=diff.ts(x,lag=T,difference=2)
x3=diff.ts(x,lag=T,difference=3)
print(mean(x1))
print(mean(x2))
print(mean(x3))
# mean(x2) et mean(x3) sont du mÃªme ordre donc on en dÃ©duit que x2 est de moyenne nulle, donc la tendance est un polynÃ´me d'ordre 1 et que la pÃ©riode est 20
# on peut aussi regarder les graphiques pour s'en convaincre
x=ts(x,frequency=20)
x_dec=decompose(x,type=c("additive"))
par(mfrow=c(4,1))
plot(x)
plot(x_dec$trend)
plot(x_dec$seasonal)
plot(x_dec$random)