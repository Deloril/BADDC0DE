#/bin/bash/python3

from scapy.all import *
from scapy import *
from scapy.utils import rdpcap
from scapy.utils import wrpcap

packets = rdpcap("./baddcode-csirtFlag.pcapng")

for pkt in packets:
    if pkt[TCP].dport == 12345:
        pkt[IP].dst = "122.56.32.4"
        pkt[IP].src = "10.5.50.214"
        pkt[0].src = '3c:22:fb:94:02:9e' # pretty sure this changes the ethernet address
        pkt[0].dst = 'e4:8d:8c:2b:2:ab' # pretty sure this changes the ethernet address
    else:
        pkt[IP].dst = "122.56.32.4"
        pkt[IP].src = "10.5.50.214"
        pkt[0].dst = '3c:22:fb:94:02:9e' # pretty sure this changes the ethernet address
        pkt[0].src = 'e4:8d:8c:2b:2:ab' # pretty sure this changes the ethernet address
    #del pkt[IP].chksum
    del(pkt.chksum)
    #del pkt[TCP].chksum
    #del pkt[0].dst
    #del pkt[0].src

wrpcap("./baddcode-CSIRT-ipFix.pcap", packets)
wireshark("./baddcode-CSIRT-ipFix.pcap", packets)