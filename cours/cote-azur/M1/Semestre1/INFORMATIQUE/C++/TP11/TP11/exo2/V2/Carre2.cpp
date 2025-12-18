#include "Carre2.hh"

Carre::Carre(Point2D p, double l) {
  _centre = p;
  _longueur = l;
  set_sommets();
}

void Carre::set_sommets() {
  _pts[0].x = _centre.x - _longueur/2;
  _pts[1].x = _centre.x + _longueur/2;
  _pts[2].x = _centre.x + _longueur/2;
  _pts[3].x = _centre.x - _longueur/2;
  _pts[0].y = _centre.y - _longueur/2;
  _pts[1].y = _centre.y - _longueur/2;
  _pts[2].y = _centre.y + _longueur/2;
  _pts[3].y = _centre.y + _longueur/2;
}

string Carre::to_str() const{
  string s = "Carre de centre (" + to_string(_centre.x) + ", " + to_string(_centre.y) + "), de longueur " + to_string(_longueur) + " et de sommets\n" ;
  for(int i=0;i<4;i++)
    s += "(" + to_string(_pts[i].x) + ", " + to_string(_pts[i].y) + ")\n";
  return s;
}

void Carre::apply_rot(const Rot& r) {
  _centre = r(_centre);
  
  for(int i=0;i<4;i++)
    _pts[i] = r(_pts[i]);
}
