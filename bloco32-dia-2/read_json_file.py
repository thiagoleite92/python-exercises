import json

with open('pokemons.json') as file:
	pokemons = json.load(file)["results"]


grass_pokemon_types = [
	pokemon for pokemon in pokemons if "Grass" in pokemon["type"]
]

with open("grass_pokemons.json", "w") as file:
	json_to_write = json.dumps(
		grass_pokemon_types
	)
	file.write(json_to_write)

print(pokemons[0])
print(grass_pokemon_types[0])
