from get_data import get_file_names, get_specific_filedata, get_sorted_data
from plot_data import plot_data, plot_averages, plot_averages_hourly, plot_data_hourly


def get_file():
    print('Which file would you like to use?')

    j = 0
    available_choices = []
    files = get_file_names()

    for i in files:
        j = j + 1
        available_choices.append(j)
        print(f'{str(j)}. {i}')

    input_value = input("Enter the corresponding number of your choice, then hit enter (\"all\" for all files): ")

    if input_value == "all":
        return get_sorted_data()
    elif int(input_value) in available_choices:
        return get_specific_filedata(int(input_value))
    else:
        print("Invalid choice. Please select a valid option.")
        get_file()


def get_hourly_intervals():
    print('Would you like the data to be represented in 6 hour intervals?')
    print("1. Yes")
    print("2. No")
    choice = int(input("Enter the corresponding number of your choice, then hit enter: "))

    if choice == 1:
        return True
    elif choice == 2:
        return False
    else:
        print("Invalid choice. Please select a valid option.")
        get_hourly_intervals()


def get_plot():
    print('What would you like to plot?')
    print("1. Averages")
    print("2. Raw data")
    data_to_plot = input("Enter the corresponding number of your choice, then hit enter: ")
    choice = int(data_to_plot)

    if choice == 1:
        if get_hourly_intervals():
            print(plot_averages_hourly(get_file()))
        else:
            print(plot_averages(get_file()))
        exit(1)
    elif choice == 2:
        if get_hourly_intervals():
            print(plot_data_hourly(get_file()))
        else:
            print(plot_data(get_file()))
        exit(1)
    else:
        print("Invalid choice. Please select a valid option.")
        get_plot()


if __name__ == '__main__':
    get_plot()
