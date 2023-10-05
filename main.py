from plot_data import plot_data, plot_averages


def get_plot():
    print('What would you like to plot?\n')
    print("1. Averages")
    print("2. Raw data")
    data_to_plot = input("Enter the corresponding number of your choice, then hit enter: ")
    choice = int(data_to_plot)

    if choice == 1:
        print(plot_averages())
        exit(1)
    elif choice == 2:
        print(plot_data())
        exit(1)
    else:
        print("Invalid choice. Please select a valid option.")
        get_plot()


if __name__ == '__main__':
    get_plot()
