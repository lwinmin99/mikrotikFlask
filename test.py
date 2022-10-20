import requests

url = "https://192.168.113.111/rest/ip/address"
header = {
    "Authorization": 'Basic bHdpbm1pbmtvOmx3aW5taW5rbzEyMw==',
}

payload = { "address" : "192.168.111.180", "interface": "dummy"}
response = requests.put(url, headers=header, json = payload , verify=False)
datas= response.json()
print(datas)