// # Pour compiler (à faire dans le terminal de Visual Studio Code ou celui de Linux ou Mac)
// g++ moment.cpp -o moment
//
// # Pour exécuter (à faire dans le terminal de Visual Studio Code ou celui de Linux ou Mac)
// ./moment
//
#include<iostream>
#include<cmath>
using namespace std;

double moyenne(double* x, int n) {
  double moy = 0.; // pas besoin d'utiliser new ici, car on suppose que le tableau est déjà alloué
  for(int i=0;i<n;i++)
    moy += x[i];
  return moy/n;
}

double moment(int k, double* x, int n) {
  double m = 0; // pas besoin d'utiliser new ici, car on suppose que le tableau est déjà alloué
  double M = moyenne(x, n);
  for(int i=0;i<n;i++)
    m += pow(x[i]-M, k);
  return m/n;
}

int main()
{
  double* x;
  x = new double[3] {6, -2.1, -0.5};
  cout << "moment d'ordre 2 de t (on doit trouver 12.2689) " << moment(2, x, 3) << endl;
  delete [] x; // desallocation de x (car il est utilisé ensuite avec une taille différente)

  x = new double[5] {1.1, 2.1, -3.1, 6.1, -1.1};
  cout << "moment d'ordre 4 de t (on doit trouver 195.132) " << moment(4, x, 5) << endl;
  delete [] x; // desallocation de x - dans tout le code, correspondance 1 new <-> 1 delete
}
