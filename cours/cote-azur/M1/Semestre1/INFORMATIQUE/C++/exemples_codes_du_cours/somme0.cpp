#include <iostream>
using namespace std;

//  Déclaration de la fonction somme
double somme(double a, double b);

// Point d'entrée de notre programme
int main()
{
  double a, b;
  cout << "Donnez deux reels" << endl;
  cin >> a >> b;
  cout << a << " + " << b << " = " << somme(a, b) << endl;
  return 0;
}

// définition de la fonction somme
double somme(double a, double b)
{
  return a+b;
}
