print('This is our main test file')

import requests
import ipaddress

def get_ip():
    response = ip_address
    return response["ip"]



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

#test ip_address = {'ip': '2001:4860:4860::8888'}

typed_ip = input("Please enter an IP-Address or type 'own' to inspect your own: ")
if typed_ip == "own":
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
else:
    ip_address = dict()
    ip_address['ip'] = typed_ip

print(get_location())

