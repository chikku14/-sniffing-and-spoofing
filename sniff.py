#!/usr/bin/env python3
from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

sniff(prn=packet_callback, store=0, count=20)


requirements.txt
scapy
