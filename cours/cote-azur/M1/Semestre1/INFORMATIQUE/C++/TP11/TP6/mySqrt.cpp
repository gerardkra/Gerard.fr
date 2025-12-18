// Exercice: Racine carrée

// # Pour compiler (à faire dans le terminal de Visual Studio Code ou celui de Linux ou Mac)
// g++ mySqrt.cpp -o mySqrt
//
// # Pour exécuter (à faire dans le terminal de Visual Studio Code ou celui de Linux ou Mac)
// ./mySqrt

#include <iostream>
#include <cmath>
#include <iomanip>   // pour gérer le nb de chiffres après la virgule en utilisant setprecision

using namespace std;

double mySqrt(double r)
{
  double x = r;
  int nit = 5; //10; //20;
  for(int i=0;i<nit;i++)
    x = (x + r/x)/2.;
  return x;
}

int main(void)
{
  double r;
  // setprecision(8) permet d'avoir 8 chiffres significatifs à l'affichage, sqrt vient de 'cmath'
  //
  r = 9;
  cout << setprecision(8) << "Approximation of the square root of " << r << " is " << mySqrt(r) << ". True value is " << sqrt(r) << endl; 
  r = 156.;
  cout << setprecision(8) << "Approximation of the square root of " << r << " is " << mySqrt(r) << ". True value is " << sqrt(r) << endl; 
  r = 17;
  cout << setprecision(8) << "Approximation of the square root of " << r << " is " << mySqrt(r) << ". True value is " << sqrt(r) << endl; 
  r = 64;
  cout << setprecision(8) << "Approximation of the square root of " << r << " is " << mySqrt(r) << ". True value is " << sqrt(r) << endl; 
  r = 17.3;
  cout << setprecision(8) << "Approximation of the square root of " << r << " is " << mySqrt(r) << ". True value is " << sqrt(r) << endl;
  return 0;
}

