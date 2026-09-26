def velocity(distance, time):
    """Calculate velocity."""
    return distance / time


def acceleration(change_in_velocity, time):
    """Calculate acceleration."""
    return change_in_velocity / time


def force(mass, acceleration):
    """Calculate force using F = ma."""
    return mass * acceleration


def kinetic_energy(mass, velocity):
    """Calculate kinetic energy."""
    return 0.5 * mass * velocity**2


def potential_energy(mass, gravity, height):
    """Calculate gravitational potential energy."""
    return mass * gravity * height


if __name__ == "__main__":
    mass = 2
    velocity_value = 5
    height = 10
    gravity = 9.81

    print("Basic Physics Calculations")
    print("--------------------------")
    print("Velocity:", velocity(100, 10), "m/s")
    print("Force:", force(mass, 3), "N")
    print("Kinetic Energy:", kinetic_energy(mass, velocity_value), "J")
    print("Potential Energy:", potential_energy(mass, gravity, height), "J")
