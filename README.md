# 🕵️ OSINT Aggregator

![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-MacOS%20%7C%20Linux-lightgrey?style=for-the-badge)

> **A powerful OSINT tool built in Python — aggregates public intelligence from multiple sources into unified reports. Similar to tools used by RAW, IB, and CERT-In analysts.**

---

## ⚡ Features

| Module | Description |
|--------|-------------|
| 👤 **Username Recon** | Search across GitHub, Reddit, Telegram, Medium |
| 📧 **Email Recon** | Validate email + fetch MX records |
| 📨 **Email Header Analysis** | Extract source IP, trace routing path |
| 📍 **IP Intelligence** | Geolocate IP, fetch ISP + timezone |
| 🌐 **Domain Recon** | WHOIS + DNS (A, MX, NS) records |
| 📱 **Phone Recon** | Carrier, location, validity check |
| 🔗 **Auto IP Chaining** | Auto traces source IP from email headers |
| 📄 **Report Generator** | Formatted intelligence reports |

---

## 🛠️ Tech Stack

![httpx](https://img.shields.io/badge/httpx-HTTP%20Requests-orange?style=flat-square)
![dnspython](https://img.shields.io/badge/dnspython-DNS%20Lookups-blue?style=flat-square)
![python-whois](https://img.shields.io/badge/python--whois-WHOIS%20Queries-purple?style=flat-square)
![rich](https://img.shields.io/badge/rich-Terminal%20UI-red?style=flat-square)

---

## 📁 Project Structure

```
osint-aggregator/
├── 📄 main.py
├── 📁 modules/
│   ├── 👤 username.py
│   ├── 📧 email_recon.py
│   ├── 📨 email_header.py
│   ├── 📍 ip_intel.py
│   ├── 🌐 domain_recon.py
│   ├── 📱 phone_recon.py
│   └── 📄 report.py
├── 📁 config/
│   └── 🔑 api_keys.py
└── 📖 README.md
```

---

## ⚙️ Setup & Installation

**1. Clone the repo**
```bash
git clone https://github.com/prerak-369/osint-aggregator.git
cd osint-aggregator
```

**2. Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install httpx dnspython python-whois rich pyfiglet colorama
```

**4. Add API keys in `config/api_keys.py`**
```python
IPINFO_TOKEN = "your_ipinfo_token"
NUMVERIFY_API_KEY = "your_numverify_key"
```

**5. Run**
```bash
python main.py
```

---

## 🎯 Real World Use Cases

🔍 Cybersecurity Investigations
📊 Digital Footprint Analysis
🕵️ Email Header Forensics
🌐 Network Reconnaissance
⚠️  Threat Intelligence Gathering

---

## ⚠️ Disclaimer

> This tool is for **educational and ethical use only**.  
> Always obtain proper authorization before investigating any target.  
> The developer is not responsible for any misuse.

---

## 👨‍💻 Author

**Prerak Patel**  
BCA Student | Cybersecurity Enthusiast  

[![GitHub](https://img.shields.io/badge/GitHub-prerak--369-black?style=flat-square&logo=github)](https://github.com/prerak-369)