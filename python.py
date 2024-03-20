import os
import json
from control.control_main import MainControl

# Constante
DATABASE_DIRECTORY = "data"
DIRECTORY_CONTENT = ("players", "tournaments")


def create_directory_if_not_exists(directory_path: str, file: str):
    """
    Creates a directory if it does not already exist and
    initializes an empty JSON file within it.

    Args:
        directory_path (str): The path of the directory to be created.
        file (str): The name of the file (including extension)
        to be created within the directory.
    """
    directory_file = os.path.join(directory_path, file)
    if not os.path.exists(directory_file):
        os.makedirs(directory_file)

        json_file_path = os.path.join(directory_file, f"{file}.json")
        with open(json_file_path, "w", encoding="utf-8") as outfile:
            json.dump("", outfile)


def main():
    """
    Main function that ensures the existence of specified
    directories within the DATABASE_DIRECTORY.

    Iterates through the folders listed in DIRECTORY_CONTENT and calls the
    create_directory_if_not_exists function to create each folder
    within the DATABASE_DIRECTORY.
    """
    for folder in DIRECTORY_CONTENT:
        create_directory_if_not_exists(DATABASE_DIRECTORY, folder)

    MainControl()


if __name__ == '__main__':
    main()
