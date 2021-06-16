"""
This program parses data from a .csv file and serialises that data into a .json file.

Project structure:
  - output.json     (write)     The result of data parsing and serialisation.
  - TestCases.csv   (read)      File that is being parsed.
  - TestCases.json  (example)   File that gives an example of correct output.

Program flow: 
  { csv_file -> reader_object -> data_matrix -> rows -> columns -> json_output }
"""

import csv, json

RELEVANT_INDEXES = (1, 4, 5, 6, 2)
COLUMN_NAMES = ("testKey", "start", "finish", "comment", "status")

KEY_1_NAME = "testExecutionKey"
KEY_2_NAME = "tests"

KEY_1_VALUE = "SSP50-8832"

csv_dict = {
    KEY_1_NAME : KEY_1_VALUE,
    KEY_2_NAME : []
}

def time_reformat(time):
    order = (2, 0, 1)
    last_part = ":00+01:00"
    step_0 = time.split(" ")
    step_1 = step_0[0].split("/")
    step_2 = [step_1[i] for i in order]
    step_3 = "-".join(step_2)
    step_4 = step_3[:len(step_3)-1] + '0' + step_3[len(step_3)-1:]
    step_5 = step_4 + 'T' + step_0[1] + last_part
  
    for index, item in enumerate([step_0, step_1, step_2, step_3, step_4, step_5]):
        print("Step {}: {}".format(index, item))
    print()

    return step_5

def key_value_map(values):
    keys = COLUMN_NAMES
    order = RELEVANT_INDEXES
    map_dict = {}

    for n in range(len(keys)):
        if n == 1 or n == 2:
            map_dict[keys[n]] = time_reformat(values[order[n]])
        else:
            map_dict[keys[n]] = values[order[n]]

    csv_dict[KEY_2_NAME].append(map_dict)

with open("TestCases.csv", 'r') as read_file:
    csv_reader = csv.reader(read_file, delimiter=';')
    csv_matrix = list(csv_reader)
    for row in range(1, len(csv_matrix)):
        key_value_map(csv_matrix[row])

with open("output.json", 'w') as write_file:
    json.dump(csv_dict, write_file, indent=4)