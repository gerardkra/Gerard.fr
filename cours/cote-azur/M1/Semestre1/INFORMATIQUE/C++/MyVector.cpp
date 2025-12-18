#include<iostream>
#include "MyVector.hh"

using namespace std;

MyVector::MyVector(unsigned int n) : _n(n)
{
  _vals = new double[_n];
  for(int i=0;i<_n;i++)
    _vals[i] = 0.;
}


MyVector::MyVector(unsigned int n, double* t) : _n(n)
{
  _vals = new double[_n];
  for(int i=0;i<_n;i++)  // important - on évite les copies de pointeurs mais on copie le contenu
    _vals[i] = t[i];
}

MyVector::~MyVector()
{
    //  Le destructeur doit libérer la mémoire
    // lors de la destruction de l'objet.
  delete [] _vals;
}

double MyVector::prod_scal(const MyVector& v) const
{
  double resu = 0;
  for(int i=0;i<_n;i++)
    resu += v._vals[i]*_vals[i];
  return resu;
}

void MyVector::affiche() const
{
  cout << "Objet MyVector de taille " << _n << endl;
  for(int i=0;i<_n-1;i++)
    cout << _vals[i] << " ";
  cout << _vals[_n-1] << endl;
}

void MyVector::resize(unsigned int newSize)
{
    // on a rien à faire  si même taille
  if(newSize == _n)
    return;

  // on recopie les anciennes valeurs de _vals dans un tableau temporaire buf (pour buffer)
  double* buf;
  buf = new double[_n];
  for(int i=0;i<_n;i++)
    buf[i] = _vals[i];

  if(newSize != _n){
    //  on détruit l'ancien tableau devenu inutile
    delete [] _vals;
    // allocation
    _vals = new double[newSize];
  }
  
  if(newSize> _n)
    {
      for(int i=0;i<_n;i++)
	_vals[i] = buf[i];
      for(int i=_n;i<newSize;i++)
	_vals[i] = 0;
    }
  else if (newSize < _n)
    {
      for(int i=0;i<newSize;i++)
	_vals[i] = buf[i];
    }
  _n = newSize;
  
  delete [] buf;
}

//    La fonction reduce est amie de la classe MyVector

// Le 1er argument de la fonction f sera la somme qu'on calcule à laquelle on ajoute un élément du tableau _vals
double MyVector::reduce(double (*f)(double, double)) const
{
  double s = 0;
  for(int i=0;i<_n;i++)
    s = f(s, _vals[i]);
  return s;
}

double MyVector::myMediane() const
{
  double resu;
  bool verifCroissant = true;
  if(!_n) {
    cout << "Erreur vecteur de taille nul, impossible de calculer la moyenne" << endl;
    resu = -1;
  }
  else
    {
      for(int i=0;i<_n-1;i++)
	if(_vals[i+1]< _vals[i])
	  {
	    verifCroissant = false;
	    break;
	  }
      if(!verifCroissant)
	resu = -1;
      else
	{
	  if(_n%2)
	    resu = _vals[_n/2];
	  else
	    if(_n>=2)
	      resu =  (_vals[_n/2]+_vals[_n/2-1])/2.;
	}
    }
  return resu;
}

void MySwap(double & T1, double& T2)
{
  double T3;
  T3 = T1;
  T1 = T2;
  T2 = T3;
}


void MySort(double* tab, int n)
{
  for(int i=n-1;i>=1;i--)
    {
      for(int j=0;j<=i-1;j++){
	if (tab[j+1] < tab[j])
	  MySwap(tab[j+1], tab[j]);
      }
    }
}

double MyVector::myMedianeV2() const
{
  double resu;
  double* tab = new double[_n]; // on ne modifie pas _vals
  for(int i=0;i<_n;i++)
    tab[i] = _vals[i];
  MySort(tab, _n);
  if(_n%2)
    resu = tab[_n/2];
  else
    if(_n>=2)
      resu =  (tab[_n/2]+tab[_n/2-1])/2.;
  delete [] tab;
  return resu;
}
