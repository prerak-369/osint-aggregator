import httpx
import dns.resolver

def check_email(email):
    domain = email.split("@")[-1]
    result = {
        "email": email,
        "domain": domain,
        "mx_records": [],
        "valid": False
    }
    try:
        mx_records = dns.resolver.resolve(domain, "MX")
        result["valid"] = True
        for mx in mx_records:
            result["mx_records"].append(str(mx.exchange))
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        result["valid"] = False
    
    return result