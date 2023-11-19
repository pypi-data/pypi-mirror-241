import requests

def smtp_comm(api_key, url, ip, lang, product_id, license_code, client_name):
    smtp_url = f'{url}/api/activate_license'
    headers = {
        'LB-API-KEY': api_key,
        'LB-URL': url,
        'LB-IP': ip,
        'LB-LANG': lang,
        'Content-Type': 'application/json'
    }

    payload = {
        "verify_type": "non_envato",
        "product_id": product_id,
        "license_code": license_code,
        "client_name": client_name
    }

    response = requests.post(smtp_url, headers=headers, json=payload)
    return response.text

def verify_license(api_key, url, ip, lang, product_id, license_code, client_name):
    smtp_verify = f'{url}/api/verify_license'
    headers = {
        'LB-API-KEY': api_key,
        'LB-URL': url,
        'LB-IP': ip,
        'LB-LANG': lang,
        'Content-Type': 'application/json'
    }

    payload = {
        "product_id": product_id,
        "license_code": license_code,
        "client_name": client_name
    }

    response = requests.post(smtp_verify, headers=headers, json=payload)
    return response.text
