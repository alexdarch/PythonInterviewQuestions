from datetime import datetime
from solution import get_earthquakes_async
import asyncio

START_DATE = datetime.strptime("2014-01-01", "%Y-%m-%d")
END_DATE = datetime.strptime("2014-03-05", "%Y-%m-%d")

ids = asyncio.run(get_earthquakes_async(START_DATE, END_DATE))
print(ids)