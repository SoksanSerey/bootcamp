"""
You will create a function that take one string in argument ( that’s represent a valid a facebook url or fb username
and then a tuple with the request status_code ( usually it will be 200 ) in the first element the associated ID in the
second element ) If no ID is found, you will return a tuple with the status_code as first element and 0 in the
second element.
"""


def get_fbid(fburl):
    import requests

    end_url = 'https://findmyfbid.com/'
    param = {'url': fburl}
    p = requests.post(end_url, param)
    # post the the param into the end url
    dict_result = p.json()
    # if the input is valid, it will return as dict, else it will return as list
    if isinstance(dict_result, dict):
        output_tuple = (p.status_code, dict_result['id'])
        # write the status code into tuple as first element and id as second element
        return output_tuple
    elif isinstance(dict_result, list):
        output_tuple = (p.status_code, 0)
        # write the status code into tuple as first element and 0 as second element
        return output_tuple


# print(get_fbid("https://www.facebook.com/soksan.serey16"))
# print(get_fbid("zuck"))
# print(get_fbid("adwopawpodawodpwdpwoawopdwopawopdw"))
