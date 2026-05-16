import httpx
from config.api_keys import NUMVERIFY_API_KEY

def check_phone(phone):
    response = httpx.get(f"http://apilayer.net/api/validate?access_key={NUMVERIFY_API_KEY}&number={phone}")
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to retrieve phone information"}
