class PlayerModel:
    def __init__(self, first_name="", last_name="", birth_date=None):
        self._first_name = first_name
        self._last_name = last_name
        self._birth_date = self._validate_birth_date(birth_date)

    # Getter methods
    def get_first_name(self) -> str:
        return f"First Name: {(self._first_name).capitalize()}"

    def get_last_name(self) -> str:
        return f"Last Name: {(self._last_name).upper()}"

    def get_birth_date(self) -> str:
        return self._birth_date

    # Setter methods
    def set_first_name(self, first_name):
        self._first_name = first_name

    def set_last_name(self, last_name):
        self._last_name = last_name

    def set_birth_date(self, birth_date):
        self._birth_date = self._validate_birth_date(birth_date)

    # Validate birth date
    def _validate_birth_date(self, birth_date):
        if birth_date is None:
            return None

        day, month, year = map(int, birth_date)
        day_str = str(day).zfill(2)  # Ajoute un zéro initial si nécessaire
        if 1 <= int(day_str) <= 31 and 1 <= month <= 12:
            return (day_str, month, year)
        else:
            raise ValueError("Invalid birth date. Day should be between 1 and 31, and month between 1 and 12.")

    def formatted_birth_date(self):
        if self._birth_date is None:
            return None
        else:
            return f"Birth Date: ({self._birth_date[0]}, {self._birth_date[1]:02d}, {self._birth_date[2]})"

# Example usage:
if __name__ == "__main__":
    # Create an instance of the PlayerModel
    player = PlayerModel()

    # Set player attributes
    try:
        player.set_first_name(("jean"))
        player.set_last_name(("Dupont"))
        player.set_birth_date(('10', '01', 1999))
    except ValueError as e:
        print(e)

    # Get and print player information
    print(player.get_first_name(), type(player.get_first_name()))
    print(player.get_last_name(), type(player.get_last_name()))
    print(player.formatted_birth_date(), type(player.formatted_birth_date()))
