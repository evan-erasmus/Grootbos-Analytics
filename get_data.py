import csv
import os

data_dir = './Data'
filenames = os.listdir(data_dir)


def get_file_names():
    return filenames


def get_sorted_data():
    combined_data = []
    result_data = []

    for filename in filenames:
        csv_file_path = f'./Data/{filename}'
        data_list = []

        with open(csv_file_path, mode='r', newline='') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data_list.append(row)

        combined_data.append(data_list)

    for set in combined_data:
        for record in set:
            result_data.append(record)

    sorted_data = sorted(result_data, key=custom_sort_key)

    return sorted_data


def get_specific_filedata(choice):
    combined_data = []
    result_data = []

    i = 0

    # for filename in filenames:
    csv_file_path = f'{data_dir}/{filenames[i]}'
    data_list = []

    with open(csv_file_path, mode='r', newline='') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data_list.append(row)

    combined_data.append(data_list)

    for set in combined_data:
        for record in set:
            result_data.append(record)

    # result_data = list(unique_everseen(result_data))
    sorted_data = sorted(result_data, key=custom_sort_key)

    return sorted_data


def custom_sort_key(item):
    date_time_str = item['localDate'] + ' ' + item['localTime']
    return date_time_str
