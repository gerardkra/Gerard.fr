#ifndef __NEURONE_HH__
#define __NEURONE_HH__
#include<iostream>

using namespace std;

class Neurone
{
private:
  double* _poids;   //   tableau des poids
  unsigned int _n;  //  taille du tableau des poids

public:
  /*
    Ce constructeur construit un neurone
    dont les poids initiaux sont aléatoires
  */
  Neurone(unsigned int);

  //  constructeur par copie
  Neurone(const Neurone&);

  // destructeur  
  ~Neurone();

        //  l'opérateur + permet d'additioner le vecteur de poids avec un tableau de double
  Neurone operator+(double* t) const;
  
  // opérateur =  Ne pas oublier la référence à gauche!
        Neurone & operator=(const Neurone& other);

  //  opérateur() qui applique le neurone aux entrées
  double operator()(double *entries) const;

  //  opérateur d'affichage du neurone
  friend ostream& operator<<(ostream & c, const Neurone & N);
};
#endif
