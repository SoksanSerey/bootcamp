"""
You will create a function that take a string list in parameter and return a list of tuple with two elements:
(1. ID, 2. NAME). The string list parameter will represent a Pokemon Type. (for example ‘Fire’, ‘Water’, ‘Psychic’...)
To do so, you will make a get request to the endpoint, and find every Pokemon that got the desired type inside
the ‘type’ Key (it’s represent a string array).
"""


def poke_type(input_list):
    import requests

    r = requests.get(url='https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json')
    reg = r.json()
    reg_new = reg['pokemon']
    # open json file and write it as python document
    new_list = []
    for i in reg_new:
        if set(input_list).issubset(i['type']):
            # search type of pokemon base on the list that input
            new_list.append((i['id'], i['name']))
    return new_list


# print(poke_type(['Water', 'Fire']))
