import requests

# Step 1: Fetching data from OTX
def fetch_threat_intelligence():
    url = 'https://otx.alienvault.com/api/v1/pulses/subscribed'
    headers = {
        'X-OTX-API-KEY': 'YOUR_API_KEY_HERE'  # Replace with your actual OTX API key
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"[!] Error: Received status code {response.status_code}")
            return None
    except Exception as e:
        print(f"[!] Exception occurred: {e}")
        return None

# Step 2–4: Analyze, contextualize, and export prioritized threat data
def parse_threat_intelligence(data):
    if not data or 'results' not in data:
        print("[!] Invalid or empty data received.")
        return

    prioritized_output = []
    high_priority_tags = ['ransomware', 'phishing']

    for pulse in data['results']:
        pulse_name = pulse.get('name', 'Unnamed Pulse')
        pulse_tags = pulse.get('tags', [])
        indicators = pulse.get('indicators', [])

        # Determine priority
        priority = 'HIGH' if any(tag.lower() in high_priority_tags for tag in pulse_tags) else 'LOW'

        # Format pulse info
        entry = f"Pulse: {pulse_name}\n"
        entry += f"Tags: {', '.join(pulse_tags)}\n"
        entry += f"Priority: {priority}\n"
        entry += "Indicators:\n"
        for indicator in indicators:
            ioc = indicator.get('indicator', 'N/A')
            ioc_type = indicator.get('type', 'N/A')
            entry += f"  - {ioc} ({ioc_type})\n"
        entry += "-" * 60 + "\n"

        print(entry)  # Display on screen
        prioritized_output.append(entry)

    # Step 4: Write output to file
    try:
        with open("otx_intelligence_report.txt", "w") as report:
            report.writelines(prioritized_output)
        print("[+] Report saved to otx_intelligence_report.txt")
    except Exception as e:
        print(f"[!] Failed to write report: {e}")

# Entry point
if __name__ == "__main__":
    print("[*] Starting CTI collection from OTX...")
    threat_data = fetch_threat_intelligence()
    parse_threat_intelligence(threat_data)



