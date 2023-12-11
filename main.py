
from absciss  import Point
from absciss  import TroisPoints


point1 = Point(1, 2)
point2 = Point(3, 4)
point3 = Point(5, 6)


print("Coordonnées des points:")
print(point1)
print(point2)
print(point3)


print("Les points 1 et 2 sont égaux:", point1 == point2)
print("Les points 1 et 3 sont égaux:", point1 == point3)


distance = point1.calculer_distance(point2)
print(f"Distance entre le point 1 et le point 2: {distance}")

milieu = point1.calculer_milieu(point2)
print(f"Milieu entre le point 1 et le point 2: {milieu}")


triangle = TroisPoints(point1, point2, point3)


print("Les points du triangle sont alignés:", triangle.sont_alignes())


print("Le triangle formé par les points est isocèle:", triangle.est_isocele())
