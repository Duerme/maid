import scapy.all as scapy
import socket
import config

def arp_request(ip_address):
    arp_packet = scapy.ARP(pdst=ip_address)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    full_packet = broadcast / arp_packet
    answered = scapy.srp(full_packet, timeout=1, iface=config.ntwrk_adapter, verbose=False)[0]
    
    for host in answered:
        print(host[1].psrc)
        print(host[1].hwsrc)
        print("--------------------------------------------------------------")

def device_info(host):
    try:
        hostname = socket.gethostbyaddr(host)[0]
        return hostname
    except socket.herror as e:
        print(f"Could not resolve the hostname for {host}. Error message: {e}")

arp_request(config.ip_subnet)
# hostname = device_info("10.0.0.32")

