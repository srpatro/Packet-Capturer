from time import sleep

from scapy.all import *
from scapy.layers.inet import IP, ICMP

import packets
lock = threading.Lock()
def send_packet(ips):
    while True:
        with lock:
            for ip in ips:
                send(IP(src=ip, dst=ip) / ICMP() / "Hello World")
            sleep(.5)


def get_current_network_ip(pkt):
    if IP in pkt:
        ip_src = pkt[IP].src
        ip_dst = pkt[IP].dst
    #if TCP in pkt:
     #   tcp_sport = pkt[TCP].sport
      #  tcp_dport = pkt[TCP].dport

        #print(" IP src " + str(ip_src) + " TCP sport " + str(tcp_sport))
        return str(ip_src)
        # you can filter with something like that
    if ((pkt[IP].src == "192.168.0.1") or (pkt[IP].dst == "192.168.0.1")):
        print("!")
