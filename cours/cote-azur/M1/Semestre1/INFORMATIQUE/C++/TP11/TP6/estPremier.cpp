// # Pour compiler (à faire dans le terminal de Visual Studio Code ou celui de Linux ou Mac)
// g++ estPremier.cpp -o estPremier
// # Pour exécuter (à faire dans le terminal de Visual Studio Code ou celui de Linux ou Mac)
// ./estPremier

#include<iostream>
#include<cmath>
using namespace std;

// boolalpha permet simplement l'affichage d'un booléen (true ou false) en chaîne de caractères  (sans boolalpha, c'est 1 ou 0)

bool estPremier(unsigned int m)
{
  bool resu = true;
  for(int i=2;i<sqrt(m);i++)
    {
      if(m%i==0)  {
	resu = false;
      	break;
      }
    }
  return resu;
}

int main()
{
  cout << boolalpha << "estPremier(71) (should be true) " << estPremier(71) << endl;
  cout << boolalpha << "estPremier(2427) (should be false) " << estPremier(2427) << endl;
  cout << boolalpha << "estPremier(87109) (should be false) " << estPremier(87109) << endl;
  return 0;
}
