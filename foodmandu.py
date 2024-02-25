import requests
import json

cookies = {
    # your cookies here
}

headers = {
    # your headers here
}

params = {
    # your params here
}

response = requests.get('https://foodmandu.com/webapi/api/Vendor/GetVendors1', params=params, cookies=cookies, headers=headers)

if response.status_code == 200:
    with open('foodmandu_response.json', 'w') as f:
        json.dump(response.json(), f)
    print("Data saved to foodmandu_response.json")
else:
    print(f"Failed to fetch data: {response.status_code}")
