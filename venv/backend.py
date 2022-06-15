#URL-infosystem V1.0
#this is the main back-end file, which collects data from ipapi.co and returns the selected values

import requests
import ipaddress

#gets the raw IP
def get_ip():
    response = ip_address
    return response["ip"]

#extracts the desired values from the API
def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "IP-version": response.get("version"),
        "city": response.get("city"),
        "postal code": response.get("postal"),
        "region": response.get("region"),
        "country": response.get("country_name"),
        "internet host": response.get("org")
    }
    return location_data

#prompt for input of IP or alternatively an automatic search for its own
typed_ip = input("Please enter an IP-Address or type 'own' to inspect your own: ")
if typed_ip == "own":
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
else:
    ip_address = dict()
    ip_address['ip'] = typed_ip

#calls the get_location() class and prints the results (value pairs)
print(get_location())

