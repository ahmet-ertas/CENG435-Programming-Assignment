from scapy.all import *

# Implement your ICMP receiver here
def packet_callback(packet):
    if packet.haslayer(ICMP) and packet[IP].ttl == 1:
        print("Received ICMP Request packet:")
        packet.show()

# Start sniffing for ICMP packets
print("Listening for incoming ICMP packets with TTL=1...")
sniff(filter="icmp", prn=packet_callback, store=0)