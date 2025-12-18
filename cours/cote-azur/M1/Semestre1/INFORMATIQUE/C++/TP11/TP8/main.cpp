#include "MyVector.hh"
#include<iostream>

// Pour compiler:
// g++ main.cpp MyVector.cpp -o MyVector
//
// Si message d'erreur "error: expected ';' at end of declaration" sur new, faire
// g++ -std=c++11 main.cpp MyVector.cpp -o MyVector 

// Pour exécuter:
// ./MyVector

using namespace std;

//  fonction somme qui sera utilisée
// lors de l'appel de la fonction reduce
double somme(double a, double b){
  return a+b;
}

int main(void){

  MyVector v0(4);
  cout << "v0: " << endl;
  v0.affiche();

  double*  t1 = new double[5] {-7.1, -5.4, 1.1, 1.5, 1.7};
  MyVector v1(5, t1);  
  delete [] t1; // on peut liberer l'espace memoire alloue pour t1 car son contenu a ete copie dans v1._vals
  cout << endl << "v1: " << endl;
  v1.affiche();

  double*  t2 = new double[6] {-2.3, 0, 1, 2.3, 7.3, 11.1};
  MyVector v2(6, t2);  
  delete [] t2;
  cout << endl <<"v2: " << endl;
  v2.affiche();

  double  t3[5] = {6, -2, 2.5, 5.1, -5.4};  // tableau de taille fixee
  MyVector v3(5, t3);  

  cout << endl << "produit scalaire v1.v3 (on doit trouver -30.58) " << endl;
  cout << v1.prod_scal(v3) << endl;

  cout << endl << "myMediane de v1 (on doit trouver 1.1) " << endl;
  cout << v1.myMediane() << endl;

  cout << endl << "myMediane de v2 (on doit trouver 1.65) " << endl;
  cout << v2.myMediane() << endl;

  cout << endl << "myMedianeV2 de v2 (on doit trouver 1.65) " << endl;
  cout << v2.myMedianeV2() << endl;
  
  cout << endl << "myMediane de v3 (on doit trouver -1 - v3 n'est pas dans l'ordre croissant) " << endl;
  cout << v3.myMediane() << endl;  

  v1.resize(7);
  cout << endl << "Affichage de v1 après v1.resize(7) " << endl;
  v1.affiche();

  cout << endl << "Reduce v2: 19.4 " << endl;
  cout << v2.reduce(somme) << endl;

  v2.resize(3);
  cout << endl << "Affichage de v2 après v2.resize(3) " << endl;
  v2.affiche();

  cout << endl << "myMedianeV2 de v3 (on doit trouver 2.5) " << endl;
  cout << v3.myMedianeV2() << endl;

  double t4[6] = {6, -2, 2.5, 5.1, -5.4, 12.1};
  MyVector v4(6, t4);
  cout << endl << "Affichage de v4 " << endl;
  v4.affiche();
  cout << endl << "myMedianeV2 de v4 (on doit trouver 3.8) " << endl;
  cout << v4.myMedianeV2() << endl;  
}
