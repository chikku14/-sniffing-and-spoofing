#!/usr/bin/env python3
from scapy.all import IP, ICMP, send

packet = IP(dst="8.8.8.8") / ICMP()

send(packet, count=4)
print("Spoofed packets sent.")



