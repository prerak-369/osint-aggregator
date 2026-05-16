from modules.username import check_username
from modules.ip_intel import check_ip
from modules.email_recon import check_email
from modules.email_header import analyze_header
import sys
from modules.domain_recon import check_domain
from modules.phone_recon import check_phone
from modules.report import generate_report

print("Hello...")

#asking user
print("What do you want to search?\n- 1. Username\n- 2. Email\n- 3. Phone\n- 4. IP\n- 5. Domain")

try:
    search_choice = int(input("Enter the number of your choice: "))
except ValueError:
    print("Invalid input! Please enter a number...")
    search_choice = -1  # default invalid value


if(search_choice == 1):
    print("You chose to search by Username.")
    user_name = input("Enter the username to search: ")
    print(f"Searching for username: {user_name}")
    results = check_username(user_name)
    data = {}
    for platform, found, url in results:
        if found:
            print(f"[+] Found on {platform}: {url}")
            data[platform] = url
        else:
            print(f"[-] Not found on {platform}")
            data[platform] = "Not Found"
    print(generate_report(user_name, data))

elif(search_choice == 2):
    user_email = input("Enter the email to search: ")
    result = check_email(user_email)
    print(f"Email: {result['email']}")
    print(f"Domain: {result['domain']}")
    print(f"Valid: {result['valid']}")
    print(f"MX Records: {result['mx_records']}")
    print(generate_report(user_email, result))  # ← ADD
    
    print("\nDo you have a raw email header to analyze? (y/n): ", end="")
    choice = input()
    if choice == "y":
        print("Paste your raw header below and type 'END' on a new line when done:")
        lines = []
        while True:
            try:
                line = input()
            except EOFError:
                break
            if line.strip() == "END":
                break
            lines.append(line)
        raw_header = "\n".join(lines)
        header_info = analyze_header(raw_header)
        for key, value in header_info.items():
            print(f"{key}: {value}")
        if "source_ip" in header_info:
            print("\n[*] Checking source IP location...")
            ip_result = check_ip(header_info["source_ip"])
            for key, value in ip_result.items():
                print(f"{key}: {value}")
            print(generate_report(header_info["source_ip"], ip_result)) 

elif(search_choice == 3):
    user_phone = input("Enter the phone number to search: ")
    result = check_phone(user_phone)
    for key, value in result.items():
        print(f"{key}: {value}")
    print(generate_report(user_phone, result))

elif(search_choice == 4):
    user_ip = input("Enter the IP address to search: ")
    result = check_ip(user_ip)
    for key, value in result.items():
        print(f"{key}: {value}")
    print(generate_report(user_ip, result))

elif(search_choice == 5):
    print("You chose to search by Domain.")
    user_domain = input("Enter the domain to search: ")
    print(f"Searching for domain: {user_domain}")
    domain_info = check_domain(user_domain)
    for key, value in domain_info.items():
        print(f"{key}: {value}")
    print(generate_report(user_domain, domain_info))  
else:
    print("Invalid choice.")