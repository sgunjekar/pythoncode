
import json
import logging
import requests

policy_api = 'https://<server>/logs-service/api/v1.0/logs/policies'

logger = logging.getLogger('policy_util')
logging.basicConfig(level=logging.INFO)

def get_jwt_token():
    with open("jwt_token.txt", "r") as f:
        return f.read().strip()

def get_server_url(config):
    domain_url = config.get('domain_url', '<tenant_name>-private-dev.qa.sps.secops.bmc.com')
    tenant_name = config.get('tenant_name', 'aramco')
    return domain_url.replace('<tenant_name>', tenant_name)

def get_headers(jwt_token):
    return {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + jwt_token,
    }

def create_policy_api(payload, **config):
    print('-----------------------------------------------------------')
    print(payload)
    print('-----------------------------------------------------------')
    jwt_token = get_jwt_token()
    server = get_server_url(config)
    url = policy_api.replace('<server>', server)
    response = requests.post(url, data=json.dumps(payload), headers=get_headers(jwt_token))
    if response.status_code == 200:
        logger.info(f'✅ Policy "{payload.get("name")}" created successfully')
        return response.json().get('id')
    else:
        logger.error(f'❌ Failed to create policy: {response.status_code}')
        logger.error(response.text)

if __name__ == "__main__":
    config = {
        "tenant_name": "aramco",
        "domain_url": "aramco-private-dev.qa.sps.secops.bmc.com"
    }

    # Corrected payload structure based on your UI network response
    policy_payload = {
        "id": "",
        "name": "test11",
        "description": "",
        "execution_order": 9999,
        "enabled": False,
        "tenant_id": "454758490",
        "selection_criteria": "( name EQUALS 'test' )",
        "usergroups": [],
        "configurations": [
            {
                "name": "test11",
                "type": "COLLECTION",
                "configuration_details": [
                    {
                        "collection_type": "file",
                        "connector_type": "tdc-connector-linux",
                        "path": "/opt/bmc/apache_logs.log"
                    }
                ]


            }
        ]
    }


    create_policy_api(policy_payload, **config)
