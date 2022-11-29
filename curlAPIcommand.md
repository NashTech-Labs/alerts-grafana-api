## Create API tokens using REST POST method

1. create org
```bash
export Grafana_Server="13.126.211.230"

curl -X POST -H "Content-Type: application/json" -d '{"name":"DevOps1"}' http://admin:admin@$Grafana_Server:3000/api/orgs
```
2. If already have an org or step 3 fails then add ADmin user to org
```bash
curl -X POST -H "Content-Type: application/json" -d '{"loginOrEmail":"admin", "role": "Admin"}' http://admin:admin@$Grafana_Server:3000/api/orgs/<org id of new org>/users
```
* find id in api output of 
```bash
curl http://admin:admin@$Grafana_Server:3000/api/orgs/
```

on browser with access with the grafana server

3. switch tonew org
```bash
curl -X POST http://admin:admin@$Grafana_Server:3000/api/user/using/<id of new org>
```
4. create API Token
```bash
curl -X POST -H "Content-Type: application/json" -d '{"name":"apikeycurl", "role": "Admin"}' http://admin:admin@$Grafana_Server:3000/api/auth/keys
{"id":3,"name":"apikeycurl","key":"eyJrIjoiTlhsdmVGajR6S05hWTZpR3l1R2o5MVdMREtJMTNaVnMiLCJuIjoiYXBpa2V5Y3VybCIsImlkIjoyfQ=="}
```


## Alerts using API

1. see available alerts
```bash
curl -X POST -H "Content-Type: application/json Authorisation: Bearer eyJrIjoiTlhsdmVGajR6S05hWTZpR3l1R2o5MVdMREtJMTNaVnMiLCJuIjoiYXBpa2V5Y3VybCIsImlkIjoyfQ==" http://admin:admin@$Grafana_Server:3000/api/alerts
```

