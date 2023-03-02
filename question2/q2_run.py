from datetime import datetime
import functions as f 

START_DATE = datetime.strptime("2014-01-01", "%Y-%m-%d")
END_DATE = datetime.strptime("2014-03-05", "%Y-%m-%d")

ids = f.get_earthquakes(START_DATE, END_DATE)
print(ids)