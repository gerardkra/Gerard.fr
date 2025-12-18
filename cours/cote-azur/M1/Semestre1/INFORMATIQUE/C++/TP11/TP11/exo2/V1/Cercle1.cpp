#include "Cercle1.hh"

Cercle::Cercle(const Point2D& p, double l): _rayon(l), Forme(p) {} // seule syntaxe possible pour _centre
//Cercle::Cercle(const Point2D& p, double l) {
//  _rayon = l;
//  _centre = p;
//}
string Cercle::to_str() const{
  return "Cercle de centre (" + to_string(_centre.x) + ", " + to_string(_centre.y) + ") et de rayon " + to_string(_rayon);
}

