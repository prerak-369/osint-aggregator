# 🕵️ OSINT Aggregator

A powerful Open Source Intelligence (OSINT) tool built in Python that aggregates public information from multiple sources into a unified intelligence report.

## 🔍 Features

- **Username Recon** — Search username across multiple platforms (GitHub, Reddit, Telegram, Medium)
- **Email Recon** — Validate email, fetch MX records, analyze raw email headers
- **Phone Recon** — Get carrier, location, and validity of phone numbers
- **IP Intelligence** — Geolocate IPs, fetch ISP and timezone info
- **Domain Recon** — WHOIS lookup, DNS records (A, MX, NS)
- **Email Header Analysis** — Extract source IP, trace email routing path
- **Auto IP Chaining** — Automatically traces source IP from email headers
- **OSINT Report Generator** — Generates formatted intelligence reports

## 🛠️ Tech Stack

- Python 3.14
- httpx — HTTP requests
- dnspython — DNS lookups
- python-whois — WHOIS queries
- rich — Terminal formatting
- pyfiglet — ASCII banners

## 📁 Project Structure

osint-aggregator/
├── main.py
├── modules/
│   ├── username.py
│   ├── email_recon.py
│   ├── email_header.py
│   ├── ip_intel.py
│   ├── domain_recon.py
│   ├── phone_recon.py
│   └── report.py
├── config/
│   └── api_keys.py  (not included - see setup)
└── README.md

## ⚙️ Setup

1. Clone the repo
```bash
git clone https://github.com/prerak-369/osint-aggregator.git
cd osint-aggregator
```

2. Install dependencies
```bash
pip install httpx dnspython python-whois rich pyfiglet colorama
```

3. Add API keys in `config/api_keys.py`
```python
IPINFO_TOKEN = "your_ipinfo_token"
NUMVERIFY_API_KEY = "your_numverify_key"
```

4. Run
```bash
python main.py
```

## 🎯 Use Cases

- Cybersecurity investigations
- Digital footprint analysis
- Email header forensics
- Network reconnaissance
- Threat intelligence gathering

## ⚠️ Disclaimer

This tool is for educational and ethical use only. Always obtain proper authorization before investigating any target.

## 👨‍💻 Author

**Prerak Patel** — BCA Student | Cybersecurity Enthusiast