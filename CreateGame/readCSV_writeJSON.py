import csv
import json
from collections import defaultdict

"""
Reads the CSV file and creates a Dict

eliminated initialized to false, kills set to 0

"""
def read_csv():

    python_dict = defaultdict(dict)

    with open('Martel Assassins sign up (Responses) - Form Responses 1.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        next(csv_reader)

        first_flag = True
        first_line = None
        prev_line = None

        # Timestamp, Email Address, Full Name, Year, On campus?, Email
        # howard <-> sabrina <-> akshat
        for line in csv_reader:
            if first_flag:
                first_line = line
                first_flag = False
            name = line[2]
            python_dict[name]["email"] = line[5]
            python_dict[name]["year"] = line[3]
            python_dict[name]["on campus"] = True if line[4] == "Yes" else False
            python_dict[name]["eliminated"] = False
            python_dict[name]["kills"] = 0
            python_dict[name]["email"] = line[5]
            if prev_line:
                python_dict[name]["targeted by"] = prev_line[2]
                python_dict[prev_line[2]]["target"] = name
            prev_line = line

        # line = the last line
        python_dict[first_line[2]]["targeted by"] = line[2]
        python_dict[line[2]]["target"] = first_line[2]
        # print(python_dict)

        json_obj = json.dumps(python_dict)

        with open('game.json', 'w') as outfile:
            outfile.write(json_obj)

read_csv()

if __name__ == "__main__":
    pass