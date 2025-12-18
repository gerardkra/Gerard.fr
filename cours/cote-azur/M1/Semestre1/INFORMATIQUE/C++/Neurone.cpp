#include<cstdlib>
#include<iostream>
#include "Neurone.hh"

// Pour compiler seulement ce fichier:
// g++ -c Neurone.cpp   # ça ne crée aucun exécutable, mais le compilateur vérifie la syntaxe et crée le fichier objet Neurone.o
//
// Pour compiler tous les fichiers de l'exo:
//
// g++ main.cpp Data.cpp Neurone.cpp -o Neurone.exe # l'exécutable s'appelle Neurone.exe
//

using namespace std;

Neurone::Neurone(unsigned int nb) : _n(nb) {  //  initialisation de _n à la valeur de nb passé en paramètre - écriture raccourcie

  _poids = new double[_n];    //     allocation de l'espace mémoire pour _poids

  //  initialisation des poids avec des valeurs aléatoires entre 0 et 1
  for(int i=0; i<_n;i++)
        _poids[i] = rand() / (1.0 * RAND_MAX);
}

/*
    constructeur par copie de Neurone
*/
Neurone::Neurone(const Neurone& other)
{
  _n = other._n;
  _poids = new double[_n];

  for(int i=0; i<_n;i++)
    _poids[i] = other._poids[i];
}

/*
    Destructeur
    on n'a que _poids à libérer
*/
Neurone::~Neurone()
{
  if(_poids)
    delete [] _poids;
}


/*
    L'opérateur + permet ici de donner un sens à :
    N + tab où tab est un tableau de doubles.
    On choisit le fait que le type de retour de l'addition d'un neurone avec un tableau soit un neurone.

    On suppose que tab a la bonne taille.
*/
Neurone Neurone::operator+(double* tab) const {
  Neurone N(*this); // N est une instance de Neurone qui sera retournée. On aurait pu aussi utiliser l'autre constructeur via 'Neurone N(_n);'

  //  on additione ensuite les poids de l'instance courante avec les valeurs de t
  for(int i=0; i<N._n;i++)
    N._poids[i] += tab[i]; // avec l'autre constructeur 'N._poids[i] = _poids[i] + tab[i];'

  //  on retourne le nouveau neurone 
  return N;
}

/*
    L'opérateur () permet de transformer un objet de type Neurone en fonction.
    Si on a un Neurone N, on pourra écrire N(tab) où tab est un tableau de doubles.
    Le résultat sera lui-même de type double et sera le résultat de la formule explicitée dans le sujet de TP.
*/
double Neurone::operator()(double *entries) const
{
    double res = 0;
 
    for (int i = 0; i < _n; i++)
        res += entries[i] * _poids[i];
 
    return (res > 0) ? 1 : -1;  // l'opérateur ternaire de condition sert ici à appliquer la fonction d'activation.
}

/*
    opérateur d'affectation de Neurone
    Utile pour affecter les valeurs d'une instance à une autre instance
    Si on a deux Neurones:
    Neurone a, b;
    On pourra écrire
    a = b; 
    sans causer de problème avec _poids alloué dynamiquement.
*/
Neurone & Neurone::operator=(const Neurone& other)
{
    if (this != &other) // on vérifie d'abord que l'on n'est pas dans le cas a = a qui peut poser probléme.
    {
        delete[] _poids;  // le cas a = a pose probléme à cause de ca.
        _n = other._n;
        _poids = new double[other._n];
        for (int i = 0; i < _n; i++)
            _poids[i] = other._poids[i];
    }
    return *this;   // la valeur d'une affectation est la valeur elle même, on retourne donc l'instance courante.
}                   // en déréferant le  pointeur this.



/*
    La surcharge de l'operateur << n'est pas une fonction membre de la classe Neurone
    En effet, quand on écrit cout << n << ... par exemple, le premier opérande est de type
    ostream. (le type de cout)
    On déclare donc cette surcharge comme fonction amie de la classe Neurone
    de maniére à pouvoir accéder aux champs privées de la classe Neurone facilement.
 
    Reste la question du type de retour :
    afin de pouvoir chainer les affichage :
    cout << n << endl; (<-- on utilise ici deux fois d'affilé <<)
    il faut que cout << n soit aussi de type ostream et vaille cout
    ainsi écrire cout << n << endl revient à faire :
    cout << n --> cout avec affichage de n
    cout << endl;
*/
ostream& operator<<(ostream & o, const Neurone & N)
{
  for(int i=0; i<N._n-1;i++)
    o << N._poids[i] << " "; // on utilise o comme si c'était 'cout'.
  o << N._poids[N._n-1] << endl;
  return o; // on retourne l'objet ostream recu en paramètre de manière à pouvoir chaîner les affichages.
}

