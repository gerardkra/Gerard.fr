# EXERCICE 3.1

pari=5
n=10 000

g<-fonction(x)
{
	si (x>0)
	{
		retour(exp(pari*x))
	}
	autre
	{
		retour(0)
	}	
}

ft<-fonction(x)
{
	return(exp(-(x-bet)^2/2)/sqrt(2*pi))
}

f<-fonction(x)
{
	retour(exp(-x^2/2)/sqrt(2*pi))
}

h<-fonction(x)
{
	retour(exp(pari*x))
}

gg<-fonction(x)
{
	retour(g(x)*f(x)/ft(x))
}

#Question 1
s=0
pour (i dans 1:n)
{
	x=rnorme(2,0,1)	
	s=s+(g(x[1])-g(x[2]))^2
}
v1=s/(2*n)
imprimer (v1)
#on constate que la variance est très grande

#Question 2
#Échantillonage d'importance
s=0
pour (i dans 1:n)
{
	x=rnorme(2,pari,1)
	s=s+(gg(x[1])-gg(x[2]))^2
}
imprimer(s/(2*n))
#on constate que la variance est bien réduite par par rapport à la question 1

#Question 3
#Variable de contrôle
s=0
pour (i dans 1:n)
{
	x=rnorme(2,0,1)
	s=s+(g(x[1])-h(x[1])-g(x[2])+h(x[2]))^2
}
imprimer(s/(2*n))
#on constate que la variance est bien réduite par par rapport à la question 1

#Question 4
#Variables antithétiques
n=10 000
s=0
pour (i dans 1:n)
{
	x=rnorme(2,0,1)
	s=s+((g(x[1])+g(-x[1]))/2-(g(x[2])+g(-x[2]))/2)^2
}
v4=s/(2*n)
imprimer (v4)
imprimer (v4/v1)
#la réduction de variance n'est pas flagrante, il faut prendre n plus grand pour avoir une meilleure précision

-------------------------------------------------- -----------

# EXERCICE 3.2

# Question 2

n=1000
s=0
pour (i dans 1:n)
{
	x=rnorme(2,0,1)
	s=s+(carré(abs(x[1]))-carré(abs(x[2])))^2
}
imprimer(s/(2*n))

#Question 4
s=0
pour (i dans 1:n)
{
	x=rnorme(2,0,1)
	s=s+(abs(x[1])-sqrt(abs(x[1]))-abs(x[2])+sqrt(abs(x[2])))^2
}
imprimer(s/(2*n))


-------------------------------------------------- -----------

# EXERCICE 3.3

# Question 1

indicateur<-fonction(x)
{
	r=0
	si (x>l)
	{
		si (x<l+1)
		{
			r=1
		}
	}
	retour(r)
}
			

n=10 000
s=0
l=3
pour (i dans 1:n)
{
	u=runif(1,0,1)
	x=-log(u)
	s=s+indicateur(x)
}
imprimer(s/n)

s=0
pour (i dans 1:n)
{
	u=runif(2,0,1)
	x1=-log(u[1])
	x2=-log(u[2])
	s=s+(indicateur(x1)-indicateur(x2))^2
}
imprimer(s/(2*n))

# Question 2

s=0
pour (i dans 1:n)
{
	u=runif(1,l,l+1)
	s=s+exp(-u)
}
imprimer(s/n)

s=0
pour (i dans 1:n)
{
	u=runif(2,l,l+1)
	s=s+(exp(-u[1])-exp(-u[2]))^2
}
imprimer(s/(2*n))
# on remarque que la variance est réduite

# EXERCICE 3.3 (avec gaussienne)

l=5
n=100 000

ftilde<-fonction(x)
{
	z=0
	si (x>l)
	{
		si (x<l+1)
		{
			z=exp(-x)/(exp(-l)-exp(-l-1))
		}
	}
	retour(z)
}

f<-fonction(x)
{
	retour(exp(-x*x/2)/sqrt(2*pi))
}

g<-fonction(x)
{
	z=0
	si (x>l)
	{
		si (x<l+1)
		{
			z=1
		}
	}
	retour(z)
}

Fexpo<-fonction(u)
{
	return(-log(exp(-l)*(1-u)+u*exp(-l-1)))
}

print("valeur approchée par méthode déterministe : ")
intégrer(f,l,l+1)
I=intégrer(f,l,l+1)$valeur

# méthode 1
s=0
pour (i dans 1:n)
{
	u=runif(1,l,l+1)
	s=s+f(u)
}
cat("moyenne 1 : ",s/n)

s=0
pour (i dans 1:n)
{
	u=runif(1,l,l+1)
	v=runif(1,l,l+1)
	s=s+(f(u)-f(v))^2
}
cat("variance relative 1 : ",s/(2*n*I^2))

	

# méthode 2
s=0
pour (i dans 1:n)
{
	u=runif(1,0,1)
	x=Fexpo(u)
	s=s+f(x)/ftilde(x)
}
cat("moyenne 2 :",s/n)

s=0
pour (i dans 1:n)
{
	u=runif(1,0,1)
	x=Fexpo(u)
	v=runif(1,0,1)
	y=Fexpo(v)
	s=s+(f(x)/ftilde(x)-f(y)/ftilde(y))^2
}
cat("variance relative 2 : ",s/(2*n*I^2))
	
