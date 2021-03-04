import requests
import json
import jsonpath




# storing the variable in the url
url = "https://www.googleapis.com/books/v1/volumes?q=isbn:0131103628&key=AIzaSyBY8LEYyV5982mLwBmFkJq5dbWtdwiO3X8"
requests.get(url)

# Send Get request
response = requests.get(url)
# will print out the response
print(response)

# print response body
print(response.content)

