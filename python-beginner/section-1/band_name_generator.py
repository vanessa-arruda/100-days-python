print("----------------------------------------")
print("---Welcome to the Band Name Generator---")
print("----------------------------------------\n")


def generate_band_name(city: str, animal: str) -> str:
    return f"Your band name could be {city} {animal}!"


city = input("What's your favorite city? \n")
animal = input("What's your favorite animal or pet's name? \n")
print(generate_band_name(city, animal))
