
Note that the API is exclusive on the end date. I.e. https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2014-01-01&endtime=2014-01-02 will only return earthquakes on 2014-01-01 
("2014-01-01", "2014-03-05") => ['2014-01-01', '2014-01-31', '2014-03-02', '2014-03-05']