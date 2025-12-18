// Exercice: Moyenne (I)
//
// Pour compiler (à faire dans le terminal de Visual Studio Code ou celui de Linux ou Mac):
// g++ moyenne1.cpp -o moyenne1
//
// Pour exécuter (à faire dans le terminal de Visual Studio Code ou celui de Linux ou Mac):
// ./moyenne1
//
// On entre ensuite les cinq valeurs, séparées par <Entrée>
//

#include<iostream>
using namespace std;

// methode 1
int main()
{
  cout << "Entrer cinq valeurs au clavier:" << endl;
  float v1, v2, v3, v4, v5; // on choisit le type float pour être générique (on veut faire la moyenne de nombres réels, pas seulement d'entiers). Le type 'double' convient aussi.
  // On pourrait utiliser un tableau mais on ne l'a pas encore vu en cours.
  cin >> v1; // pas besoin de endl avec cin
  cin >> v2;
  cin >> v3;
  cin >> v4;
  cin >> v5;
  float m = (v1 + v2 + v3 + v4 + v5)/5;
  cout << "La moyenne est " << m << endl;
  return 0;
}

//// methode 2
//int main()
//{
//  cout << "Entrer cinq valeurs au clavier:" << endl;
//  float val; // le type 'double' convient aussi
//  float m  = 0.;
//  for(int i=0;i<5;i++) 
//    {
//      cin >> val;
//      m += val;
//    }
//  cout << "La moyenne est " << m/5 << endl;
//  return 0;
//}
