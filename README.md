# BADDC0DE

luke.pearson@lukepearso-ltm BADDEC0DE % python3 scapyFix.py
WARNING: No IPv4 address found on en5 !
WARNING: No IPv4 address found on ap1 !
WARNING: more No IPv4 address found on awdl0 !
Traceback (most recent call last):
  File "/usr/local/lib/python3.10/site-packages/scapy/fields.py", line 758, in h2i
    inet_aton(x)
OSError: illegal IP address string passed to inet_aton

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/luke.pearson/Library/CloudStorage/OneDrive-Personal/BADDEC0DE/scapyFix.py", line 14, in <module>
    pkt[0].src = '3c:22:fb:94:02:9e' # pretty sure this changes the ethernet address
  File "/usr/local/lib/python3.10/site-packages/scapy/packet.py", line 463, in __setattr__
    return self.setfieldval(attr, val)
  File "/usr/local/lib/python3.10/site-packages/scapy/packet.py", line 454, in setfieldval
    self.payload.setfieldval(attr, val)
  File "/usr/local/lib/python3.10/site-packages/scapy/packet.py", line 445, in setfieldval
    self.fields[attr] = any2i(self, val)
  File "/usr/local/lib/python3.10/site-packages/scapy/fields.py", line 793, in any2i
    return self.h2i(pkt, x)
  File "/usr/local/lib/python3.10/site-packages/scapy/fields.py", line 760, in h2i
    return Net(x)
  File "/usr/local/lib/python3.10/site-packages/scapy/base_classes.py", line 162, in __init__
    self.start = self.ip2int(net) >> inv_mask << inv_mask
  File "/usr/local/lib/python3.10/site-packages/scapy/base_classes.py", line 140, in ip2int
    "!I", socket.inet_aton(cls.name2addr(addr))
  File "/usr/local/lib/python3.10/site-packages/scapy/base_classes.py", line 127, in name2addr
    socket.getaddrinfo(name, None, cls.family)
  File "/usr/local/Cellar/python@3.10/3.10.2/Frameworks/Python.framework/Versions/3.10/lib/python3.10/socket.py", line 955, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno 8] nodename nor servname provided, or not known
