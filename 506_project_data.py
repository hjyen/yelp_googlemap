import unittest
import requests
import json
import pprint


#-------yelp search API-------#


try:
	# read caching data
	sample_search = open('sample_search_yelp.txt').read() 
	food_lst = json.loads(sample_search)

except:
	app_id = 'GDJoP3wI8NpCJGPWarSBDA'
	app_secret = 'g14W0ZKtK8Jk1Ali0YQys9DjibYKcp3nSwX32PDM0TO9K63nNAUXRSodY8RhlvrX'
	data = {'grant_type': 'client_credentials','client_id': app_id,'client_secret': app_secret}
	token = requests.post('https://api.yelp.com/oauth2/token', data=data)
	access_token = token.json()['access_token']
	baseurl_search = 'https://api.yelp.com/v3/businesses/search'
	headers = {'Authorization': 'bearer %s' % access_token}
	params = {}
	params['location'] = 'Ann Arbor'
	params['term'] = 'restaurant'
	resp_search = requests.get(baseurl_search, params=params, headers=headers)
	food_lst = resp_search.json()['businesses']
	# cache the data
	f_search = open('sample_search_yelp.txt' , 'w')
	f_search.write(json.dumps(food_lst))
	f_search.close()


class Food():
	def __init__(self, food_dict={}):
		if 'name' in food_dict:
			self.name = food_dict['name']
		else:
			self.name = ""

		if 'categories' in food_dict:
			self.categories = food_dict['categories']
		else:
			self.categories = []

		if 'rating' in food_dict:
			self.rating = food_dict['rating']
		else:
			self.rating = 0
 
		if 'review_count' in food_dict:
			self.review_count = food_dict['review_count']
		else:
			self.review_count = 0

		if 'coordinates' in food_dict:
			self.coordinates = food_dict['coordinates']
		else:
			self.coordinates = {}

		if 'price' in food_dict:
			self.price = food_dict['price']
		else:
			self.price = ""

	def get_pricelevel(self):
		pricelevel = [len(p) for p in self.price.split()]
		return pricelevel

	def get_category_type(self):
		category_lst= [c['alias'] for c in self.categories]
		return category_lst

	def get_coordinates_str(self):
		latitude = self.coordinates['latitude']
		longitude = self.coordinates['longitude']
		coordinates_str = str(latitude)+','+str(longitude)
		return coordinates_str


food_insts = [Food(data) for data in food_lst]
# print len(food_insts)


# [Price_Performance]
print "\n\n***** Price_Performance *****"


price_lst = []
for insts in food_insts:
	price_lst.append(insts.get_pricelevel()[0])
# print price_lst

rating_lst=[]
for insts in food_insts:
	rating_lst.append(insts.rating)
# print rating_lst

name_lst = []
for insts in food_insts:
	name_lst.append(insts.name)


def pricerating(food_insts):
	pr_ratio = [r/p for p,r in zip(price_lst, rating_lst)]
	restaurant_prratio_dic = {name_lst[i]:pr_ratio[i] for i in range(len(name_lst))}

	# dict = {keys[i]: values[i] for i in range(len(keys))}

	return restaurant_prratio_dic

#print pricerating(food_insts)   # type(pricerating(food_insts)) == dict

ranking = sorted(pricerating(food_insts), key = pricerating(food_insts).get, reverse=True)
# print ranking

top3ranking = ranking[:3]
print 'Top 3 price-perfromance restaurants are '+top3ranking[0]+', '+top3ranking[1]+', '+top3ranking[2]+'.'


## [Popular_Restaurant]
print "\n\n***** Popular_Restaurant *****"

review_count_lst = []
for insts in food_insts:
	review_count_lst.append(insts.review_count)


restaurant_popular_dic = {name_lst[i]:review_count_lst[i] for i in range(len(name_lst))}
# print restaurant_popular_dic

popularity = sorted(restaurant_popular_dic, key = restaurant_popular_dic.get, reverse=True)
# print popularity

top3popularity = popularity[:3]
print 'Top 3 popular restaurants are '+top3popularity[0]+', '+top3popularity[1]+', '+top3popularity[2]+'.'


## [Popular_Category]
print "\n\n***** Popular_Category *****"

def popular_category(food_insts):
	category_total = [insts.get_category_type() for insts in food_insts]

	all_typies_dict = {}
	for restaurant in category_total:
		for c in restaurant:
			if c in all_typies_dict:
				all_typies_dict[c] += 1
			else:
				all_typies_dict[c] = 1

	all_typies_tuple = [(i,all_typies_dict[i]) for i in all_typies_dict]
	all_typies_tuple.sort(key=lambda x:x[1], reverse=True)
	return all_typies_tuple

print popular_category(food_insts)



## [Restaurant_Coordinates]
print "\n\n***** Restaurant_Coordinates *****"

coordinates_lst = [insts.get_coordinates_str() for insts in food_insts]

name_location_dict = dict(zip(name_lst,coordinates_lst))
pprint.pprint(name_location_dict) 



# Write code to create your emo_scores.csv file
new_file = open('category.csv','w')
new_file.write('category, numbers\n')


for i in popular_category(food_insts):
	new_file.write(str(i[0])+','+ str(i[1])+'\n')




#------- google matrix API -------#

northquad = "42.280732,-83.740025"
mezes = name_location_dict["Mezes Greek Grill"]
neo = name_location_dict['NeoPapalis']
pilar = name_location_dict["Pilar's Tamales"]

try:
	# read caching data
	sample_map_topranking = open('sample_map_topranking.txt').read() 
	map_topranking_dict = json.loads(sample_map_topranking)

except:
	google_key = 'AIzaSyCCTeKohvbDkYWNqo37eT7PgP5apOXn-3Q'
	baseurl_map ='https://maps.googleapis.com/maps/api/distancematrix/json?'

	map_params = {}
	map_params['origins'] = northquad
	map_params['destinations'] = mezes+'|'+neo+'|'+pilar
	map_params['mode'] = 'walking'
	map_params['key'] = google_key

	resp_map = requests.get(baseurl_map, params=map_params)
	map_topranking_dict = resp_map.json()

	f_map = open('sample_map_topranking.txt' , 'w')
	f_map.write(json.dumps(map_topranking_dict))
	f_map.close()



home = "42.2565806,-83.7357371"
zingerman = name_location_dict["Zingerman's Delicatessen"]
frita = name_location_dict['Frita Batidos']
roadhouse = name_location_dict["Zingerman's Roadhouse"]


try:
	# read caching data
	sample_map_mostpopular = open('sample_map_mostpopular.txt').read() 
	map_mostpopular_dict = json.loads(sample_map_mostpopular)

except:
	google_key = 'AIzaSyCCTeKohvbDkYWNqo37eT7PgP5apOXn-3Q'
	baseurl_map ='https://maps.googleapis.com/maps/api/distancematrix/json?'

	map_params_pop = {}
	map_params_pop['origins'] = northquad
	map_params_pop['destinations'] = zingerman+'|'+frita+'|'+roadhouse
	map_params_pop['mode'] = 'transit'
	map_params_pop['transit_mode']= 'bus'
	map_params_pop['key'] = google_key

	resp_map_pop = requests.get(baseurl_map, params=map_params_pop)
	map_mostpopular_dict = resp_map_pop.json()

	f_map_pop = open('sample_map_mostpopular.txt' , 'w')
	f_map_pop.write(json.dumps(map_mostpopular_dict))
	f_map_pop.close()


class Map():
	def __init__(self, map_dict={}):
		if 'duration' in map_dict:
			self.duration = map_dict['duration']['value']
		else:
			self.duration = 0
		if 'distance' in map_dict:
			self.distance = map_dict['distance']['value']
		else:
			self.distance = 0
		if 'status' in map_dict:
			self.status = map_dict['status']
		else:
			self.status = 'not OK'


	def get_duration(self):
		minutes = self.duration/60 
		seconds = self.duration%60
		return str(minutes)+" minutes and "+str(seconds)+" seconds" 

	def get_distance(self):
		km = float(self.distance)/1000
		return str(km)+'km'



## [Nearest_Top_Restaurant]
print "\n\n***** Nearest_Top_Restaurant *****"
def time_distance(map_insts, restaurant):
	time_lst= [insts.duration for insts in map_insts]
	time_str_lst= [insts.get_duration() for insts in map_insts]
	distance_str_lst = [insts.get_distance() for insts in map_insts]
	status_lst = [insts.status for insts in map_insts]
	restaurant_time_tuple = zip(restaurant, time_lst, time_str_lst, distance_str_lst, status_lst)
	restaurant_time_tuple.sort(key = lambda x:x[1])
	nearest_status = restaurant_time_tuple[0][4]
	if nearest_status == "OK":
		return restaurant_time_tuple[0]


top_map_insts = [Map(data) for data in map_topranking_dict['rows'][0]['elements']] 

nearest_top_ranking = time_distance(top_map_insts, top3ranking)
print 'It takes ' +nearest_top_ranking[2]+' to walk from NorthQuad to '+ nearest_top_ranking[0]+' with a distance of '+nearest_top_ranking[3]+'.'


## [Nearest_Pop_Restaurant]
print "\n\n***** Nearest_Pop_Restaurant *****"

pop_map_insts = [Map(data) for data in map_mostpopular_dict['rows'][0]['elements']]

nearest_pop_restauraunt = time_distance(pop_map_insts, top3popularity)
print 'It takes ' +nearest_pop_restauraunt[2]+' by bus from my home to '+ nearest_pop_restauraunt[0]+' with a distance of '+nearest_pop_restauraunt[3]+'.'




##### TESTS BELOW #########
print "\n\n***** TESTS *****"
class Price_Performance(unittest.TestCase):
	def test1(self):
		self.assertEqual(type(food_insts), type([]), "testing that food_insts is a list")
	def test2(self):
		self.assertEqual(len(pricerating(food_insts)), 20, 'testing that length of pricerating is 20')
	def test3(self):
		self.assertEqual(type(pricerating(food_insts)), type({}), 'testing that type of pricerating is a dict' )

class Popular_Restaurant(unittest.TestCase):
	def test4(self):
		self.assertEqual(len(review_count_lst), len(name_lst)), 'testing that length of review_count_lst is equal to length of name_lst'

class Popular_Category(unittest.TestCase):
	def test5(self):
		self.assertEqual(type(popular_category(food_insts)), type([]), 'testing that type is a list')

class Restaurant_Coordinates(unittest.TestCase):
	def test6(self):
		self.assertEqual(len(coordinates_lst), 20, 'testing that length of pricerating is 20')
	def test7(self):
		self.assertTrue("eat" in name_location_dict)

class Nearest_Top_Restaurant(unittest.TestCase):
	def test8(self):
		self.assertEqual(len(top_map_insts), 3, 'testing that length of top_map_insts is 3')
	def test9(self):
		self.assertEqual(type(nearest_top_ranking[2]), type(''), 'testing that type is a string' )
class Nearest_Pop_Restaurant(unittest.TestCase):
	def test10(self):
		self.assertEqual(type(nearest_pop_restauraunt[1]), type(100), 'testing that type is a integer')

unittest.main(verbosity=2)
