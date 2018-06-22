# API Integration

Readme for API Integration (note project was developed using python 2.7 and Django version 1.11)


The following application integrates API information that is yielded from making calls to Yelp and Zomato’s API. Initially, scripts for both Yelp and Zomato API were created to load restaurants and the corresponding information returned from the API call (separate tables for Yelp/Zomato API restaurant information) into the database of the web application. Some preconfigured runs of the scripts were made to load some samples into both the Yelp and Zomato API tables. The scripts can be adjusted to yield information for restaurants according to geographical location which can be specified by zip code and city name.

The main objective of the application is to combine the information returned from both Yelp and Zomato’s API for a restaurant. So, at times there is logistical information provided by Zomato such as the average cost of two people dinning at the restaurant which is not provided by Yelp. Likewise, Yelp’s API provides images related to the restaurant while Zomato’s API does not. Furthermore, another key driving point behind the application is to integrate the reviews given on both Yelp and Zomato for a restaurant. Unfortunately, Yelp limits their review API call to only three for a restaurant while Zomato’s limit is five. While in total, the application has eight reviews for a restaurant that can be found on both Yelp and Zomato, the reviews are limited to brief text excerpts due to the nature of the API response. 

Additionally, some other interesting functions were implemented which cannot be found on either Yelp or Zomato. A recommended recipe function was created to help users find recipes that relates to a specific restaurant’s cuisine type. Another implemented function gives users a list of recommended recipes and restaurants based off the cuisine type of their most recent searched restaurant on the application.

Documentation and comments can be found throughout the code. Most of the backend implementation lies at the following path: finalproject/polls/views.py. While the schema and tables for the database of the application can be found at finalproject/polls/models.py. Moreover, frontend for styling and presenting the application can be found at finalproject/finalproject/templates

     
