#TD/TP No 6
#1.1.1
	omega1=6/100
	omega2=10/100
	omega3=40/100
	x1 = 2*cos(2*pi*1:100*omega1) 
	 x2 = 2*cos(2*pi*1:100*omega2) 
	  x3 = 2*cos(2*pi*1:100*omega3)
	x=x1+x2+x3
	 par(mfrow=c(2,2))
	 plot.ts(x1, ylim=c(-5,5), main=expression(omega==2*pi*6/100))
	 plot.ts(x2, ylim=c(-5,5), main=expression(omega==2*pi*10/100))
	 plot.ts(x3, ylim=c(-5,5), main=expression(omega==2*pi*40/100))
	 plot.ts(x, ylim=c(-5,6), main="sum")
 
#1.1.2 
par(mfrow=c(2,1))
n=length(x) ; P=abs(fft(x)/n)^2 ; Fr=(0:(n-1))*2*pi/n ; plot(Fr,P,type="o",xlab="frequence",ylab="pÃ©riodogramme")
#Attention, les abscisses vont de 0 Ã  2*pi.
#On voit bien des pics en 2*pi*6/100, 2*pi*10/100, 2*pi*40/100.
 
 #1.1.3
 k=kernel("daniell",4)
 # par(mfrow=c(1,1))
 spec.pgram(x,k,taper=0,log='no')
 #Les abscisses vont de 0 Ã  pi (elles ne s'affichent pas correctement).
 #Ce graphique contient les mÃªmes pics que le pÃ©riodogramme. Comme il est obtenu par lissage Ã  partir du pÃ©riodogramme, certains pics peuvent Ãªtre confondus.
  
 #1.1.5
 n=100
 modele=list(ar=c(0,-0.5,0.2))
 x=arima.sim(modele,n) 
  plot(x)
  xw=window(x,1,20)
  plot(xw)
  
 #1.1.6
spec.pgram(x,k,taper=0,log='no')
#On voit un pic en 1,7 (=0.27*pi/0.5) (environ), ce qui correspond Ã  une pÃ©riode de 2*pi/1.7=4 (environ). Et en effet, x oscille avec une pÃ©riode Ã  peu prÃ¨s Ã©gale Ã  4. 
 
 #1.2.1-2
  x=sunspot.year
 spec.pgram(x,k,taper=0,log='no')
 #On voit un pic en 0,1. Ce qui correspond Ã  une frÃ©quence : (0.1/0.5)*pi, et donc Ã  une pÃ©riode : (2*pi)/((0.1/0.5)*pi)=10. Ce qu'on voit sur le graphe de x. 
 
 #Brouillon
 #n=length(x) ; P=abs(fft(x)/n)^2 ; Fr=(0:(n-1))*2*pi/n ; plot(Fr,P,type="o",xlab="frequence",ylab="pÃ©riodogramme")
 
 #1.2.3-4
 data=scan(file="http://math.unice.fr/~rubentha/enseignement/soi.clean.dat",skip=1)
 x=ts(data,frequency=12)
 soi.per=spec.pgram(x,k,taper=0,log='no')
 #On observe un pic en 0.2*pi/6 (les abscisses vont toujours de 0 Ã  pi). Ceci correspond Ã  une pÃ©riode  (2*pi)/(0.2*pi/6)=60 mois (data contient des donnÃ©es mensuelles) donc 5 ans. L'indice SOI est un indicateur du phÃ©nomÃ¨ne El-Nino (que l'on pense Ãªtre de pÃ©riode 4 annnÃ©es).
 
