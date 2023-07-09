import requests
from datetime import date, datetime, timedelta
from typing import List


def get_earthquakes_sync(start_date: datetime, end_date: datetime) -> List[str]:
    URL = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={0}&endtime={1}"

    all_dates = [start_date + timedelta(days=x) for x in range((end_date - start_date).days + 1)]
    dates = [datetime.strftime(x, "%Y-%m-%d") for x in all_dates 
         if (x - start_date).days % 30 == 0 or x == end_date or x == start_date]

    all_features = []
    for d1, d2 in zip(dates[:-1], dates[1:]):
        data = requests.get(URL.format(d1, d2)).json()
        features = [{'id': x['id'], 
                    'mag': x['properties']['mag']
                    } for x in data['features'] if x['properties']['mag'] is not None and x['properties']['mag'] >= 5.0]
        # print(f"[d1: {d1}, d2: {d2}]:  {len(features)} items")
        all_features.extend(features)
    ids = [x['id'] for x in sorted(all_features, key=lambda x: x['mag'])]
    
    return ids