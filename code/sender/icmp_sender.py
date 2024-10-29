from scapy.all import *

DESTINATION = "receiver"
icmp_packet = IP(dst=DESTINATION, ttl=1) / ICMP()
print("Sending ICMP packet with TTL=1 to", DESTINATION)
send(icmp_packet)