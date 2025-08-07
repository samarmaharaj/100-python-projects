import subprocess

def wifi_scan():
    result = subprocess.run(['netsh', 'wlan', 'show', 'networks', 'mode=Bssid'], capture_output=True, text=True)
    networks = result.stdout.split('\n')

    for line in networks:
        if 'SSID' in line:
            ssid = line.split(': ')[1]
        if 'BSSID' in line:
            bssid = line.split(': ')[1]
            print(f"SSID: {ssid}, BSSID: {bssid}")

# Example usage
wifi_scan()
