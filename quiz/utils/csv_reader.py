# Python standard library imports
import csv
from typing import Dict


def read_csv(file_path: str) -> Dict:
    """Read csv file into a list of dictionaries.

    Args:
        file_path (str): File path of the csv data to read.

    Returns:
        Dict: List of dictionaries.
    """
    try:
        with open(file_path) as csvfile:
            reader = csv.DictReader(csvfile)
            csv_dict_list = []
            for row in reader:
                csv_dict_list.append({key: value for key, value in row.items()})
            return csv_dict_list
    except FileNotFoundError as err:
        print(
            f"{err}, please provide a corect path to the file with questions and answers!"
        )
