import requests
import json

grafana_url = "a5c07bf2eeabc479f99071aaddbac98b-364804466.ap-south-1.elb.amazonaws.com"
username = "admin"
password = "prom-operator"

base_url = "http://{}:{}@{}".format(username, password, grafana_url)

headers = {
    'Authorization': 'Bearer eyJrIjoiMlViUENzNzZUZjVLUnpISjlMb3hrT2NaMXVUbGoxbzQiLCJuIjoiQWRtaW4iLCJpZCI6MX0=',
    'Content-Type': 'application/json',
}
json_data = {
    'Condition':'A', #condition
    'Title': 'Checking alert', #title
    'Data':[
        {
            'RefID': 'A',
            'QueryType': '',
            'relativeTimeRange': {
                'from': 600,
                'to': 0
            },
            'DatasourceUID': 'prometheus',
            'model': {
                'editorMode': 'builder',
                'expr': 'node_load1 < 1.5',
                'hide': False,
                'intervalMs': 1000,
                'legendFormat': '__auto',
                'maxDataPoints': 43200,
                'range': True,
                'RefID': 'A'
            }
        },
        {
            'RefID': 'B',
            'QueryType': '',
            'relativeTimeRange': {
                'from': 60,
                'to': 0
            },
            'DatasourceUID': 'prometheus',
            'model': {
                'conditions': [
                    {
                        'evaluator': {
                            'params': [
                                0,
                                0
                            ],
                            'type': 'gt'
                        },
                        'operator': {
                            'type': 'and'
                        },
                        'query': {
                            'params': [
                                'A'
                            ]
                        },
                        'reducer': {
                            'params': [],
                            'type': 'avg'
                        },
                        'type': 'query'
                    }
                ],
                'datasource': {
                    'name': 'Expression',
                    'type': 'prometheus',
                    'uid': 'prometheus'
                },
                'expression': 'A',
                'hide': False,
                'intervalMs': 1000,
                'maxDataPoints': 43200,
                'RefID': 'B',
                'type': 'classic_conditions'
            }
        }
    ],
    'ExecErrState': 'Error', #exec_err_state
    'FolderUID': 'QG5iHMK4k', #namespace_uid,
    'Labels': {
        "severity": "warning"
    }, #labels
    'NoDataState': 'NoData', #no_data_state
    'OrgID': 1, #orgId
    'RuleGroup': 'Instances', #rule_group
    'for': '1m' #for
}

resp = requests.post(
    base_url + "/api/v1/provisioning/alert-rules", headers=headers, json=json_data)
print(json.dumps(resp.json(), indent=4))
