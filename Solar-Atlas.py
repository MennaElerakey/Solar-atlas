def show_mercury():
    print("\nMercury")
    print("Distance from Sun: 57.9 million km")
    print("Moons: 0")
    print("Gravity: 3.7 m/s²")

def show_venus():
    print("\nVenus")
    print("Distance from Sun: 108.2 million km")
    print("Moons: 0")
    print("Gravity: 8.87 m/s²")

def show_earth():
    print("\nEarth")
    print("Distance from Sun: 149.6 million km")
    print("Moons: 1")
    print("Gravity: 9.8 m/s²")

def show_moon():
    print("\nThe Moon")
    print("Distance from Earth: 384,400 km")
    print("Gravity: 1.62 m/s²")

def show_mars():
    print("\nMars")
    print("Distance from Sun: 227.9 million km")
    print("Moons: 2")
    print("Gravity: 3.71 m/s²")

def show_jupiter():
    print("\nJupiter")
    print("Distance from Sun: 778.5 million km")
    print("Moons: 95")
    print("Gravity: 24.79 m/s²")

def show_saturn():
    print("\nSaturn")
    print("Distance from Sun: 1.43 billion km")
    print("Moons: 146")
    print("Gravity: 10.44 m/s²")

def show_uranus():
    print("\nUranus")
    print("Distance from Sun: 2.87 billion km")
    print("Moons: 28")
    print("Gravity: 8.87 m/s²")

def show_neptune():
    print("\nNeptune")
    print("Distance from Sun: 4.5 billion km")
    print("Moons: 16")
    print("Gravity: 11.15 m/s²")

def main():
    print("Welcome to Solar Atlas!")
    print("Planets: Mercury, Venus, Earth, Moon, Mars, Jupiter, Saturn, Uranus, Neptune")

    while True:
        choice = input("\nEnter a planet name (or 'exit' to quit): ").lower()

        if choice == "mercury":
            show_mercury()
        elif choice == "venus":
            show_venus()
        elif choice == "earth":
            show_earth()
        elif choice == "moon":
            show_moon()
        elif choice == "mars":
            show_mars()
        elif choice == "jupiter":
            show_jupiter()
        elif choice == "saturn":
            show_saturn()
        elif choice == "uranus":
            show_uranus()
        elif choice == "neptune":
            show_neptune()
        elif choice == "exit":
            print("Exiting the Solar System Explorer. Goodbye!")
            break
        else:
            print("Unknown name. Please try again.")

main()
