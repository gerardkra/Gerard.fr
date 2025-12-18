// Exercice: Fonction puissance
//
// Pour compiler:
// g++ myPow.cpp -o myPow
//
// Pour exécuter (les exemples sont dans le main)
// ./mypow
//

#include<iostream>
#include<cmath>

using namespace std;

double myPow(double x, int m)
{
  double resu = 1;
  double eps = 1e-9; // pour la précision numérique
  int j = 0;
  if(m>=0)
    {
      while(j<=m-1)
	{
	  resu *= x;
	  j++;
	}
    }
  else
    {
      if(fabs(x)<eps) {  // valeur 0 pour x non autorisée si m<0
	cout << "Valeur de  l'argument non autorisée. Arrêt" << endl;
	exit(1); // arrêt brutal du programme avec code retour 1
      }
      while(j<=-m-1)
	{
	  resu /= x;
	  j++;
	}
    }
  return resu;
}

int main()
{
  cout << "2^4 " << myPow(2, 4) << " " << pow(2,4) << endl;
  cout << "2^10 " << myPow(2, 10) << " " << pow(2,10) << endl;
  cout << "1.5^2 " << myPow(1.5, 2) << " " << pow(1.5,2) << endl;
  cout << "2^(-3) " << myPow(2, -3) << " " << pow(2,-3) << endl;
  cout << "3^(-4) " << myPow(3, -4) << " " << pow(3,-4) << endl;
  cout << "3^0 " << myPow(3, 0) << " " << pow(3,0) << endl;
  cout << "(-2)^0 " << myPow(-2, 0) << " " << pow(-2,0) << endl;
  cout << "(0)^2 " << myPow(0, 2) << " " << pow(0,2) << endl;
  cout << "(0)^(-2) " << myPow(0, -2) << " " << pow(0,-2) << endl;
  return 0;
}
