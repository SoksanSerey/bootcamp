"""
You will create a function that take one string in argument that’s represent a valid a url and then return the HTML
code of the page as a string. (No need output for this function but you might need to print your results before
submitting your work).
"""


def get_html(webpage):
    import requests

    r = requests.get(webpage, )
    output_string = r.text
    return output_string


# print(get_html('https://www.techbeamers.com/websites-to-practice-selenium-webdriver-online/'))
