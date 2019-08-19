import requests
import json
from orak import login_service, urls, services, environment

def login_call(username, password, env):

    url = login_service[env]
   
    body = {}
    body['userName'] = username
    body['password'] = password

    payload = json.dumps(body)

    headers = {
        "content-type": "application/json"
    }

    try:
        response = requests.post(url, data=payload, headers=headers)
        if response.ok:
            participant_model = json.loads(response.text)
            if participant_model:
                access_token = participant_model['accessToken']
                metadata_url = environment[env] + urls['metadata']
                headers['access-token'] = access_token

                metadata_response = requests.get(metadata_url, headers=headers)
                if response.ok:
                    metadata_model = json.loads(metadata_response.text)
                    role_list = metadata_model['roles']

                    is_authorized = False

                    for role in role_list:
                        if role == 'Site Administrator':
                            is_authorized = True
                            full_name = metadata_model['firstName']

                    if is_authorized:
                        return access_token, env, True, full_name
                    else:
                        return 'You are not authorized to access!', env, False        

        elif response.status_code == 403:
            resp = json.loads(response.text)
            return resp['errorCodes'][0]['errorCode'], env, False
    except Exception:
        return f'Unable to connect to {env} environment', env, False

