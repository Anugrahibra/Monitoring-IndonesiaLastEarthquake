# Monitoring-IndonesiaLastEarthquake

This package aims to provide an easy way to obtain the latest earthquake information in Indonesia, as reported by the Indonesian Meteorology, Climatology, and Geophysics Agency (BMKG). 

## HOW IT WORK
This package will scrape from BMKG to get latest earthquake happened in Indonesia

This package will use BeautifulSoup4 and Requests to produce output in the form of JSON that is ready to be used in web or mobile application

## HOW TO USE
```python
import lastearthquake

if __name__ == '__main__':
    print('Main Application')
    result = data_extraction()
    show_data(result)
```