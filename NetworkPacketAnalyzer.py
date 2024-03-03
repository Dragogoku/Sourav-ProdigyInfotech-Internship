from scapy.all import *

def sniff_packets(interface):
    """
    A packet sniffer that prints out the IP address, protocol, payload data, and source.

    :param interface: The network interface to sniff packets from
    """
    packets = sniff(filter="tcp", iface=interface)
    for packet in packets:
        ip_packet = packet.getlayer(IP)
        payload = str(packet.getlayer(Raw))
        print(f"IP address: {ip_packet.src}, Protocol: {ip_packet.proto}, Payload: {payload}, Source: {interface}")

if __name__ == "__main__":
    sniff_packets("eth0") 