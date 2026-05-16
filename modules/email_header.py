import re

def analyze_header(raw_header):
    # Split the header into lines
    lines = raw_header.split("\n")
    email_info = {}

    # Extract relevant information from each line
    for line in lines:
        if line.startswith("From:"):
            email_info["from"] = line[6:].strip()
        elif line.startswith("To:"):
            email_info["to"] = line[4:].strip()
        elif line.startswith("Subject:"):
            email_info["subject"] = line[9:].strip()
        elif line.startswith("Date:"):
            email_info["date"] = line[6:].strip()
        elif line.startswith("X-Originating-IP:"):
            email_info["source_ip"] = line[18:].strip()
        elif line.startswith("Received:"):
            # IP nikalo Received field se
            ip_match = re.search(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', line)
            if ip_match and "source_ip" not in email_info:
                email_info["source_ip"] = ip_match.group()
        

    return email_info
