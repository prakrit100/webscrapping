import requests
import json

url = 'https://www.nepsealpha.com/trading/1/search'

headers = {
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'Referer': 'https://www.nepsealpha.com/trading/chart',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

params = {
    'limit': '500',
    'query': '',
    'type': '',
    'exchange': '',
}

response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    data = response.json()
    filtered_data = [{"name": item.get("name", ""), "description": item.get("description", ""), "exchange": item.get("exchange", "")} for item in data]
    
    with open('filtered_nepse.json', 'w') as f:
        json.dump(filtered_data, f)
else:
    print(f"Failed to fetch data: {response.status_code}")
    
