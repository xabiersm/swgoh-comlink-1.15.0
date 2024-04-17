from swgoh_comlink import SwgohComlink
import pandas as pd
import pprint
import requests

# comlink = SwgohComlink(url='http://localhost:5000')
# gameData = comlink.getGameData(include_pve_units=False)
# name = gameData['units'][256]['nameKey'].split("_",1)[1].split("_",1)[0]
# print(len(gameData['units']))
# # pprint.pprint(gameData['units'])



# # for unit in units:
# #     pprint.pprint
# pprint.pprint(name)
# pprint.pprint(gameData['units'][0]['combatType'])
# # este id coincide con definitionId de player_data
# pprint.pprint(gameData['units'][0]['id'])
# pprint.pprint(gameData['units'][0]['baseId'])
# # pprint.pprin
# player_data = comlink.get_player(229494361)
# player_name = player_data['name']
# guild_id = player_data['guildId']
# print(guild_id)
# guild = comlink.get_guild(guild_id)
# guild_name = guild['profile']['name']
# roster = player_data['rosterUnit']

# print(player_name)
# print(guild_name)
# pj = 3

# print(f"Character: {roster[pj]['definitionId'].split(':',1)[0]}")
# print(f"Level: {roster[pj]['currentLevel']}")
# print(f"Stars: {roster[pj]['currentRarity']}")
# print(f"Gear: {roster[pj]['currentTier']}")
# print(f"Relic: {roster[pj]['relic']['currentTier']-2}")
# # print(f"Combat type: {roster[pj]['combatType']}")
# print(f"guild_members = {guild['profile']['memberCount']}")
# guild_players = guild['member']
# # pprint.pprint(guild_players)
# # pillamos el id del miembro con los datos del gremio que recibimos
# player_id = guild_players[0]['playerId']
# print(f"Player ID: {player_id}")
# # obtenemos el nombre del miembro con el id 
# print(f"Player name: {comlink.get_player(player_id=player_id)['name']}")

# memberIds = []

# data = []

# # print(len(guild_players))

# # for member in range(0,guild['profile']['memberCount']):
# for member in range(0,2):
#     # pprint.pprint(member)
#     # pprint.pprint(guild_players)
#     # print(guild_players[member]['playerId'])
#     playerName = comlink.get_player(player_id=guild_players[member]['playerId']).get('name').replace(' ','_')
#     for character in roster:
#         charName = character['definitionId'].split(':',1)[0]
#         charStars = character['currentRarity']
#         charGear = character['currentTier']
#         # charRelic = character
        
#         data.append({
#             'Player name': playerName,
#             'Character name': character['definitionId'].split(':',1)[0],
#             'Stars': character['currentRarity'],
#             'Gear level': character['currentTier']
#             # 'Relic level': character['relic']['currentTier']
#         })

# df = pd.DataFrame(data)
# print(df.head(10))
# print(df.tail(10))

# print(f"longitud: {len(roster)}")
# pj_length = len(roster)
# for pj in range(0,pj_length):
    # print(roster[pj]['definitionId'])

def get_characters() -> list:
    # gameData = comlink.getGameData(include_pve_units=False)
    # characters = []
    # ships = []
    # print("Gathering all the characters...")
    # for character in range(0,len(gameData['units'])):
    #     character_id = gameData['units'][character]['baseId']
    #     combatType = gameData['units'][character]['combatType']
    #     if combatType == 1:
    #         if character_id not in characters:
    #             characters.append(character_id)
    #     elif combatType == 2:
    #         if character_id not in ships:
    #             ships.append(character_id)
    # characters.sort()
    # ships.sort()     
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