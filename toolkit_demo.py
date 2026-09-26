from basic_physics import force, kinetic_energy, potential_energy
from unit_converter import celsius_to_kelvin, meters_to_kilometers


def main():
    mass = 2
    velocity = 5
    height = 10
    gravity = 9.81

    print("Physics Research Computing Toolkit")
    print("-----------------------------------")

    print("Force:", force(mass, 3), "N")
    print("Kinetic Energy:", kinetic_energy(mass, velocity), "J")
    print("Potential Energy:", potential_energy(mass, gravity, height), "J")

    print("25 °C in Kelvin:", celsius_to_kelvin(25), "K")
    print("5000 m in kilometers:", meters_to_kilometers(5000), "km")


if __name__ == "__main__":
    main()
