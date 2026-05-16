import whois
import dns.resolver

def check_domain(domain):
    domain_info = {}

    # WHOIS lookup
    try:
        whois_info = whois.whois(domain)
        domain_info["domain"] = whois_info.domain
        domain_info["registrar"] = whois_info.registrar
        domain_info["creation_date"] = whois_info.creation_date
        domain_info["expiration_date"] = whois_info.expiration_date
    except Exception as e:
        print(f"Error fetching WHOIS info: {e}")

    # DNS A records
    try:
        dns_records = dns.resolver.resolve(domain, "A")
        domain_info["ip_addresses"] = [ip.address for ip in dns_records]
    except Exception as e:
        print(f"Error fetching DNS records: {e}")

    # MX records
    try:
        mx_records = dns.resolver.resolve(domain, "MX")
        domain_info["mx_records"] = [str(mx.exchange) for mx in mx_records]
    except Exception:
        domain_info["mx_records"] = []

    # NS records
    try:
        ns_records = dns.resolver.resolve(domain, "NS")
        domain_info["ns_records"] = [str(ns) for ns in ns_records]
    except Exception:
        domain_info["ns_records"] = []

    return domain_info