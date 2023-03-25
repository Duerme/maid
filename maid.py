import scapy.all as scapy
import socket

def arp_request(ip_address):
    arp_packet = scapy.ARP(pdst=ip_address)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    full_packet = broadcast / arp_packet
    answered, unanswered = scapy.srp(full_packet, timeout=1, iface="Wi-Fi", verbose=False)
    return answered.summary()

def device_info(host):
    hostname = socket.gethostbyaddr(host)[0]
    return hostname

arp_request("192.168.1.1/24")
hostname = device_info("192.168.1.18")
print(hostname)

