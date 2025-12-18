#include<iostream>
#include "Animal.hh"
using namespace std;

// fonction membre pour acceder au nom de l'Animal
string Animal::get_nom() const
{
  return _nom;
}

// fonction membre pour acceder au poids de l'Animal
double Animal::get_poids() const
{
  return _poids;
}

// fonction membre affiche de la classe Animal
void Animal::affiche() const
{
  cout << "Animal " << _nom << ", de "
       <<_poids << " kgs" << endl;
}

// constructeur a deux arguments
Animal::Animal(string c, double p) : _nom(c),
				     _poids(p) {}

// constructeur sans argument
Animal::Animal() : _nom(""), _poids(0) {}

// fonction poidsTotal
double poidsTotal(Animal* t, int n)
{
  double p=0;
  for(int i=0;i<n;i++)
    p += t[i].get_poids();
  return p;
}





// fonction affiche (pour plusieurs Animaux)
void affiche(Animal* t, int n)
{
  for(int i=0;i<n;i++)
    t[i].affiche();
}

// fonction getMaxPoids - indice de l'Animal le plus lourd
int getMaxPoids(Animal* t, int n)
{
  double p = t[0].get_poids();
  int j = 0;
  for(int i=1;i<n;i++)
    {
      if(t[i].get_poids()> p) {
	j = i; p = t[i].get_poids(); }
    }
  return j;
}

// main
int main()
{
  Animal troupeau[3] = {Animal("vache", 1000),
    Animal("mouton", 400), Animal("chevre", 60)};
  affiche(troupeau, 3);
  cout << "Poids Total: " <<
    poidsTotal(troupeau, 3) << endl;
  int j = getMaxPoids(troupeau, 3);
  cout << "L'animal de poids le plus eleve est "
       << troupeau[j].get_nom() << endl;
  return 0;
}
