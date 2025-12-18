#include <iostream>
using namespace std;

int main()
{
  int a;               // On déclare un entier a; on réserve donc 4 octets en mémoire que l'on nomme 'a'
  unsigned int b;      // On déclare un entier non signé b, 4 octets sont aussi alloués
  char c;              // On déclare un caractère 'c', un octet est réservé
  double reel1, reel2; // deux réels sont déclarés et la place correspondante en mémoire est allouée

  a = 0;       // On attribue à 'a' la valeur 0 -> jusqu'à maintenant, elle n'avait pas de valeur
  b = -1;      // On essaye de donner une valeur négative à b !
  c = 'a';     // 'a' est la notation pour le caractère a.
  reel1 = 1e4; //  reel1 prend la valeur 10000
  reel2 = 0.0001;
  cout << "a : " << a << " " << endl
	    << "Interessant : "
	    << "b : " << b << endl    // HA ! - ça n'est pas -1!
	    << "c ; " << c << " " << endl;
  cout << reel1 << endl;
  cout << reel2 << endl;
}
