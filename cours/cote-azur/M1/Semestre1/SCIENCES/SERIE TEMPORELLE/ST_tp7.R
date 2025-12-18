#TP 7

#Essai de simulation 
a0=1
a1=0.5
n=300
sigma=1
x=c(1)
for (i in 1:n)
{
	sigma=a0+a1*x[length(x)]^2
	x=c(x,sqrt(sigma)*rnorm(sigma))
}

#1
#1.1
dax <- diff(log(EuStockMarkets))[,"DAX"]
dax2=dax^2
mm=0
m=0
q=0
for (i in 1:2)
{
	for (j in 0:i)
	{
		serie<-arima(dax2,order=c(i,0,j))
		print(i);print(j);print(serie$aic)
		if ((serie$aic) < mm)
		{
			mm=serie$aic
			m=i
			q=j
		}
	} 
}
print(m);print(q);print(mm)
#On trouve m=2, q=2 donc p est dans {0,1,2}. Donc le processus est dans la classe GARCH(2,2). Si on trouve a2=0, a1<>0, on pourra dire qu'il est dans la classe GARCH(1,2) (... etc ...).

library(tseries)
serie<-garch(dax,order=c(2,2))
serie$coef #On affiche les coefficients estimÃ©s. 
#Comme a1, a2 sont du mÃªme ordre que b1, b2, on dÃ©cide que p=2, q=2.

#1.2
#Choisissons un niveau alpha=0.02 pour le test.
Box.test(serie$residuals)
#La p-valeur affichÃ©e est > alpha donc on reste sur (H0) (les rÃ©sidus forment bien un bruit blanc).

#2
#2.1
x=scan(file="http://math.unice.fr/~rubentha/enseignement/nyse.dat")
serie<-garch(x,order=c(1,1))
serie$coef

#2.2
xw=window(x,start=900,end=1000)
plot.ts(xw)
# Sachant X_{t-1}, X_{t-2}, â€¦, X_{t} est une gaussienne de variance sigma_{t}^2. Il est donc facile de calculer m telle que X_{t} (sachant â€¦) est dans [-m;m] avec proba 0,32 (en s'aidant de la table de la loi normale).
fi=window(0.47*serie$fitted.values,start=900,end=1000)
fi1=fi[,1]
plot.ts(fi1,ylim=c(-0.07,0.07))
lines(-fi1)
lines(xw,col='red')
