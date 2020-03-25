import requests
import csv
from datetime import datetime
from cachetools import cached, TTLCache
import dateutil.parser
from app.utils import countrycodes, date as date_util

"""
Base URL for fetching data.
"""
base_url = 'https://raw.githubusercontent.com/CSSEGISandData/2019-nCoV/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-%s.csv';

@cached(cache=TTLCache(maxsize=1024, ttl=3600))
def get_data(category):
    """
    Retrieves the data for the provided type. The data is cached for 1 hour.
    """
    # Adhere to category naming standard.
    category = category.lower().capitalize();
    # Request the data
    request = requests.get(base_url % category)
    text    = request.text
    # Parse the CSV.
    data = list(csv.DictReader(text.splitlines()))
    # The normalized locations.
    locations = []
    #add country
    add_country = []

    for item in data:
        # Filter out all the dates.
        history = dict(filter(lambda element: date_util.is_date(element[0]), item.items()))
        #sorted date history
        history = sorted_history_date(formated_date(history))
        # Country for this location.
        country = item['Country/Region']
        # Latest data insert value.
        latest = list(history.values())[-1];
        # Normalize the item and append to locations.
        if not country in add_country:
            add_country.append(country)

            locations.append({
                # General info.
                'country':  country,
                'country_code': countrycodes.country_code(country),
                'province': item['Province/State'],
                # History.
                'history': history,
                # Latest statistic.
                'total': int(latest or 0),
            })

    # Latest total.
    total = sum(map(lambda location: location['total'], locations))
    # Return the final data.
    return {
        'locations': locations,
        'total': total,
        'last_updated': datetime.utcnow().isoformat() + 'Z'
    }

"""
Get all the data for different categories (confirmed, death and recovered)
"""
def get_all_data():
    # data
    data = []
    # Get all the categories.
    confirmed = get_data('confirmed')
    deaths    = get_data('deaths')
    recovered = get_data('recovered')

    # Add confirmed
    for element in confirmed['locations']:
        data.append({
            'country':  element['country'],
            'country_code': element['country_code'],
            'province': element['province'],
            'total': {
                'confirmed': element['total']
            }
        })

    # Add death
    for country in data:
        for element in deaths['locations']:
            if element['country'] == country['country']:
                country['total']['death'] = element['total']

    # Add recovered
    for country in data:
        for element in recovered['locations']:
            if element['country'] == country['country']:
                country['total']['recovered'] = element['total']

    return {
        'data': data,
        'last_updated': dateutil.parser.parse(confirmed["last_updated"]),
        # Latest.
        'latest': {
            'confirmed': confirmed['total'],
            'deaths':    deaths['total'],
            'recovered': recovered['total'],
        }
    }

"""
Sorted data by date
"""
def sorted_history_date(data):

    return dict(sorted(data.items(), key = lambda x:datetime.strptime(x[0], '%m/%d/%Y')))

"""
Formated date in the history
"""
def formated_date(data):
    data_formated = {}

    for date in data :
        splited_date = date.split('/')
        date_formated = "{:02d}/{:02d}/{:2d}".format(int(splited_date[0]), int(splited_date[1]), int(splited_date[2]))
        data_formated[date_formated+"20"] = data[date]
    
    return data_formated

"""
Get the country name by code
"""
def get_country_name(country_code):
    data = get_data('confirmed')

    for element in data['locations']:
        if element['country_code'].lower() == country_code.lower() :
            return element['country']

    return None

"""
Sorted data by date desc
"""
def sorted_data(data, reversed):
    data_tuple = data['locations']
    data_tuple = sorted(data_tuple, key=lambda k: k.get('total', 0), reverse=reversed)
    return {
        'data': data_tuple,
        'total': data['total']
    }