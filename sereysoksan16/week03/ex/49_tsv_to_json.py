def tsv_to_json(tsv_file, json_file):
    """
    This function is used to convert tsv file into json file
    :param tsv_file: path of tsv file
    :param json_file: path of json file
    :return: 1 if the process is success and 0 is not
    """
    import csv
    import json

    try:
        with open(tsv_file, 'r') as tsvFile:
            file_reader = csv.DictReader(tsvFile, dialect='excel-tab')
            row_list = list(file_reader)
        with open(json_file, 'w+') as jsonFile:
            jsonFile.write(json.dumps(row_list, indent=4))
        return 1
    except (ValueError, FileNotFoundError):
        return 0


# print(tsv_to_json('./test/output.tsv', './/test//demos.json'))
