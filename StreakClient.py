import requests,json

API_KEY = "************"
baseURL = "https://www.streak.com/api/v1"
#gmail password
PASSWORD = "*******"

# Function to send request to fetch the JSON response.
def sendGetRequest(url):
    url = baseURL + url
    r = requests.get(url,auth=(API_KEY,PASSWORD))
    return r.json()

# Function to send a Delete CURL request
def sendDeleteRequest(url):
    url = baseURL + url
    r = requests.delete(url,auth=(API_KEY,PASSWORD))
    return r.json()

# Function to send Data with the request
def sendPutRequest(url,data):
    url = baseURL + url
    r = requests.put(url,data=data,auth=(API_KEY,PASSWORD))
    return r.json()

# Function to send Data using POST with the request
def sendPostRequest(url,data):
    url = baseURL + url
    headers = {'Content-Type':'application/json'}
    r = requests.post(url,json=data,auth=(API_KEY,PASSWORD),headers=headers)
    return r.json()