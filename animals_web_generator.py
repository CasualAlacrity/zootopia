import json
from typing import List


def run_app():
    animals_data = load_data('data/animals_data.json')
    print_animals(animals_data)


def print_animals(animals_data: List[dict]):
    for animal in animals_data:
        animal_name = animal.get("name")
        animal_diet = animal.get("characteristics").get("diet")
        animal_location = animal.get("locations")[0]
        animal_type = animal.get("characteristics").get("type")

        if animal_name:     print(f"Name: {animal_name}")
        if animal_diet:     print(f"Diet: {animal_diet}")
        if animal_location: print(f"Location: {animal_location}")
        if animal_type:     print(f"Type: {animal_type}")
        print("")  # New line for better readability


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


if __name__ == "__main__":
    run_app()
