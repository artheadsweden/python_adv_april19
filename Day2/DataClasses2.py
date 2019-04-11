from dataclasses import *
from math import asin, radians, sin, cos, sqrt


@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0

    def distance(self, other):
        r = 6371
        lam_1, lam_2 = radians(self.lon), radians(other.lon)
        phi_1, phi_2 = radians(self.lat), radians(other.lat)
        h = (sin((phi_2 - phi_1) / 2)**2
             + cos(phi_1) * cos(phi_2) * sin((lam_2 - lam_1) / 2)**2)
        return 2 * r * asin((sqrt(h)))


def main():
    oslo = Position("Oslo", 10.75, 59.91)
    stockholm = Position("Stockholm", 18.06, 59.32)
    print(oslo.distance(stockholm))


if __name__ == '__main__':
    main()
