// # Pour compiler (à faire dans le terminal de Visual Studio Code ou celui de Linux ou Mac)
// g++ exo3.cpp -o exo3
//
// # Pour exécuter (à faire dans le terminal de Visual Studio Code ou celui de Linux ou Mac)
// ./exo3

// L'utilisateur entrera les valeurs demandées du tableau.
// Ici, dans l'exemple du main, la taille des tableaux est imposée et vaut n=5 (cf ligne 64).

#include <iostream>
#include <cstdlib>
#include <ctime>   // pour srand mais pas toujours nécessaire selon les machines

using namespace std;

double* create_array(int n)
{
  double* d = new double[n];
  return d;
}

double get_kbd_number()
{
  double r;
  cout << "Entrer un réel" << endl;
  cin >> r;
  return r;
}

double get_rand_number()
{
  double r = (double) rand()/RAND_MAX;  // on peut écrire "double r = 1.0*rand()/RAND_MAX;"  la multiplication étant prioritaire
  return r;
}

void init_array_kbd(double* t, int n)
{
  for(int i=0;i<n;i++)
    t[i] = get_kbd_number();
}

void init_array_rand(double* t, int n)
{
  for(int i=0;i<n;i++)
    t[i] = get_rand_number();
}

void apply(double* t, int n, double (*f)())
{
  for(int i=0;i<n;i++)
    t[i] = f();
}

void affiche(double *t, int n)
{
  for(int i=0;i<n-1;i++)
    cout << t[i] << " ";    // les valeurs du tableau sur une seule ligne
  cout << t[n-1] << endl;  //  saut de  ligne final
}
int main()
{

  srand(time(NULL));   // pour que le tirage soit "aléatoire"
  int n = 5; //10;

  double* t;
  t = create_array(n);  // equivalent a t = new double[n];

  double r = get_kbd_number();
  cout << "kbd number = " << r << endl;

  r = get_rand_number();
  cout << "rand number = " << r << endl;

  cout << "init_array_kbd" << endl;
  init_array_kbd(t, n);
  affiche(t,n);

  cout << "init_array_rand" << endl;
  double* t1 =  create_array(n);   // equivalent a t1 = new double[n];
  init_array_rand(t1, n);
  affiche(t1,n);

  cout << "apply + get_rand_number" << endl;
  double*  t2 = create_array(n); // equivalent a t2 = new double[n];
  apply(t2, n, get_rand_number);
  affiche(t2,n);

  cout << "apply + get_kbd_number" << endl;
  double*  t3 = create_array(n); // equivalent a t3 = new double[n];
  apply(t3, n, get_kbd_number);
  affiche(t3,n);

  delete [] t;  // desallocation
  delete [] t1;
  delete [] t2;
  delete [] t3;
}
