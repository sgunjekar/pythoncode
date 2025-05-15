from rsso_auth_module import get_jwt_token

config = {
    "domain_url": "aramco-private-dev.qa.sps.secops.bmc.com",
    "tenant_name": "aramco",
    "tenant_id": "454758490",
    "tenant_user": "hannah_admin",
    "tenant_password": "Password_1234"
}

token = get_jwt_token(**config)
print("JWT Token:", token)
