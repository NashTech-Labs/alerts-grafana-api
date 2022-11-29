import requests
import json

grafana_url = "a063ada84b4724b2b9cd2aca57cde5d7-1236935921.ap-south-1.elb.amazonaws.com"
username = "admin"
password = "prom-operator"

base_url = "http://{}:{}@{}".format(username, password, grafana_url)

headers = {
    'Authorization': 'Bearer eyJrIjoiN0xNM1V4UWpMUkVoZXRKaWh2bVJya3IzZGNqb0dvTGkiLCJuIjoiQWRtaW4iLCJpZCI6MX0=',
    'Content-Type': 'application/json',
}

# resp = requests.get('http://admin:admin@13.126.211.230:3000/api/admin/stats')
resp = requests.get(base_url + "/api/ruler/grafana/api/v1/rules",headers=headers)
print(json.dumps(resp.json(), indent=4))

