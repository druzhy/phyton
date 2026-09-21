#import math
#math.sqrt()

#import sys
#print(sys.path)

import requests
response = requests.get("https://www.google.com/")
print(response.text)