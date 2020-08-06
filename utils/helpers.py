import random
import yaml
import csv

def read_configs():
    params = {}
    with open("config.yml", 'r') as ymlfile:
        config = yaml.safe_load(ymlfile)['SETTINGS']

    for key, value in config.items():
        params[key] = value
    return params


def get_file_entries(file_name: str):
    with open(file_name, 'r', encoding="utf-8-sig") as file:
        csv_reader = csv.reader(file)
        entry_list = [line[0] for line in csv_reader]
    return entry_list


def get_random_file_entry(file_name: str) -> str:
    with open(file_name, 'r', encoding="utf-8-sig") as file:
        csv_reader = csv.reader(file)
        entry_list = [line[0] for line in csv_reader]
    return random.choice(entry_list)
