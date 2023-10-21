# MAID - Map, Analyze, Intrude, Dismantle

MAID is a network penetration tool that follows a step-by-step approach of Map, Analyze, Intrude, Dismantle to identify vulnerabilities and exploit them to gain access to a target network. It helps security professionals test and strengthen their network's security.

## Requirements
- Python 3
- scapy
- config
- argparse
- 
## Usage
To run the program, you need to specify the target IP or IP range as an argument using the -t or --target option. For example:

`python arp_scanner.py -t 192.168.1.0/24`

This will scan the entire subnet of 192.168.1.0/24 and display the results in a table format.

## Output
The output of the program will look something like this:

------------------------------------------------------------------------------------------------------------
IP              MAC                     Vendor                                  Hostname
------------------------------------------------------------------------------------------------------------
192.168.1.1     00:11:22:33:44:55       Cisco Systems Inc                       router.example.com
192.168.1.2     66:77:88:99:aa:bb       Dell Inc                                laptop.example.com
192.168.1.3     cc:dd:ee:ff:00:11       Apple Inc                               iphone.example.com
