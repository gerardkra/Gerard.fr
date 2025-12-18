# EXERCICE 1.5 ---------------------------------------

n=1000
s=0
pour (i dans 1:n)
{
	x=runif(1,0,1)
	t=runif(1,0,pi/2)
	si (x<sin(t))
	{
		s=s+1
	}	
}
cat("estimation de pi : ",2*n/s)
