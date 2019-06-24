def json_to_tsv(json_file, tsv_file):
    """
    This function is used to convert the content in json file into tsv file
    :param json_file: json file path
    :param tsv_file: tsv file path
    :return: return 1 if it is success and 0 if it fail
    """
    import json
    import csv

    try:
        input_file = open(json_file, 'r')  # read the json file
        output_file = open(tsv_file, "w+")  # write the tsv file
        data = json.load(input_file)  # convert json file into list that contain dict
        input_file.close()  # close the json file

        output = csv.writer(output_file, delimiter='\t', lineterminator='\n')
        # write the content into tsv type
        output.writerow(data[0].keys())
        for row in data:
            output.writerow(row.values())
        output_file.close()  # close tsv file
        return 1
    except (ValueError, FileNotFoundError):
        return 0


# print(json_to_tsv('.//test//demo.json', './test/output.tsv'))
