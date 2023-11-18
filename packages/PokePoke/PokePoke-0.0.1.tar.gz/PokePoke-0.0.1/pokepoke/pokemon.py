import requests

class pokeball:
    def __init__(self):
        self.base_url = "https://pokeapi.co/api/v2"

    def get_pokemon_info(self, pokemon_name):
        url = f"{self.base_url}/pokemon/{pokemon_name.lower()}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_pokemon_ability(self, ability_name):
        url = f"{self.base_url}/ability/{ability_name.lower()}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
