# smart_dash
A Flask/Python home dashboard easily deployed and maintained as a docker container

## Configure Modules
### Weather
This module is to allow for weather lookup based on the location provided to the app config.
The app is built to lookup using the apixu weather api. This does assume a free tier 10k api call per month, and uses 
caching to retain the api results of each call to avoid overages. This can be adjusted in the app configs
 
|config_name|description|default_value|
|---|---|---|
|W_MONTHLY_API_LIMIT|This is the apixu limit|10000|
|W_API_CACHE_LIMIT|*Auto-generated based on monthly limit* |2592000/W_MONTHLY_API_LIMIT|
|W_BASE_URL|Base API URL|'http://api.apixu.com'|
|W_VERSION|Version of api|'v1'|
|W_ZIPCODE|Zip code of the weather lookup desired|06770|

### 