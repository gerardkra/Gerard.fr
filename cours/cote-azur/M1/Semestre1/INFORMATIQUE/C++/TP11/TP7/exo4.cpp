// # Pour compiler (à faire dans le terminal de Visual Studio Code ou celui de Linux ou Mac)
// g++ exo4.cpp -o exo4
//
// # Pour exécuter (à faire dans le terminal de Visual Studio Code ou celui de Linux ou Mac)
// ./exo4
//
#include<iostream>
#include<cstring>  // necessaire pour strlen, strcat, strcpy
using namespace std;

int main()
{
  cout << "Entrer une chaine de caracteres" << endl;
  string s;

  cin >> s;
  cout << "Affichage de la chaine, de sa taille et de la chaine doublee" << endl;
  cout << s << endl;
  cout << s.size() << endl;
  cout << s + s << endl;
  cout << "Entrer une chaine de caracteres" << endl;
  char ch[20];

  cin >> ch;  // ca marche!
  cout << "Affichage de la chaine, de sa taille et de la chaine doublee" << endl;
  int i=0;
  while(ch[i++]) cout << ch[i-1];
  cout << endl;
  cout << --i << endl;  // taille de la chaine - on enleve 1
  cout << strlen(ch) << endl; //  autre methode pour avoir la taille
  char ch2[20];
  strcpy(ch2, strcat(ch, ch));
  cout << ch2 << endl;
}
