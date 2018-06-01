# E-Commerce-CheapHerder

Readme for Cheapherder


The following application allows users to place an order on a product collectively. The thought process behind this is that if one is to visit a wholesale website such as Alibaba then what becomes apparent is that there is a required minimum quantity purchase for said item. For instance, say we wanted to purchase water bottles from Alibaba. Most of the water bottle products listed on there will have a minimum quantity purchase of 1000 items. The cheap prices for items available on Alibaba are due in part to the fact that the user is required to order a massive quantity of said product. Our application allows multiple users to place an order on one product. So if we go back to our water bottle example, one user may pledge to buy 200 water bottles while another may pledge to buy 50. Until the minimum quantity requirement is not met, the group order is available for any user to pledge a certain amount. Allowing users to collectively place an order not only helps the user get a much lower price on a product but also takes away the burden from having to order an unnecessary amount for a particular product. 

The following application had two custom built Web Scrapers to get product listings and information into our database. We scraped product information from both DHgate and Kole imports (https://www.dhgate.com  & https://www.koleimports.com ). After the web scraper had scraped the product information, we developed a script to insert this information into the database.

The application has two perspectives. One perspective is the seller’s side while the other is the buyer’s side. On the seller’s side we are able to not only upload products for the buyers to see but also change any information that is related to a current product that may have been posted in the past. 

Aside from the main feature of allowing multiple users to place one order, other advance functions that we implemented in this project were a live-chat feature which allowed users from the buyer’s perspective to communicate with one another (Especially useful for users who are involved in the same group order for a product). We also implemented a recommendation feature that looked at a user’s search history and mined frequent words that the user searched for. Then the function would take these frequent words and find products that had these words in the product description.

Though it may be confusing to navigate through the different files and code of this project, the essential core functionality lies within the views.py file. The file can be found at the path: CheapHerder/CheapHerder/views.py

DEMO DEMONSTRATION: A Demo of the application can be found on YouTube https://www.youtube.com/watch?v=Zz4h4_KdsfI