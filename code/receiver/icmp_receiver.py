from scapy.all import *

# Callback function that will run whenever a packet is received
def packet_callback(packet):
    # Check if the packet is ICMP and is a request packet
    if packet.haslayer(ICMP) and packet[IP].ttl == 1:
        print("Received ICMP Request packet:")
        # Display packet details
        packet.show()

print("Listening for incoming ICMP packets with TTL=1...")
# Wait for incoming packets
# sniff(filter="icmp", prn=packet_callback, store=0)