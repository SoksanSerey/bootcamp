"""
You will create a function, that will take one string list as parameters and return a list of tuple.
Each string element of the list represent a currency pair
For each pair you have inside your array, you will add one element in your tuple list
"""


def get_currency(string_list):
    import requests
    from datetime import datetime

    try:
        # if type is wrong or key error
        list01 = []
        url = 'https://www.freeforexapi.com/api/live'
        separator = ','
        pairs_items = separator.join(string_list)
        # convert list into string list
        param = {'pairs': pairs_items}
        r = requests.post(url, params=param)
        reg = r.json()
        req_new = reg['rates']
        # get json file and write it as python doc
        for key in req_new:
            time_stamp = req_new[key]['timestamp']
        # get timestamp from the json file
        current_datetime = datetime.fromtimestamp(time_stamp)
        current_datetime = current_datetime.strftime('%d/%m/%Y %H:%M')
        # convert timestamp into readable date
        for key in req_new:
            list01.append((key, req_new[key]['rate'], req_new[key]['timestamp'], current_datetime))
        return list01
    except (TypeError, KeyError):
        return 'The currency pair ' + str(string_list) + ' was not recognised or supported'


# print(get_currency(['EURUSD', 'EURGBP', 'USDGBP']))
# print(get_currency(['ABCDEF']))
