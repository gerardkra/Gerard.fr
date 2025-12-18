// Exercice: Racines d'un polynôme
//
// # Pour compiler (à faire dans le terminal de Visual Studio Code ou celui de Linux ou Mac)
// g++ poly.cpp -o poly
//
// # Pour exécuter (à faire dans le terminal de Visual Studio Code ou celui de Linux ou Mac)
// ./poly
//
//  Dans ce qui suit, sqrt vient de 'cmath' et la fonction fabs (aussi de 'cmath') est la fonction valeur absolue pour un nombre réel. On teste ici si a==0 (ou numériquement parlant si |a|<=eps)
// 
#include<iostream>
#include<cmath>

using namespace std;

int main()
{
  double a, b, c;  // (coefficients du polynome) - on aurait pu choisir float au lieu de double
  double s1, s2;  // (racines du polynomes) - on aurait pu choisir float au lieu de double
  double eps = 1e-9; // pour la précision numérique (pour tester si a==0)
  cout << "Entrer les coefficients a, b et c du polynome" << endl;
  cin >> a;
  cin >> b;
  cin >> c;
  cout << "Le polynome est " << a << "*x^2 + " << b << "*x + " << c << "." << endl;
  double discr = b*b - 4*a*c; // discrimant
  if(discr<0)
    cout << "Le polynome n'a pas de racine reelle." << endl;

  if(discr>=0)
    {
      if(fabs(a)> eps)   // on teste si a est différent de 0 - Pour cela, on teste si |a|>eps, pour éviter des erreurs de précision numérique.
	{
	  s1 = (-b + sqrt(discr))/(2*a);
	  s2 = (-b - sqrt(discr))/(2*a);
	  cout << "Le polynome a des racines reelles." << endl;
	  cout << "Les deux racines sont " << s1 << " et " << s2 << endl;
	  cout << "Verification pour s1: " << a*s1*s1 + b*s1+ c << endl;
	  cout << "Verification pour s2: " << a*s2*s2 + b*s2+ c << endl;
	}
      else if(fabs(b)> eps)   // ici a=0 et on teste si b est different de 0
	{
	  s1 = -c/b;
	  cout << "La solution (unique) est " << s1 << endl;
	  cout << "Verification pour s1: " << a*s1*s1 + b*s1+ c << endl;
	}
      else
	cout << "Polynôme constant" << endl;
    }
  return 0;
}
