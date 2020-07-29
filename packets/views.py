import json
# import subprocess

# import pcapy
from time import sleep

from django.http import HttpResponse
from django.shortcuts import render
from scapy.all import *
from scapy.layers.dns import DNS
from scapy.layers.inet import ICMP, IP

ping_ips = dict()
lock = threading.Lock()


def send_packet(ips):
    global ping_ips
    while True:
        with lock:
            ip = random.choice(ips)
            if ip in ping_ips:
                ping_ips[ip] += 1
            else:
                ping_ips[ip] = 1
            send(IP(src=ip, dst=ip) / ICMP() / "Hello World")
            print(ping_ips)
            sleep(.5)


def packets(request):
    global ping_ips
    print(ping_ips)
    p = list()
    ping_ips = dict()

    # address = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))  # To generate Randoem IP
    ips = ['252.45.106.224', '129.166.26.198', '150.16.129.19', '176.141.166.86', '234.128.200.180', '105.32.221.253',
           '118.11.65.104', '56.163.73.202', '10.133.173.102', '143.48.168.137', '89.187.221.139', '210.12.159.176',
           '185.54.50.252', '64.231.93.109', '114.69.255.35', '153.27.66.81', '10.195.106.78', '229.57.222.53',
           '37.205.40.139', '113.187.145.121', '119.203.219.71']
    t = threading.Thread(target=send_packet, args=(ips,))
    t.start()
    #Scapy network capturer Code
    # if random_ip == sniff(filter="host 37.205.40.139", prn=get_current_network_ip, count=2):
    #    # or it possible to filter with filter parameter...!
    #    #sniff(filter="ip and host 192.168.0.1", prn=print_summary)
    #   return HttpResponse(json.dumps(p), content_type="application/json")
    # p.clear()
    return render(request, 'packet_sniffer_logger.html', context={'ips': ips})


def getGlobalVariable(request):
    if request.GET['ip'] in ping_ips:
        value = ping_ips[request.GET['ip']]
    else:
        value = 0
    return HttpResponse(json.dumps(value), content_type="application/json")
