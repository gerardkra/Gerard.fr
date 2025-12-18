#include <cstdlib>
#include<ctime>
#include "Neurone.hh"
#include "Data.hh"

/*
    La fonction finish prend un neurone
    et un ensemble de jeux de données en paramètres.
    Pour chaque jeu, la fonction teste s'il est 
    donné dans la bonne classe par le neurone.
    Si l'ensemble des jeux passent le test, 
    la fonction renvoie true, sinon false.
*/
bool finish(Neurone &n, Data & d)
{
    for (int i = 0; i < d.getN(); i++)
        if (d.getY(i) * n(d.getX(i)) < 0)
            return false;
    return true;
}

/*
    Cette fonction prend un neurone et un objet Data
    en paramètre.
    Elle implémente l'algorithme donné dans l'énoncé
    du TP
*/
Neurone learning(Neurone& n, Data& d)
{
    while (!finish(n, d)) // ATTENTION : si l'ensemble des données n'est pas linéairement 
                          //             séparable, l'algorithme peut ne pas se terminer !    
    {
        int r = (rand() % d.getN());     // r est un nombre entier entre 0 et n - 1
        double *X = d.getX(r);          // X est un tableau de double correspond à r
        if (d.getY(r) * (n(X)) < 0)     // si la données est mal classé par le neurone
        {
            //  On applique les modifications sur le neurone
            X[0] = 0.001 * d.getY(r);           
            X[1] = 0.001 * d.getY(r) * X[1];
            X[2] = 0.001 * d.getY(r) * X[2];        
            // Utilisation ici de l'opérateur + de la classe Neurone.
            // Utilisation de l'opérateur =
            n = n + X; 
        }
        delete[] X;        // on libère l'espace alloué pour X.
    }
    return n;
}



int main()
{
    // Initialisation de la graine aléatoire.
    srand(time(NULL));

    //  Creation d'un neurone a 3 entreés (1, X, Y)
    // initialisations des poids aléatoires.
    Neurone n(3);

    // Création d'un jeu de données TEST
    double x1[4] = {-1,1,-1,1};
    double x2[4] = {-1,-1, 1, 1};
    double y[4] = {-1,1,-1,1};
    Data d(4);
    d.setX1(x1);
    d.setX2(x2);
    d.setY(y);


    // appel de la fonction d'apprentissage
    n = learning(n, d);

    // affichage du neurone.
    cout << n << endl;

    // Vérification de l'apprentissage :
    // on applique chaque jeux de données en entrées du neurone.
    for (int i = 0; i < 4; i++)
        cout  << (n(d.getX(i))) << endl;
}
