#1
#1.2
#AR : On essaie avec p=2.
#Pour trouver des coefficients qui correspondent Ã  un processus stationnaire, il suffit de dÃ©velopper un polynÃ´me dont les racines sont de module >1 (et dont le terme constant est 1). Par exemple : (1-X/2)^2=1-X+X^2/4. On peut donc prendre a1=1, a2=-1/4.
modele<-list(ar=(c(1,-1/4)))
n=500
x=arima.sim(modele,n)
plot(x)
#MA : On essaie avec q=2.
modele<-list(ma=(c(2,3)))
y=arima.sim(modele,n)
plot(y)

#1.3
acf(x,lag.max=20,type=c('correlation'))
acf(y,lag.max=20,type=c('correlation'))
#Les corrÃ©lations dÃ©croissent bien vers 0.
pacf(x,lag.max=20)
pacf(y,lag.max=20)
#Rien de sigificatif parce que p,q=2 (donc les auto-corrÃ©lations partielles doivent Ãªtre nulles).

#1.4
modele=list(ar=c(0.2,0.4,0.3), ma =c(0.5,0.2))
x=arima.sim(modele,n)
plot(x)
acf(x,lag.max=20)
pacf(x,lag.max=20)
# Si toutes les valeurs de xt sont >0 on va avoir des autocorrelations toujours >0 (et tendant vers 0). Les auto-corrÃ©lations partielles sont assez vite nulles parce que p, q sont petits. 

#1.5
modele=list(ar=c(0.2,0.4,0.3), ma =c(0.5,0.2),order=c(3,2,2))
x=arima.sim(modele,n)
plot(x)
acf(x,lag.max=20)
pacf(x,lag.max=20)
# Si toutes les valeurs de xt sont >0 on va avoir des autocorrelations toujours >0. On observe des auto-corrÃ©lations partielles nulles. 

#----------------------------------------------------------------------#

#2
#Vrai modÃ¨le pour serie1.dat :
#modele=list(ar=c(0.3,0.2,0.3),order=c(3,1,0))
#x=arima.sim(modele,n)

#2.1 
data=scan(file="http://math.unice.fr/~rubentha/enseignement/serie1.dat")
x=ts(data)
plot(x)
#Non, parce que la sÃ©rie n'a l'air stationnaire (la moyenne dÃ©croÃ®t).

#2.2 On remarque que diff(x) renvoie (x2-x1,x3-x2,...).
y=diff(x)

#2.3 
acf(y,lag.max=20)
#Les auto-correlations tendent vers 0.
pacf(y,lag.max=20)
#Les auto-correlations partielles sont nulles Ã  partir d'un certain rang.
#Donc on propose un modÃ¨le AR(3) pour y.



#2.4
out<-ar(y,aic=TRUE,order.max=NULL)
out
#On trouve :
#Coefficients:
 #    1       2       3  
#0.2720  0.2421  0.3183 

#2.5
# Faisons un test de niveau alpha=0,01.
Box.test(out$resid,lag=5)
#On trouve une p-valeur>alpha donc on conclut qu'on a bien un bruit blanc.

#2.6
#On propose le modÃ¨le pour x : ARIMA(3,1,0).


#2.7
#Vrai modele:
#modele=list(ma=c(0.2,-.5,0.6),order=c(0,2,3))
#x=arima.sim(modele,n)

data=scan(file="http://math.unice.fr/~rubentha/enseignement/serie2.dat")
x=ts(data)
plot(x)

#On voit que la serie x=serie2.dat n'est pas stationnaire (la moyenne n'est pas constante).
#On voit que y=diff(diff(x)) a l'air stationnaire (mais pas diff(x), parce que sa moyenne n'a pas l'air constante).
y=diff(x)
plot(y)
y=diff(diff(x))
plot(y)
acf(y,lag.max=20)
#Les auto-corrÃ©lations sont nulles Ã  partir d'un certain rang (4).
pacf(y,lag.max=20)
#Les auto-corrÃ©lations partielles tendent vers 0.
#On propose donc pour y un modÃ¨le MA(4).
out<-arima(y,order=c(0,0,3))
out$coef
#On trouve : -0.08355661 -0.30771185  0.56250498
# Faisons un test de niveau alpha=0,01.
Box.test(out$resid,lag=5)
#On trouve une p-valeur>alpha donc on conclut qu'on a bien un bruit blanc.

#----------------------------------------------------------------------#

#3
#3.1
#C'est un processus AR(3).

#3.2-3-4
P=50
n=100
biais=c(0,0,0,0,0)
variance=c(0,0,0,0,0)
modele=list(ar=c(1,-0.5,1.0/3))
for (i in 1:P)
{
	x=arima.sim(modele,n+5)
	y=window(x,1,n)
	out<-arima(y,order=c(3,0,0))
	p=predict(out,5)
	for (j in 1:5)
	{
		biais[j]=biais[j]+p$pred[j]-x[n+j]
		variance[j]=variance[j]+(p$pred[j]-x[n+j])^2
	}
}
biais=biais/P
variance=variance/P
print(biais)
print(variance)

#3.5 
P=200
n=250
biais=c(0,0,0,0,0)
variance=c(0,0,0,0,0)
modele=list(ar=c(1,-0.5,1.0/3))
for (i in 1:P)
{
	x=arima.sim(modele,n+5)
	y=window(x,1,n)
	out<-arima(y,order=c(3,0,0))
	p=predict(out,5)
	for (j in 1:5)
	{
		biais[j]=biais[j]+p$pred[j]-x[n+j]
		variance[j]=variance[j]+(p$pred[j]-x[n+j])^2
	}
}
biais=biais/P
variance=variance/P
print(biais)
print(variance)
# En principe, la variance de l'erreur diminue quand P (la taille de l'Ã©chantillon d'apprentissage) augmente. Ici, ce n'est pas le cas parce que P=50 constitue un Ã©chantillon assez grand pour bien estimer les coefficients. 

#----------------------------------------------------------------------#


#4
data<-scan("http://math.unice.fr/~rubentha/enseignement/sanfran.dat",skip=1)
x=ts(data,frequency=12)

#4.1
#La sÃ©rie n'est pas stationnaire, la moyenne semble  varier pÃ©riodiquement (pÃ©riode T=12). On applique l'opÃ©rateur Delta_T Ã  x.
y=diff.ts(x,lag=12,1)
#La sÃ©rie y a l'air stationnaire.

#4.2
#On utilise la fonction toute faite de R (qui minimise le critÃ¨re AIC).
out<-ar(y,aic=TRUE,order.max=NULL)
#Faisons un test de niveau alpha=0,02 sur les rÃ©sidus produits. 
Box.test(out$resid,lag=5)
#On trouve une p-valeur Ã  0,9997 > 0,02 donc on garde l'hypothÃ¨se "bruit blanc".
#On veut ensuite ne garder que les donnÃ©es jusqu'en 1963. On en profite pour les mettre en forme plus joliment.
x<-scan("http://math.unice.fr/~rubentha/enseignement/sanfran.dat",skip=1)
x=ts(x,frequency=12)
xw=window(x,c(1,1),c(32,12))

#4.3
out<-arima(xw,order=c(2,0,0),seasonal=list(order=c(2,0,0),period=12))
plot(out$resid)
#Faisons un test de niveau alpha=0,02 sur les rÃ©sidus produits. 
Box.test(out$resid,lag=5)
#On trouve une p-valeur Ã  0,8217 > 0,02 donc on garde l'hypothÃ¨se "bruit blanc".

#4.4
p=predict(out,3*12)
xr=window(x,c(30,1),c(35,12))
plot(xr)
lines(p$pred,col="red")

#4.5
#ModÃ¨le AR.
out=ar(xw,aic=TRUE,order.max=NULL)
p=predict(out,3*12)
#R n'arrive pas Ã  faire de prÃ©diction (erreur="bla ...").

#Holt-Winters sans composante saisonniÃ¨re.
#On essaie d'ajuster une droite Ã  la sÃ©rie. Comme la courbe de la sÃ©rie  n'est pas du tout une droite, on a intÃ©rÃªt Ã  prendre des coefficients proches de 1.
xlisse<-HoltWinters(xw,alpha=0.8,beta=0.8,gamma=FALSE)
p<-predict(xlisse,n.ahead=3*12)
plot(xr)
lines(p,col="red")

#Holt-Winters avec composante saisonniÃ¨re.
#La composante saisonniÃ¨re est un peu toujours la mÃªme donc on choisit gamma proche de 0 (pour prendre en compte beaucoup d'observations). Pour les autres coefficients (qui sont les paramÃ¨tres de la droite d'ajustement) on les prend proches de 1 parce que la courbe varie rapidement (elle ne ressemble pas Ã  une droite du tout).
xlisse<-HoltWinters(xw,alpha=0.8,beta=0.8,gamma=0.2,seasonal='add')
p<-predict(xlisse,n.ahead=3*12)
plot(xr)
lines(p,col="red")

#4.6 
Graphiquement, le meilleur modÃ¨le est le SARIMA(2,0,12).

#4.7
On pourrait aussi calculer la somme des carrÃ©s des erreurs (ce que je ne fais pas ici).

#----------------------------------------------------------------------#
 
#5
x=scan("http://math.unice.fr/~rubentha/enseignement/UKinterestrates.dat")
x=ts(x,start=c(1953,3),end=c(1995,12),frequency=12)
#La sÃ©rie n'a pas l'air stationnaire (la moyenne varie).
x1=diff(x)
#La sÃ©rie x1 a l'air stationnaire.
acf(x1,lag.max=20)
pacf(x1,lag.max=20)
#Les auto-corrÃ©lations partielles tendent vers 0 et les auto-corrÃ©lations  sont nulles Ã  partir du rang  2. Donc on propose un modÃ¨le MA(1) pour x1 (donc un modÃ¨le ARIMA(0,1) pour x).
out<-arima(x,order=c(0,1,1))
#Faisons un test de niveau alpha=0,02 sur les rÃ©sidus produits.
Box.test(out$resid,lag=5)
#On trouve une p-valeur Ã  0,7624 > 0,02 donc on garde l'hypothÃ¨se "bruit blanc".

#On peut aussi essayer de faire des prÃ©dictions.
#On commence par dÃ©couper x.
xw=window(x,c(1953,3),c(1993,12))
out<-arima(xw,order=c(0,1,1))
xr=window(x,c(1953,1),c(1995,12))
plot(xr)
p=predict(out,12*2)
lines(p$pred,col='red')
#Pas de prÃ©cision extraordinaire.
