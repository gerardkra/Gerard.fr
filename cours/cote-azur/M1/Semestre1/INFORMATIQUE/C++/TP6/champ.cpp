// Exercice: Superficie d'un champ
//
// Pour compiler (à faire dans le terminal de Visual Studio Code ou celui de Linux ou Mac):
// g++ champ.cpp -o champ
//
// Pour exécuter (à faire dans le terminal de Visual Studio Code ou celui de Linux ou Mac):
// ./champ
//
// On entre ensuite les deux valeurs, séparées par <Entrée>
//

#include<iostream>
using namespace std;

int main()
{
  float largeur, longueur; // le type 'double' convient aussi
  cout << "Largeur du champ?" << endl;
  cin >> largeur; // pas besoin de endl avec cin
  cout << "Longueur du champ?" << endl;
  cin >> longueur;  // pas besoin de endl avec cin
  cout << "La superficie du champ est " << largeur*longueur << endl;
  return 0;
}
