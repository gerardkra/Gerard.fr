# EXERCICE 2.1 ---------------------------------------

n=1000
x=c()
pour (i dans 1:n)
{
	u=-log(runif(1,0,1))
	x=c(x,u)
}
hist(x,fréq=FALSE)
t=séq(0,8,0.1)
lignes(t,exp(-t),type='l',col='rouge')

# EXERCICE 2.3 ---------------------------------------

#algo de rejet
simu<-fonction(t)
{
	b=0
	tandis que (b==0)
	{
		u=runif(2,-1,1)
		si (u[1]^2+u[2]^2<1)
		{
			b=1
		}
	}
	revenir(u)
}

#dessin de points
n=100
tabx=c();taby=c()
pour (i dans 1:n)
{
	u=simu(1)
	tabx=c(tabx,u[1])
	taby=c(taby,u[2])
}
tracé(tabx,taby,pch=1)

# trace d'un cercle
x=séq(-1,1,0.01)
y=sqrt(1-x^2)
lignes (x, y, 'l')
y=-sqrt(1-x^2)
lignes (x, y, 'l')

# EXERCICE 2.4 ---------------------------------------

bernoulli<-fonction(s)
{
	u=runif(1,0,1)
	si (nous<s)
	{
		r=1
	}
	autre
	{
		r=0
	}
	retour(r)
}

simug<-fonction(t)
{
	b=0
	tandis que (b==0)
	{
		s=bernoulli(0.5)
		u=runif(2,0,1)
		x=-log(u[1])
		y=-log(u[2])
		si (2*y>(1-x)^2)
		{
			b=1
		}
	}
	retour((2*s-1)*x)
}

n=1000
tabulation=c()
pour (i dans 1:n)
{
	tab=c(tab,simug(1))
}
hist(tab,freq=FALSE)
x=séq(-5,5,0.05)
y=exp(-x*x/2)/sqrt(2*pi)
lignes(x,y,'l',col='rouge')

# EXERCICE 2.5 ---------------------------------------
	
n=10 000
p=0,05
x<-rnorme(n,1,1)
y=ordre(x)
z=x[y] #on classe les valeurs par ordre croissant
k = tronc (p*n)
cat("VaR estimée : ",-z[k])
	
	
# EXERCICE 2.8 ---------------------------------------

une=2
C=(1-exp(-a))^(-1)

f<-fonction(t)
{
	r=0
	si (t>=0)
	{
		si (t<=a)
		{
			r=exp(-t)
		}
	}
	retour(r)	
}

simu01<-fonction(t)
{
	b=0
	tandis que (b==0)
	{
		u=runif(1,0,1)	
		x=runif(1,0,a)
		si (u<exp(-x))
		{
			b=1
		}	
	}
	retour(x)
}

n=1000
tabulation=c()
pour (i dans 1:n)
{
	tab=c(tab,simu01(1))
}
hist(tab,freq=FALSE)
x=séq(0,a+1,0.05)
y=c()
pour (i en 1:longueur(x))
{
	y=c(y,f(x[i]))	
}
lignes(x,y,'l',col='rouge')

simu02<-fonction(t)
{
	b=0
	tandis que (b==0)
	{
		u=runif(1,0,1)
		v=runif(1,0,1)
		x=-log(v)
		si (u<f(x)*exp(x))
		{
			b=1
		}
	}
	retour(x)
}


n=1000
tabulation=c()
pour (i dans 1:n)
{
	tab=c(tab,simu02(1))
}
hist(tab,freq=FALSE)
x=séq(0,a+1,0.05)
y=c()
pour (i en 1:longueur(x))
{
	y=c(y,f(x[i]))	
}
lignes(x,y,'l',col='rouge')

# EXERCICE 2.9 ---------------------------------------

f1<-fonction(t)
{
	r=0
	si (t>=1)
	{
		r=exp(-t*t)
	}
	retour(r)	
}

f2<-fonction(t)
{
	retour(exp(-t*t))
}

g2<-fonction(t)
{
	r=0
	si (t>=0)
	{
		r=exp(-t)
	}
	retour(t)	
}

simu29<-fonction(t)
{
	b=0
	tandis que (b==0)
	{
		u=runif(1,0,1)
		v=runif(1,0,1)
		x=-log(v)
		si (u<f1(x)/g2(x))
		{
			b=1
		}	
	}	
	retour(x)
}

n=1000
tabulation=c()
pour (i dans 1:n)
{
	tab=c(tab,simu29(1))
}
hist(tab,freq=FALSE)
x=séq(1,3,0.05)
y=c()
# on peut calculer une valeur approchée de Z avec R
Z=intégrer(f2,inférieur=1,supérieur=10)$valeur
pour (i en 1:longueur(x))
{
	y=c(y,f2(x[i])/Z)	
}
lignes(x,y,'l',col='rouge')