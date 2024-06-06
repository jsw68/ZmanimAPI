# ZmanimAPI
An API to get Zmanim for anywhere around the world. 

Technologies used: Python, Django, JavaScript, HTML

## Documentation and usage

To search via a GUI, see the search feature at http://jsw68.pythonanywhere.com/search/. 
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

The easiest way to view the website is through the [search feature](https://jsw68.pythonanywhere.com/search), found at URL/search. 
The search feature allows to search by date, zip code (US only), and city. 

If you want to view the Zmanim in a more eye-pleasing manner, these are the URLS for you.
They are the same as their API counterparts, except without the /api/. 

Here they are in the website format:
1. URL/lat/lon - This gives the Zmanim for the place with the latitude lat and the longitude lon. 
2. URL/lat/lon/date - Same as number 1, except there is an optional date string at the end. This date should be in the form YYYY-MM-DD. 
3. URL/us/zip_code - This gives the Zmanim for the area with the zip code of zip_code. 
4. URL/us/zip_code/date - Same as number 3 except with an optional date string at the end in the form YYY-MM-DD.

