import requests
import pandas as pd
import pprint
import tourist_attraction
import food_location

test_a = tourist_attraction.get_tourist_sites()
test_b = food_location.get_Cheongju()
test_c = food_location.get_Chungju()

for item in test_a:
    print(item)

for item in test_b:
    print(item)

for item in test_c:
    print(item)