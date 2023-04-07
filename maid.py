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
    
    print("------------------------------------------------------------------------------------------------------------\nIP\t\tMAC\t\t\tVendor\t\t\t\t\tHostname\n------------------------------------------------------------------------------------------------------------")
    for host in answered:
        ip = host[1].psrc
        mac = host[1].hwsrc
        hostname = device_info(ip)
        current_mac = host[1].hwsrc.replace(':', '').lower()
        oui = current_mac[0:6]
        vendor = mac_identifiers.get(oui, "UNKNOWN")
        # print(ip + "\t\t" + mac + "\t" + vendor + "\t\t" + str(hostname))
        print(ip.ljust(16) + mac.ljust(24) + vendor.ljust(40) + str(hostname))

def device_info(host):
    try:
        hostname = socket.gethostbyaddr(host)[0]
        if hostname:
            return hostname
    except socket.herror:
        pass
    return "Could not resolve hostname"

arp_request(config.ip_subnet)