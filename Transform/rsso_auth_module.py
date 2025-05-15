
import json
import time
import requests

admin_api = 'https://<server>:443/admin'
rsso_api = 'https://<server>:443/rsso/start'
consent_decision_api = 'https://<server>:443/rsso/oauth2/consent-decision'
ims_jwt_token = 'https://<server>:443/ims/api/v1/auth/rsso/tokens'
oauth_callback = 'https://<server>:443/imsportal/oauth/callback'

jwt_token = None

def refresh_jwt_token(**config):
    domain_url = config.get('domain_url', '<tenant_name>-private-dev.qa.sps.secops.bmc.com')
    tenant_name = config.get('tenant_name', 'hp')
    server = domain_url.replace('<tenant_name>', tenant_name)
    for i in range(0, 6):
        try:
            client_details = _get_rsso_values(server)
            saml_token = _get_saml_token(server, **config)
            consent_details = _get_rsso_consent_decision(server, client_details, saml_token)
            auth = _get_rsso_oidc_token(server, consent_details)
            jwt = _get_ims_jwt_token(server, auth, **config)
            return jwt
        except Exception as e:
            if i < 5:
                time.sleep(1)
                continue
            else:
                raise Exception("Login failed for tenant %s." % tenant_name) from e

def _get_rsso_values(server):
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.get(admin_api.replace('<server>', server), headers=headers)
    if response.status_code == 200:
        response = response.text.split('\n')
        data = [i.strip().replace('amp', '').replace('"/>', '') for i in response if 'name="goto"' in i][0].split("?")[1]
        params = {x[0]: x[1] for x in [x.split("=") for x in data.split("&;")]}
        return params
    else:
        raise Exception("Failed to get RSSO values.")


def _get_saml_token(server, **config):
    tenant = config.get('tenant_name', 'hp') + '.' + str(config.get('tenant_id', '529553743'))
    payload = {
        "tenant": server + "@" + tenant,
        "user-name": config.get('tenant_user', 'admin'),
        "password": config.get('tenant_password', 'password'),
        "goto": "https://" + server,
        "url_hash_handler": "true"
    }
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(rsso_api.replace('<server>', server), headers=headers, data=payload)

    if response.status_code == 200:
        response_cookies = response.cookies.get_dict()
        for k, v in response_cookies.items():
            print(f"[DEBUG] Cookie found: {k}={v}")
            if k == "helix_jwt_token":
                return {"helix_jwt_token": v}

    raise Exception("Failed to get SAML token.")

def _get_rsso_consent_decision(server, params, headers):
    url = f"{consent_decision_api.replace('<server>', server)}?client_id={params.get('client_id')}&state={params.get('state')}&redirect_key={params.get('redirect_key')}&scope=openid"
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 302:
        data = response.headers.get('Location').split("?")[1]
        return {x[0]: x[1] for x in [x.split("=") for x in data.split("&")]}
    raise Exception("Failed to get consent decision.")

def _get_rsso_oidc_token(server, params):
    headers = {'content-type': 'application/json'}
    response = requests.get(oauth_callback.replace('<server>', server), headers=headers, params=params, allow_redirects=False)
    if response.status_code == 302:
        rsso_oidc = response.cookies.get_dict()
        return [v for k, v in rsso_oidc.items() if 'RSSO_OIDC' in k][0]
    raise Exception("Failed to get OIDC token.")

def _get_ims_jwt_token(server, rsso_oidc, **config):
    global jwt_token
    headers = {'content-type': 'application/json'}
    tenant = config.get('tenant_name', 'hp') + '.' + str(config.get('tenant_id', '529553743'))
    payload = {"rsso_token": rsso_oidc, "rsso_tenant_id": tenant}
    response = requests.post(ims_jwt_token.replace('<server>', server), headers=headers, json=payload)
    if response.status_code == 200:
        jwt_token = response.json().get('json_web_token')
        return jwt_token
    raise Exception("Failed to get JWT token.")

def get_jwt_token(**config):
    global jwt_token
    if jwt_token is None:
        return refresh_jwt_token(**config)
    return jwt_token

def set_jwt_token(token):
    global jwt_token
    jwt_token = token
