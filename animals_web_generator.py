import json
from typing import List

REPLACE_ANIMAL_INFO = "__REPLACE_ANIMALS_INFO__"


def run_app():
    animals_data = load_data('data/animals_data.json')
    html_template = load_template('templates/original/animals_template.html')

    html_template = html_template.replace(REPLACE_ANIMAL_INFO,
                                          parse_animal_data_to_html(animals_data))

    with open('templates/animals_template.html', 'w') as f:
        f.write(html_template)


def parse_animal_data_to_html(animals_data: List[dict]) -> str:
    animal_html_data = ""

    for animal in animals_data:
        animal_html_data += serialize_animal(animal)

    return animal_html_data

def serialize_animal(animal: dict) -> str:
    # Grab the raw data from the animal
    animal_name = animal.get("name")
    animal_diet = animal.get("characteristics").get("diet")
    animal_location = animal.get("locations")[0]
    animal_type = animal.get("characteristics").get("type")

    animal_html_data = ""

    animal_html_data += '<li class="cards__item">\n'  # Open the list item

    # Add animal information to the HTML
    if animal_name: animal_html_data += f'<div class="card__title">{animal_name}</div>\n'
    animal_html_data += '<p class="card__text">\n'
    if animal_diet: animal_html_data += f"<strong>Diet:</strong> {animal_diet}<br/>\n"
    if animal_location: animal_html_data += f"<strong>Location:</strong> {animal_location}<br/>\n"
    if animal_type: animal_html_data += f"<strong>Type:</strong> {animal_type}<br/>\n"
    animal_html_data += '</p>\n'

    animal_html_data += '</li>\n'  # Close the list item

    return animal_html_data


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
