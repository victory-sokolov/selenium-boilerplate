import csv
import random

import yaml


def read_configs():
    params = {}
    with open("config.yml", 'r') as ymlfile:
        config = yaml.safe_load(ymlfile)['SETTINGS']

    for key, value in config.items():
        params[key] = value
    return params


def get_file_entries(file_name: str):
    """
        Read csv file and construct dictionary from data, where:
        1.) key   -> csv header
        2.) value -> csv column value
    """
    with open(file_name, 'r', encoding="utf-8") as file:
        csv_reader = csv.reader(file)

        header = next(csv_reader, None)
        data = {i.replace(' ', '_'): [] for i in header}

        keys = data.keys()
        for line in csv_reader:
            for key, i in zip(keys, line):
                data[key].append(i)
        return data


def get_random_file_entry(file_name: str) -> str:
    with open(file_name, 'r', encoding="utf-8-sig") as file:
        csv_reader = csv.reader(file)
        entry_list = [line[0] for line in csv_reader]
    return random.choice(entry_list)


def slow_connection_simulation(driver, latency=10):
    driver.set_network_conditions(
        offline=False,
        latency=latency,
        download_throughput=500 * 1024,
        upload_throughput=500 * 1024)
