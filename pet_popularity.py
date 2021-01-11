#Tracking Pet Popularity Online
#scrape the wikipedia page for pets
#count the number of times a particular pet appreas on that page HTML 
#analyze our results.
import requests
url = "https://en.wikipedia.org/wiki/Pet"
r = requests.get(url)
#converting the returned object into a string
r = r.text
pets = ["cats", "dogs", "snakes", "fish", "bird", "monkey", "iguana"]
for pet in pets:
 print("{} : {} mentions ". format(pet, r.count(pet) ) )

#dog is the most mentioned pet in the wiki page.