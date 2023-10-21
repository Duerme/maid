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

![](https://ibb.co/Z2xsG2d)
