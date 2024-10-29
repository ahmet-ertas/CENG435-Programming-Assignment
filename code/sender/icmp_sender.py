from scapy.all import *

# Specify destination hostname
DESTINATION = "receiver"
# Create the ICMP packet with TTL=1
icmp_packet = IP(dst=DESTINATION, ttl=1) / ICMP()

print("Sending ICMP packet with TTL=1 to", DESTINATION)
# Send the ICMP packet
send(icmp_packet)