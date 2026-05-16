import httpx
from config.api_keys import IPINFO_TOKEN

def check_ip(ip):
    response = httpx.get(f"https://ipinfo.io/{ip}?token={IPINFO_TOKEN}")
    data = response.json()
    
    result = {
        "ip": ip,
        "city": data.get("city", "N/A"),
        "region": data.get("region", "N/A"),
        "country": data.get("country", "N/A"),
        "org": data.get("org", "N/A"),
        "timezone": data.get("timezone", "N/A"),
        "hostname": data.get("hostname", "N/A")
    }
    return result