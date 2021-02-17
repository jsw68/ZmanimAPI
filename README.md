# ZmanimAPI
An API to get Zmanim for any Longitude and Latitude

## Documentation and usage

The base url for all of the following will be represnted as: URL. 
There is no up-to-date URL as of now. 

#### API Documentation

All API requests start at the base url: URL/api/

There are four kinds of requests that can be added to that Base URL:
1. URL/api/lat/lon - This gives the Zmanim for the place with the latitude lat and the longitude lon. 
2. URL/api/lat/lon/date - Same as number 1, except there is an optional date string at the end. This date should be in the form YYYY-MM-DD. 
3. URL/api/us/zip_code - This gives the Zmanim for the area with the zip code of zip_code. 
4. URL/api/us/zip_code/date - Same as number 3 except with an optional date string at the end in the form YYY-MM-DD.

Note: Right now, only US zip codes are supported. 

#### Website Documentation

If you want to view the Zmanim in a more eye-pleasing manner, these are the URLS for you.
They are the same as their API counterparts, except without the /api/. 

Here they are in the website format:
1. URL/lat/lon - This gives the Zmanim for the place with the latitude lat and the longitude lon. 
2. URL/lat/lon/date - Same as number 1, except there is an optional date string at the end. This date should be in the form YYYY-MM-DD. 
3. URL/us/zip_code - This gives the Zmanim for the area with the zip code of zip_code. 
4. URL/us/zip_code/date - Same as number 3 except with an optional date string at the end in the form YYY-MM-DD.

#### ToDo
1. Search bar
2. Support for getting Zmanim from a city name, specifically helps for places outside of the US
3. Nicer errors, less errors
4. Update the PythonAnywhere site

#### Contact
To contact the author: 2022.j.wainberg@shalhevet.org




