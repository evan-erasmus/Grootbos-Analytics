from collections import defaultdict
import matplotlib.pyplot as plt
from datetime import datetime
from get_data import get_sorted_data


def plot_data(data=get_sorted_data()):
    datetime_values = []
    pm10_values = []
    pm2p5_values = []

    for entry in data:
        datetime_str = entry['localDate'] + ' ' + entry['localTime']
        datetime_obj = datetime.strptime(datetime_str, '%Y/%m/%d %H:%M')
        datetime_values.append(datetime_obj)
        pm10_values.append(float(entry['pm10']))
        pm2p5_values.append(float(entry['pm2p5']))

    plt.figure(figsize=(10, 6))
    plt.plot(datetime_values, pm10_values, label='PM10', marker='o', linestyle='-')
    plt.plot(datetime_values, pm2p5_values, label='PM2.5', marker='o', linestyle='-')

    plt.xlabel('Date and Time')
    plt.ylabel('Values')
    plt.title('PM10 and PM2.5 Data Over Time')

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


def plot_averages_hourly(data=get_sorted_data(), filename='Unnamed'):
    date_intervals = defaultdict(lambda: {'pm2p5_values': [], 'pm10_values': []})

    filename = filename.replace('.csv', '.png')

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
    plt.savefig(filename)
    plt.show()


def plot_data_hourly(data=get_sorted_data(), filename='Unnamed'):
    date_intervals = defaultdict(lambda: {'pm2p5_values': [], 'pm10_values': []})

    filename = filename.replace('.csv', '.png')

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
    plt.savefig(filename)
    plt.show()
