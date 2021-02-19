# ZmanimAPI
An API to get Zmanim for any Longitude and Latitude

## Documentation and usage

All API requests start at the base url: http://jsw68.pythonanywhere.com/. For shortening purposes, this will be referred to as URL. 

#### API Documentation

There are four kinds of requests that can be added to that Base URL:
1. URL/api/lat/lon - This gives the Zmanim for the place with the latitude lat and the longitude lon. 
2. URL/api/lat/lon/date - Same as number 1, except there is an optional date string at the end. This date should be in the form YYYY-MM-DD. 
3. URL/api/us/zip_code - This gives the Zmanim for the area with the zip code of zip_code. 
4. URL/api/us/zip_code/date - Same as number 3 except with an optional date string at the end in the form YYY-MM-DD.

Note: Right now, only US zip codes are supported. 
All times are given in the local time for the area inputted. 

#### Website Documentation

If you want to view the Zmanim in a more eye-pleasing manner, these are the URLS for you.
They are the same as their API counterparts, except without the /api/. 

Here they are in the website format:
1. URL/lat/lon - This gives the Zmanim for the place with the latitude lat and the longitude lon. 
2. URL/lat/lon/date - Same as number 1, except there is an optional date string at the end. This date should be in the form YYYY-MM-DD. 
3. URL/us/zip_code - This gives the Zmanim for the area with the zip code of zip_code. 
4. URL/us/zip_code/date - Same as number 3 except with an optional date string at the end in the form YYY-MM-DD.

If you want to search in the web browser, use URL/search. 
There is an option for search by city name or by zip code (us only). There is also a date option. 

#### ToDo
1. Add line by line comments for the project
2. Add API view and regular view for cities outside of the search function. 
3. Nicer errors, less errors

#### Contact
To contact the author: 2022.j.wainberg@shalhevet.org




