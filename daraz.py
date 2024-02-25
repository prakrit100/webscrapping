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

response = requests.get(
    'https://acs-m.daraz.com.np/h5/mtop.daraz.ald.channels.service/1.0/',
    params=params,
    cookies=cookies,
    headers=headers,
)

if response.status_code == 200:
    with open('daraz_response.json', 'w') as f:
        json.dump(response.json(), f)
    print("Data saved to daraz_response.json")
else:
    print(f"Failed to fetch data: {response.status_code}")
