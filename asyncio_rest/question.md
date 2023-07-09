# List of earthquake IDs

In this question we are going to get a list of specific earthquake ids from the US govt earthquake API:

`https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={0}&endtime={1}`

your function, `get_earthquakes(start_date: datetime, end_date: datetime) -> List[str]:` must take in a start date and an end date and make several queries to the USGS api. The starttime and endtime that you send in your request matter
- they cannot be more than a month apart, otherwise the query will take too long
- they cannot be less than a month apart otherwise USGS will think that you are DoS-ing their server and block you.

For example, given the (start_date, end_date) pair: ("2014-01-01", "2014-03-05") you may make these calls to the api:
```
https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2014-01-01&endtime=2014-01-31
https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2014-01-31&endtime=2014-03-02
https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2014-03-02&endtime=2014-03-05
```

Note that the API is exclusive on the end date. I.e. https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2014-01-01&endtime=2014-01-02 will only return earthquakes on 2014-01-01.

When you receive the response, you must then return a list of earthquake ids the a magnitude greater than or equal to 5.0, and in ascending order of the magnitude.

There are multiple ways in which you can do this question. It may be easier to first do it with the synchronous requests library, and then upgrade to using asyncio and either aiohttp or httpx