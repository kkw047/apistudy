import requests
import pandas as pd
import pprint
import tourist_attraction

test_a = tourist_attraction.get_tourist_sites()

for item in test_a:
 print(item)