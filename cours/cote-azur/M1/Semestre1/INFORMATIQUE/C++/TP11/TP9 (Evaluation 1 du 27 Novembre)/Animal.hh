using namespace std;

// declaration de la classe Animal
class Animal{
private:
  string _nom; // nom de l'Animal (prive)
  double _poids; // poids de l'Animal (prive)
public:
  Animal(); // constructeur sans argument
  Animal(string, double); // constructeur a 2 arguments
  void affiche() const; // fonction d'affichage 
  double get_poids() const; // getter du poids
  string get_nom() const; // getter du nom
};

