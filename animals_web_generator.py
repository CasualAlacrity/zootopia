import json
from typing import List

REPLACE_ANIMAL_INFO = "__REPLACE_ANIMALS_INFO__"


def run_app():
    animals_data = load_data('data/animals_data.json')
    html_template = load_template('templates/animals_template.html')

    html_template = html_template.replace(REPLACE_ANIMAL_INFO, print_animals(animals_data))
    with open('templates/animals_template.html', 'w') as f:
        f.write(html_template)


def print_animals(animals_data: List[dict]) -> str:
    animal_data = ""
    for animal in animals_data:
        animal_name = animal.get("name")
        animal_diet = animal.get("characteristics").get("diet")
        animal_location = animal.get("locations")[0]
        animal_type = animal.get("characteristics").get("type")

        if animal_name: animal_data += f"Name: {animal_name}\n"
        if animal_diet: animal_data += f"Diet: {animal_diet}\n"
        if animal_location: animal_data += f"Location: {animal_location}\n"
        if animal_type: animal_data += f"Type: {animal_type}\n"

    return animal_data


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def load_template(file_path):
    """ Loads a HTML template """
    with open(file_path, "r") as handle:
        return handle.read()


if __name__ == "__main__":
    run_app()
