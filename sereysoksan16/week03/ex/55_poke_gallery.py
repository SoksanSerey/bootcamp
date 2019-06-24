"""
You will create a function, that take no argument and generate a HTML file. Your html will display the 151 pokemons.
"""


def poke_gallery():
    import requests

    r = requests.get(url='https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json')
    # the json file that contain all 151 pokemon characters
    reg = r.json()
    reg = reg["pokemon"]
    html_script_start = '<!DOCTYPE html>\n<html>\n\t<header>\n\t\t<title>Pokemon Image Render</title>' \
                        '\n\t</header>\n\t<body>\n'
    # open the html scrip till the body
    end_body = '\t</body>\n'
    end_html = '</html>'
    img_script_1 = '\t\t<img src="'
    # open image script
    img_script_2 = '" height="100px" width="100px">\n'
    # close image script
    f = open('pokemon.html', 'w+')
    f.write(html_script_start)
    for pic in reg:
        f.write(img_script_1)
        f.write(pic['img'])
        f.write(img_script_2)
    f.write(end_body)
    f.write(end_html)
    f.close()
    # write all the content in pokemon.html file


poke_gallery()
