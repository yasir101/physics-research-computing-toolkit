def meters_to_kilometers(meters):
    """Convert meters to kilometers."""
    return meters / 1000


def kilometers_to_meters(kilometers):
    """Convert kilometers to meters."""
    return kilometers * 1000


def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin."""
    return celsius + 273.15


def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius."""
    return kelvin - 273.15


def grams_to_kilograms(grams):
    """Convert grams to kilograms."""
    return grams / 1000


def kilograms_to_grams(kilograms):
    """Convert kilograms to grams."""
    return kilograms * 1000


if __name__ == "__main__":
    print("Physics Unit Converter")
    print("----------------------")
    print("1000 m =", meters_to_kilometers(1000), "km")
    print("25 °C =", celsius_to_kelvin(25), "K")
    print("500 g =", grams_to_kilograms(500), "kg")
