import requests
import json
from orak import urls, environment

def get_cached_values(access_token, env):
    url = environment[env] + urls['cache']
    headers = {
        "content-type": "application/json"
    }
    headers['access-token'] = access_token

    try:
        response = requests.get(url)
        if response.ok:
            return json.loads(response.text)
        elif response.status_code == 401:
            return {'error': 'User is not authorized to access'}
        else:
            return {'error': 'Unable to call the service'}        
    except Exception:
        return {'error': 'Unable to call the service'}     

def load_cache(access_token, env):
    url = environment[env] + urls['loadcache']
    headers = {}
    headers['access-token'] = access_token

    try:
        response = requests.get(url)
        if response.ok:
            return 'Success'
        else:
            return 'Failed'    
    except Exception:
        return 'Unable to call the service'           
