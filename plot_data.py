from collections import defaultdict
import matplotlib.pyplot as plt
from datetime import datetime
from get_data import get_sorted_data


def plot_data(data=get_sorted_data()):

    datetime_values = []
    pm10_values = []
    pm2p5_values = []
    co_values = []
    no2_values = []
    so2_values = []
    no_values = []
    voc_values = []
    rh_values = []
    pressure_values = []
    sensorTemp_values = []
    heaterTemp_values = []
    internalTemp_values = []

    for entry in data:
        datetime_str = entry['localDate'] + ' ' + entry['localTime']
        datetime_obj = datetime.strptime(datetime_str, '%Y/%m/%d %H:%M')
        datetime_values.append(datetime_obj)
        pm10_values.append(float(entry['pm10']))
        pm2p5_values.append(float(entry['pm2p5']))
        co_values.append(float(entry['co']))
        no2_values.append(float(entry['no2']))
        so2_values.append(float(entry['so2']))
        no_values.append(float(entry['no']))
        voc_values.append(float(entry['voc']))
        rh_values.append(float(entry['rh']))
        pressure_values.append(float(entry['pressure']))
        sensorTemp_values.append(float(entry['sensorTemp']))
        heaterTemp_values.append(float(entry['heaterTemp']))
        internalTemp_values.append(float(entry['internalTemp']))

    data_headers = {
        'pm10': pm10_values,
        'pm2p5': pm2p5_values,
        'co': co_values,
        'no2': no2_values,
        'so2': so2_values,
        'no': no_values,
        'voc': voc_values,
        'rh': rh_values,
        'pressure': pressure_values,
        'sensorTemp': sensorTemp_values,
        'heaterTemp': heaterTemp_values,
        'internalTemp': internalTemp_values,
    }

    plt.figure(figsize=(10, 6))

    match graph_type:
        case 1:
            for i in other_axis:
                plt.plot(datetime_values, data_headers[i], label=i, marker='o', linestyle='-')
            plt.xlabel('Date and Time')
            plt.ylabel('Values')
            plt.title(f'{", ".join(other_axis)} Data Over Time')
        case 2:
            for i in other_axis:
                plt.bar(datetime_values, data_headers[i])
            plt.xlabel('Date and Time')
            plt.ylabel('Values')
            plt.title(f'{", ".join(other_axis)} Data Over Time')
        # case 3:
        #
        # case 4:
        #
        # case 5:
        #
        # case 6:

    plt.xticks(rotation=90)

    plt.legend()

    plt.tight_layout()
    plt.show()


def plot_averages(data=get_sorted_data()):
    date_intervals = defaultdict(lambda: {'pm2p5_values': [], 'pm10_values': []})

    for entry in data:
        datetime_str = entry['localDate'] + ' ' + entry['localTime']
        datetime_obj = datetime.strptime(datetime_str, '%Y/%m/%d %H:%M')
        date = datetime_obj.strftime('%Y/%m/%d')
        date_intervals[date]['pm2p5_values'].append(float(entry['pm2p5']))
        date_intervals[date]['pm10_values'].append(float(entry['pm10']))

    unique_dates = sorted(date_intervals.keys())
    pm2p5_means = [sum(date_intervals[date]['pm2p5_values']) / len(date_intervals[date]['pm2p5_values']) for date in
                   unique_dates]
    pm10_means = [sum(date_intervals[date]['pm10_values']) / len(date_intervals[date]['pm10_values']) for date in
                  unique_dates]

    plt.figure(figsize=(12, 6))
    plt.bar(unique_dates, pm2p5_means, label='PM2.5', alpha=0.7, width=0.4)
    plt.bar(unique_dates, pm10_means, label='PM10', alpha=0.7, width=0.4, bottom=pm2p5_means)

    plt.xlabel('Date')
    plt.ylabel('Average Values')
    plt.title('Average PM10 and PM2.5 Data by Date')

    plt.xticks(rotation=90)

    plt.legend()

    plt.tight_layout()
    plt.show()


def plot_averages_hourly(data=get_sorted_data()):
    date_intervals = defaultdict(lambda: {'pm2p5_values': [], 'pm10_values': []})

    for entry in data:
        datetime_str = entry['localDate'] + ' ' + entry['localTime']
        datetime_obj = datetime.strptime(datetime_str, '%Y/%m/%d %H:%M')

        # Calculate the 6-hour interval start time
        interval_start = datetime_obj.replace(hour=(datetime_obj.hour // 6) * 6, minute=0, second=0, microsecond=0)
        interval_label = interval_start.strftime('%Y/%m/%d %H:%M')

        date_intervals[interval_label]['pm2p5_values'].append(float(entry['pm2p5']))
        date_intervals[interval_label]['pm10_values'].append(float(entry['pm10']))

    unique_intervals = sorted(date_intervals.keys())
    pm2p5_means = [sum(date_intervals[interval]['pm2p5_values']) / len(date_intervals[interval]['pm2p5_values']) for
                   interval in unique_intervals]
    pm10_means = [sum(date_intervals[interval]['pm10_values']) / len(date_intervals[interval]['pm10_values']) for
                  interval in unique_intervals]

    plt.figure(figsize=(12, 6))
    plt.bar(unique_intervals, pm2p5_means, label='PM2.5', alpha=0.7, width=0.4)
    plt.bar(unique_intervals, pm10_means, label='PM10', alpha=0.7, width=0.4, bottom=pm2p5_means)

    plt.xlabel('6-Hour Intervals')
    plt.ylabel('Average Values')
    plt.title('Average PM10 and PM2.5 Data by 6-Hour Interval')

    plt.xticks(range(len(unique_intervals)), unique_intervals, rotation=90)

    plt.legend()

    plt.tight_layout()
    plt.show()


def plot_data_hourly(data=get_sorted_data()):
    date_intervals = defaultdict(lambda: {'pm2p5_values': [], 'pm10_values': []})

    for entry in data:
        datetime_str = entry['localDate'] + ' ' + entry['localTime']
        datetime_obj = datetime.strptime(datetime_str, '%Y/%m/%d %H:%M')

        interval_start = datetime_obj.replace(hour=(datetime_obj.hour // 6) * 6, minute=0, second=0, microsecond=0)
        interval_label = interval_start.strftime('%Y/%m/%d %H:%M')

        date_intervals[interval_label]['pm2p5_values'].append(float(entry['pm2p5']))
        date_intervals[interval_label]['pm10_values'].append(float(entry['pm10']))

    unique_intervals = sorted(date_intervals.keys())
    pm2p5_means = [sum(date_intervals[interval]['pm2p5_values']) / len(date_intervals[interval]['pm2p5_values']) for
                   interval in unique_intervals]
    pm10_means = [sum(date_intervals[interval]['pm10_values']) / len(date_intervals[interval]['pm10_values']) for
                  interval in unique_intervals]

    plt.figure(figsize=(12, 6))
    plt.plot(unique_intervals, pm2p5_means, label='PM2.5', marker='o', linestyle='-')
    plt.plot(unique_intervals, pm10_means, label='PM10', marker='o', linestyle='-')

    plt.xlabel('6-Hour Intervals')
    plt.ylabel('Values')
    plt.title('PM10 and PM2.5 Data Over 6-Hour Intervals')

    plt.xticks(rotation=90)

    plt.legend()

    plt.tight_layout()
    plt.show()
