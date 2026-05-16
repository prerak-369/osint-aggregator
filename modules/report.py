from datetime import datetime

def generate_report(target, data):
    print("\n\n")
    report = ""
    report += "━" * 40 + "\n"
    report += "   OSINT INTELLIGENCE REPORT\n"
    report += "━" * 40 + "\n"
    report += f"Target   : {target}\n"
    report += f"Date     : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    report += "━" * 40 + "\n"
    report += "FINDINGS:\n\n"
    for key, value in data.items():
        report += f"  {key.upper():<20}: {value}\n"
    report += "\n" + "━" * 40 + "\n"
    return report