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


def get_other_axis():
    print('\nWhat axis would you the other axis to represent?')

    j = 0
    choices = []
    available_choices = []
    headers = get_csv_headers()

    for i in headers:
        j = j + 1
        available_choices.append(j)
        print(f'{str(j)}. {i}')

    print("Enter the corresponding number of your choice, then hit enter. Type \"done\" once you have entered all "
          "your choices.")

    is_busy = True
    check_options = 1

    while is_busy:
        input_value = input('New option: ')
        if input_value == 'done' or check_options == len(headers):
            is_busy = False
        else:
            try:
                if int(input_value) in available_choices:
                    if int(input_value) not in choices:
                        choices.append(headers[int(input_value) - 1])
                    else:
                        print("Already selected. Please select a different option or type \"done\".")
                else:
                    print("Invalid choice. Please select a valid option or type \"done\".")
            except:
                print("Invalid choice. Please select a valid option or type \"done\".")
    return choices


def get_graph_type():
    print('\nWhat graph type would you like to use?')
    print("1. Line Graph")
    print("2. Scatter Plot")
    print("3. Bar Chart")
    print("4. Stem Plot")
    print("5. Filled Between")
    print("6. Stack Plot")
    choice = int(input("Enter the corresponding number of your choice, then hit enter: "))

    if choice in [1, 2, 3, 4, 5, 6]:
        return choice
    else:
        print("Invalid choice. Please select a valid option.")
        get_graph_type()


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


def get_plot_default():
    print('\nWhat would you like to plot?')
    print("1. Averages")
    print("2. Raw data")
    data_to_plot = input("Enter the corresponding number of your choice, then hit enter: ")
    choice = int(data_to_plot)

    if choice == 1:
        print(plot_averages())
        exit(0)
    elif choice == 2:
        print(plot_data())
        exit(0)
    else:
        print("Invalid choice. Please select a valid option.")
        get_plot_default()


if __name__ == '__main__':
    get_plot()
    # print()
    # get_other_axis()
