import requests
import pprint
import Establish

'''https://stellarium.org/doc/head/remoteControlApi.html#rcStelPropertyService'''
'''THis is the site for the documentation. Cool stuff!'''
# Define the base URL for Stellarium's API assuming the server is running on localhost at port 8090
BASE_URL = "http://localhost:8090/api/stelproperty/find?str="


# Function to make an API request to Stellarium to find an object
def find_object_in_stellarium(object_name):
    # Construct the full URL with the object name
    full_url = f"{BASE_URL}{object_name}"

    # Make the GET request to the Stellarium API
    response = requests.get(full_url)

    # Check if the response is successful
    if response.status_code == 200:
        # Return the JSON data if successful
        return response.json()
    else:
        # Return an error message if the request was unsuccessful
        return f"Error: {response.status_code}, {response.reason}"

#main_poll gets the surrent state of the system. Make 2 calls to it, the first with no parameters.
#then get the data['actionChanges']['id'], data['propertyChanges']['id'] and rerun this method with
#those two numbers. every subsequent time this method is run, it will return a list of changes to stellarium.

def main_poll(param1 = -2, param2 = -2):
    BASE_URL = "http://localhost:8090/api/main/status"
    #for the first poll, we are passing -2 for both parameters. this will return a full list of the properties.

    response = requests.get(BASE_URL, params={'actionId': param1, 'propId': param2})


    # Check if the response is successful
    if response.status_code == 200:
        # Return the JSON data
        return response.json()
    else:
        # Return an error message
        return f"Error: {response.status_code}, {response.reason}"
def get_specific_property():
    BASE_URL = "http://localhost:8090/api/stelproperty/"
    property_name = 'list'

    # Construct the full URL
    full_url = f"{BASE_URL}{property_name}"

    # Make the GET request
    response = requests.get(full_url)

    # Check if the response is successful
    if response.status_code == 200:
        # Return the JSON data
        return response.json()
    else:
        # Return an error message
        return f"Error: {response.status_code}, {response.reason}"


def location_search():
    BASE_URL = "http://localhost:8090/api/locationsearch/search"

    response = requests.get(BASE_URL, params={'term':'Saturn'})

    # Check if the response is successful
    if response.status_code == 200:
        # Return the JSON data
        return response.json()
    else:
        # Return an error message
        return f"Error: {response.status_code}, {response.reason}"


# Example usage
# object_to_find = input("Enter the name of the astronomical object you want to find: ")
# data = find_object_in_stellarium(object_to_find)

#first, send it with -2, -2
#data = main_poll()
#print(data['actionChanges']['id'])
#print(data['propertyChanges']['id'])
connect = Establish.confirm_connection()
if(connect != 1):
    data = main_poll(data['actionChanges']['id'], data['propertyChanges']['id'])
pprint.pprint(connect)

#now ae wanna try to change some stuff.