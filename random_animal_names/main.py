import numpy as np
from importlib import resources


def generate_name():
    
    with resources.open("animals.txt") as animals_file:
        animals = list(animals_file)
        animal = np.random.choice(animals).strip("\n")

    with resources.open("nationalities.txt") as nationalities_file:
        nationalities = list(nationalities_file)
        nationality= np.random.choice(nationalities).strip("\n")

    with resources.open("english-adjectives.txt") as adjectives_file:
        adjectives = list(adjectives_file)
        adjective = np.random.choice(adjectives).strip("\n")

    animal_name = f"{adjective} {nationality} {animal}"
    
    return animal_name

