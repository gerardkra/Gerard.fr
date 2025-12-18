// Exercice: Calcul de la factorielle
//
// # Pour compiler (à faire dans le terminal de Visual Studio Code ou celui de Linux ou Mac)
// g++ myFact.cpp -o myFact
//
// # Pour exécuter (à faire dans le terminal de Visual Studio Code ou celui de Linux ou Mac)
// ./myFact
//
#include<iostream>
using namespace std;

// on utilise le type de sortie 'long int' (entier long) car les valeurs entières deviennent rapidement très grandes ici et le type 'int' de base ne suffirait plus.
// Pour le type d'entrée le type 'int' suffit ('unsigned int', 'short int' aussi)
//
// L'instruction 'exit' permet de sortir du programme
//
long int myFactIt(int n)
{
  if(n<0) {
    cout << "Valeur de  l'argument non autorisée. Arrêt" << endl;
    exit(1); // arrêt brutal du programme avec code retour 1
  }
  long int resu = 1;
  while(n>0)
    {
      resu *= n; // n ne sera pas modifie en sortie du programme
      n--;
    }
  return resu;
}

// version récursive
long int myFactRec(int n)
{
  if(n<0) {
    cout << "Valeur de  l'argument non autorisée. Arrêt" << endl;
    exit(1); // arrêt brutal du programme avec code retour 1
  }
  long int resu;
  if(n==0)
    resu = 1;
  else
    resu = n*myFactRec(n-1);
  return resu;
}

int main()
{
  // test sur 10 valeurs
  for(int n=0;n<10;n++)
    cout << n << "! " << myFactIt(n) << " " << myFactRec(n) << endl;
  return 0;
}
