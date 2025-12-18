// # Pour compiler (à faire dans le terminal de Visual Studio Code ou celui de Linux ou Mac)
// g++ myMin.cpp -o myMin
//
// # Pour exécuter (à faire dans le terminal de Visual Studio Code ou celui de Linux ou Mac)
// ./myMin
//
#include<iostream>
#include<cmath>
using namespace std;

// version 1 - 3 ints
int myMin(int a, int b, int c)
{
  cout << "Valeur minimum entre " << a << ", " << b << " et " << c << endl;
  cout << "myMin pour 3 ints" << endl;
  int theMin = (a<b) ? a:b;
  theMin = (theMin<c) ? theMin:c;
  return theMin;
}

// version 2 - 3 doubles
double myMin(double a, double b, double c)
{
  cout << "Valeur minimum entre " << a << ", " << b << " et " << c << endl;
  cout << "myMin pour 3 doubles" << endl;
  double theMin = (a<b) ? a:b;
  theMin = (theMin<c) ? theMin:c;
  return theMin;
}

// version 3 - 1 tableau de 3 int
int myMin(int* t)  //int myMin(int t[3]) convient aussi
{
  cout << "Valeur minimum entre " << t[0] << ", " << t[1] << ", " << t[2] << endl;
  cout << "myMin pour un tableau de 3 ints" << endl;
  int theMin = (t[0]<t[1]) ? t[0]:t[1];
  theMin = (theMin<t[2]) ? theMin:t[2];
  return theMin;
}

// correctif nécessaire pour gérer le tableau de 3 doubles
double myMin(double t[3])
{
  cout << "Valeur minimum entre " << t[0] << ", " << t[1] << ", " << t[2] << endl;
  cout << "myMin pour un tableau de 3 doubles" << endl;
  double theMin = (t[0]<t[1]) ? t[0]:t[1];
  theMin = (theMin<t[2]) ? theMin:t[2];
  return theMin;
}

// on aurait pu se passer de la version 1 de myMin pour les 3 entiers ia, ib et ic. La version 2 (3 doubles) aurait été utilisée par le compilateur (après conversion de types)
int main()
{
  int ia = 21, ib = 14, ic = 16;
  cout << myMin(ia, ib, ic) << endl;
  double a = 2.1, b = 2.4, c = 1.6;
  cout << myMin(a, b, c) << endl;

  int t[3] = {4, 12, 11};
  double v[3] = {4.9, 12, 11};
  cout << myMin(t) << endl;
  cout << myMin(v) << endl; // erreur à la compilation si pas de fonction (celle de la ligne 43)
  return 0;
}
