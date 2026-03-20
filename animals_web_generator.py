import json
from typing import List

REPLACE_ANIMAL_INFO = "__REPLACE_ANIMALS_INFO__"


def run_app():
    animals_data = load_data('data/animals_data.json')
    html_template = load_template('templates/original/animals_template.html')

    skin_type = get_selected_skin_type(animals_data)

    html_template = html_template.replace(REPLACE_ANIMAL_INFO,
                                          parse_animal_data_to_html(animals_data, skin_type))

    with open('templates/animals_template.html', 'w') as f:
        f.write(html_template)


def get_selected_skin_type(animals_data: List[dict]) -> str:
    skin_types = get_list_of_skin_types(animals_data)

    print("Available skin types:")
    for i, skin_type in enumerate(skin_types, start=1):
        print(f"{i}: {skin_type}")

    while True:
        try:
            option = int(input("Please choose a skin type: "))
            if 1 <= option <= len(skin_types):
                return skin_types[option - 1]

            print("Invalid choice. Please choose a valid number.\n")
        except ValueError:
            print("Invalid input, please enter a number.\n")
            continue

    return ""


def get_list_of_skin_types(animals_data: List[dict]) -> List[str]:
    skin_types = []

    for animal in animals_data:
        characteristics = animal.get("characteristics")
        skin_type = characteristics.get("skin_type")
        if skin_type:
            skin_types.append(skin_type)

    # Remove duplicates
    skin_types = list(dict.fromkeys(skin_types))

    return skin_types


def parse_animal_data_to_html(animals_data: List[dict], skin_type: str) -> str:
    animal_html_data = ""

    for animal in animals_data:
        # Check if the animal's skin type matches the selected skin type
        skin_type_match = animal.get("characteristics").get("skin_type") == skin_type

        if skin_type_match:
            animal_html_data += serialize_animal(animal)

    return animal_html_data


def serialize_animal(animal: dict) -> str:
    # Grab the raw data from the animal
    animal_name = animal.get("name")
    animal_diet = animal.get("characteristics").get("diet")
    animal_location = animal.get("locations")[0]
    animal_type = animal.get("characteristics").get("type")
    skin_type = animal.get("characteristics").get("skin_type")

    animal_html_data = ""

    animal_html_data += '<li class="cards__item">\n'  # Open the list item

    # Add animal information to the HTML
    if animal_name: animal_html_data += f'<div class="card__title">{animal_name}</div>\n'
    animal_html_data += '<div class="card__text">\n<ul>\n'
    if animal_diet: animal_html_data += f"<li><strong>Diet:</strong> {animal_diet}</li>\n"
    if animal_location: animal_html_data += f"<li><strong>Location:</strong> {animal_location}</li>\n"
    if animal_type: animal_html_data += f"<li><strong>Type:</strong> {animal_type}</li>\n"
    if skin_type: animal_html_data += f"<li><strong>Skin Type:</strong> {skin_type}</li>\n"
    animal_html_data += '</ul>\n</div>\n'

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
