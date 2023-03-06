import requests
from datetime import date, datetime, timedelta
from typing import List

import httpx

async def get_earthquakes_async(start_date: datetime, end_date: datetime) -> List[str]:
    URL = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={}&endtime={}"