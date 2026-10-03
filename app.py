import json
import time
import requests

# 1. Configuration
# Note: Your Splunk Cloud trial URL will usually require port 8088 or 443 for HEC data
SPLUNK_URL = "https://YOUR_SPLUNK_CLOUD_URL:8088/services/collector/event" #Change to your real splunk URL
HEC_TOKEN =  "YOUR HEC TOKEN"  #( "PASTE_YOUR_HEC_TOKEN_HERE" )

headers = {
    "Authorization": f"Splunk {HEC_TOKEN}",
    "Content-Type": "application/json"
}

# 2. Simulate a log entry (Imagine your custom tool generated this)
log_payload = {
    "time": time.time(),                # Current epoch timestamp
    "host": "kellys-desktop",      # Where the log came from ( Make sure this is a valid hostname or OS)
    "source": "my_custom_python_tool", # Script name ( You can change this to your actual script name )
    "sourcetype": "_json",              # Telling Splunk to parse it cleanly as JSON
    "event": {                          # The actual log body
        "status": "MALICIOUS_IP_DETECTED",
        "attacker_ip": "185.220.101.5",
        "threat_score": 98,
        "country": "Unknown", #(If you prefer, you can an a real country or use a python script to figure the exact country type)
        "action_taken": "Blocked via iptables firewall"
    }
}

print("[*] Blasting log data directly over the network to Splunk...")

# 3. Send the HTTP POST request (We turn off SSL verification for simple cloud trials)
try:
    response = requests.post(SPLUNK_URL, data=json.dumps(log_payload), headers=headers, verify=False)
    
    if response.status_code == 200:
        print("[+] Success! Splunk accepted the log data natively.")
        print(f"Splunk Response: {response.text}")
    else:
        print(f"[-] Failed to send. Status Code: {response.status_code}")
        print(f"Error Details: {response.text}")
        
except Exception as e:
    print(f"[-] Connection Error: {e}")

print("=======================================================")

print("\n[*] Finished processing results. Exiting script.")

print("================= Happy Splunking! ====================")


