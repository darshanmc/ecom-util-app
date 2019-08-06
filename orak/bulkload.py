import requests
import json
from orak import bulk_service, environment, b2b_environment, b2b_urls

def bulk_load(schema, env, body, access_token):
    schema = bulk_service[schema]
    url = environment[env] + schema

    if body:
        ids = body.split(',')
        payload = json.dumps(ids)
    else:
        payload = []
                

    headers = {
        "content-type": "application/json"
    }

    headers['access-token'] = access_token

    response = requests.post(url=url, data=payload, headers=headers)

    if response.ok:
        resp = json.loads(response.content)
        if (resp):
            message = f"Records requested for upload {resp['totalNumberOfRecords']}. Records uploaded {resp['createdRecords']}"
            return message, 'success'
    elif response.status_code == 403:
        resp = json.loads(response.content)
        error_code = resp['errorCodes'][0]['errorCode']
        return error_code, 'danger'

def b2b_bulk_load(schema, env):
    url = b2b_environment[env] + b2b_urls[schema]

    headers = {
        "content-type": "application/json"
    }

    response = requests.get(url=url, headers=headers)

    if response.ok:
        return 'Records uploaded successfully', 'success'
    else:
        return 'Bulk upload failed', 'danger'    