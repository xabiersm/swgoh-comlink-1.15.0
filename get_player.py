from swgoh_comlink import SwgohComlink
import pandas as pd
import pprint
import requests

def get_characters() -> list:
  
    data = []
    characters = []
    response = requests.get("https://swgoh.gg/api/characters")

    if response.status_code == 200:
        data = response.json()
        for character in range(0,len(data)):
            character_id = data[character]['base_id']
            if character_id not in characters:
                characters.append(character_id)
    return characters
    
def get_ships() -> list:

    response = requests.get("https://swgoh.gg/api/ships/")
    ships = []
    data = []

    if response.status_code == 200:
        data = response.json()
        for ship in range(0,len(data)):
            ship_id = data[ship]['base_id']
            if ship_id not in ships:
                ships.append(ship_id)

    return ships

def swgoh_app(guild_id: str) -> None:
    comlink = SwgohComlink(url='http://localhost:5000')
    #cargamos datos del gremio
    guild = comlink.get_guild(guild_id)
    #guardamos todos los jugadores del gremio
    guildMembers = guild['member']
    
    #guardamos todos los personajes del juego (incluso los de evento, habria que filtrar)
    characters = get_characters()
    ships = get_ships()
    print(len(characters))
    print(len(ships))
    with open(r'./characters.txt','w') as fp:
        fp.write('\n'.join(characters))

    with open(r'./ships.txt','w') as fp:
        fp.write('\n'.join(ships)) 

if __name__ == "__main__":
    guild_id = "4iqC_x0yQ22UEMG4znEL5A"
    swgoh_app(guild_id)