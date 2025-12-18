#include "Cercle2.hh"

//Cercle::Cercle(const Point2D & p, double l): _centre(p), _rayon(l) {} // ko
Cercle::Cercle(const Point2D & p, double l) {
  _centre = p;
  _rayon = l;
}

string Cercle::to_str() const{
  return "Cercle de centre (" + to_string(_centre.x) + ", " + to_string(_centre.y) + ") et de rayon " + to_string(_rayon);
}

void Cercle::apply_rot(const Rot& r) {
  _centre = r(_centre);
}
