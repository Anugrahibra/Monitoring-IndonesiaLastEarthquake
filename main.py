# Import Module and call the function
from lastearthquake import data_extraction, show_data

if __name__ == '__main__':
    print('Main Application')
    result = data_extraction()
    show_data(result)