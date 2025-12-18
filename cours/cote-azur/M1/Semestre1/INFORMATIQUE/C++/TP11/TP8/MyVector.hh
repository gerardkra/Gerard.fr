#ifndef __MY_VECTOR_HH__
#define __MY_VECTOR_HH__

class MyVector{
private:
  unsigned int _n;
  double* _vals;
public:
  // Constructeurs
  MyVector(unsigned int n);   // 1er constructeur
  MyVector(unsigned int n, double* t);  // 2eme constructeur

  // Destructeur
  ~MyVector(); 

  /*
    Fonction affiche
    le const en fin de prototype sert à indiquer que la fonction ne modifie 
    l'instance courante. Ainsi cette fonction
    pourra être appelé sur des objets déclarés const. Impossible sinon.
    C'est logique pour un affichage qui ne modifie pas l'objet par déf.
  */
  void affiche() const; 

  //  fonction membre pour le produit scalaire
  double prod_scal(const MyVector& v) const;

  // fonction myMediane
  double myMediane() const;

  // fonction myMediane V2
  double myMedianeV2() const;  

  // fonction resize
  void resize(unsigned int newSize);

  /*   
       Fonction reduce
  */
  double reduce(double (*f)(double, double)) const;
};

#endif
