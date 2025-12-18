// Exercice: Moyenne (II)
//
// Pour compiler (à faire dans le terminal de Visual Studio Code ou celui de Linux ou Mac):
// g++ moyenne2.cpp -o moyenne2
//
// Pour exécuter  (à faire dans le terminal de Visual Studio Code ou celui de Linux ou Mac):
// ./moyenne2
//
// On entre ensuite la valeur de n puis les n valeurs, séparées par <Entrée>
//

#include<iostream>
using namespace std;

int main()
{
  int n; // n doit être un int (ou un unsigned int)
  cout << "Nombre n de valeurs  à entrer?" << endl;
  cin >> n;
  cout << "Entrer " << n << " valeurs au clavier:" << endl;
  float val; // on choisit le type double pour être générique (on veut faire la moyenne de nombres réels, pas seulement d'entiers).
             // le type 'double' convient aussi
  float m  = 0.;
  for(int i=0;i<n;i++) 
    {
      cin >> val;
      m += val;
    }
  cout << "La moyenne est " << m/n << endl;
  return 0;
}
