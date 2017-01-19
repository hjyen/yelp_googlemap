506 Final Project Readme Template

1. Describe your project in 1-4 sentences. Include the basic summary of what it does, and the output that it should generate/how one can use the output and/or what question the output answers. 
I used yelp API to understand the common categories of restaurants around Ann Arbor and to find the top 3 price-performance restaurants and the most popular restaurants. After that, I used google distance matrix API to determine the nearest price-performance restaurant to walk from Northquad and the nearest popular restaurant by bus from my home.


2. Explain exactly what needs to be done to run your program (what file to run, anything the user needs to input, anything else) and what we should see once it is done running (should it have created a new text file or CSV? What should it basically look like?).

First run python 506_project_data.py (without internet).
You should use cached files in the same directory called sample_search_yelp.txt, sample_map_topranking.txt, and sample_map_mostpopular.txt. 
Then, you should have a new file in your directory called category.csv which contains different categories and number of counts.
Also, you can see the print results in terminal which includes top 3 price-performance restaurants, the most popular restaurants, the nearest price-performance restaurant to walk from Northquad and the nearest popular restaurant by bus from my home.


(Your program running should depend on cached data, but OK to write a program that would make more sense to run on live data and tell us to e.g. use a sample value in order to run it on cached data.)

EXAMPLE:
First run python myproject.py
Then, when it asks for a 3-letter airport code, type an airport abbreviation. You should type "DTW" to use the cached data.
You should have a new file in your directory afterward called airport_info.csv which contains... <explain further>
etc.

3. List all the files you are turning in, with a brief description of each one. (At minimum, there should be 1 Python file, 1 file containing cached data, and the README file, but if your project requires others, that is fine as well! Just make sure you have submitted them all.)

506_project_data.py: a python file includes all codes to run
sample_search_yelp.txt: cached data using yelp search API, the data is about restaurants information in Ann Arbor
sample_map_topranking.txt: cached data using google distance API, the data is about the geometric information of top 3 price-performance restaurants
sample_map_mostpopular.txt: cached data using google distance API, the data is about the geometric information of top 3 popular restaurants
506_Final_Project_Readme.txt: Project description
category.csv: The result of different categories and number of counts
506finalresult.pdf: Final result includes screenshots of terminal and a chart generated from category.csv data


4. Any Python packages/modules that must be installed in order to run your project (e.g. requests, or requests_oauthlib, or...):
unittest,requests, json, pprint

5. What API sources did you use? Provide links here and any other description necessary.
yelp search API: https://api.yelp.com/v3/businesses/search
Google Maps Distance Matrix API: 'https://maps.googleapis.com/maps/api/distancematrix/json?'

6. Approximate line numbers in Python file to find the following mechanics requirements (this is so we can grade your code!):
- Sorting with a key function: 114, 132, 154,278
- Use of list comprehension OR map OR filter: 67, 71, 81, 105, 106, 129, 143, 153, 164, 166, 273-277, 284
- Class definition beginning 1: 34
- Class definition beginning 2: 243
- Creating instance of one class: 81
- Creating instance of a second class: 284, 293
- Calling any method on any class instance (list all approx line numbers where this happens, or line numbers where 11there is a chunk of code in which a bunch of methods are invoked):91, 143, 164, 274, 275
- (If applicable) Beginnings of function definitions outside classes: 104, 142, 272
- Beginning of code that handles data caching/using cached data: 10, 189, 219
- Test cases: 303-334

8. Rationale for project: why did you do this project? Why did you find it interesting? Did it work out the way you expected?
I am a foodie and love to explore good restaurants, so I decide to access yelp API creating a list of recommended restaurants by different criteria such as location, price/performance and ranking. Additionally, I used google distance matrix API to find which one of the top3 price-performance or popular restaurants is the nearest restaurant for me. I got a useful recommendation from this project. If I want to eat a lunch at school, I should try Mezes Greek Grill because it is the top 3 price-performance restaurant and also near to Northquad. If my friend comes to visit me in Ann Arbor, I will take her/him to Zingerman's Delicatessen because it is the most popular restaurant in Ann Arbor and is near to my home by bus. 


