import scapy.all as scapy
import socket
import config

def collect_vendor_mac():
    vendor_file = open("vendor_id.txt", encoding="utf-8")
    data = vendor_file.read()
    data_to_list = data.split("\n")
    mac_identifiers = {}
    for line in data_to_list:
        split_line = line.split("\t")
        if len(split_line) > 1:
            mac_identifiers[split_line[0].lower()] = split_line[1]
    return mac_identifiers

def arp_request(ip_address):
    arp_packet = scapy.ARP(pdst=ip_address)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    full_packet = broadcast / arp_packet
    answered = scapy.srp(full_packet, timeout=1, iface=config.ntwrk_adapter, verbose=False)[0]
    mac_identifiers = collect_vendor_mac()
    
    print("--------------------------------------------------------------\nIP\t\t\tMAC\t\t\tVendor\n--------------------------------------------------------------")
    for host in answered:
        current_mac = host[1].hwsrc.replace(':', '').lower()
        oui = current_mac[0:6]
        vendor = mac_identifiers.get(oui, "UNKNOWN")
        print(host[1].psrc + "\t\t" + host[1].hwsrc + "\t" + vendor)

def device_info(host):
    try:
        hostname = socket.gethostbyaddr(host)[0]
        return hostname
    except socket.herror as e:
        print(f"Could not resolve the hostname for {host}. Error message: {e}")

arp_request(config.ip_subnet)
# hostname = device_info("10.0.0.32")

