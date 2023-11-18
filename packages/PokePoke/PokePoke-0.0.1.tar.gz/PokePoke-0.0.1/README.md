# PokePoke

The PokeAPI is a RESTful API that serves as a comprehensive database for Pokémon-related data. It offers a wide range of information about Pokémon species, their abilities, moves, types, evolutions, and more. By providing endpoints for various queries, such as retrieving details about specific Pokémon or abilities, the PokeAPI allows developers to access and utilize Pokémon-related data in their applications. It serves as a valuable resource for enthusiasts, developers, and researchers interested in integrating Pokémon-related information into their projects.

## API 
Python Basic API wrapper
```http
  https://pokeapi.co/
```

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install pokepoke
```

## Usage

```python
from pokemon import pokeball

def main():
    poke_api = pokeball()

    # Meminta pengguna untuk memasukkan nama Pokémon
    pokemon_name = input("Masukkan nama Pokémon: ")
    pokemon_info = poke_api.get_pokemon_info(pokemon_name)
    if pokemon_info:
        print(f"Info untuk {pokemon_name.capitalize()}:")
        print(f"Berat: {pokemon_info['weight']}")
        print(f"Kemampuan: {', '.join([ability['ability']['name'] for ability in pokemon_info['abilities']])}")
    else:
        print("Pokémon tidak ditemukan.")

if __name__ == "__main__":
    main()
```
