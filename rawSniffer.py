#!/usr/bin/python

import socket
import struct
import binascii

# creating a rawSocket for communications
# PF_SOCKET (packet interface), SOCK_RAW (Raw socket) - htons (protocol) 0x08000 = IP Protocol
rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

# read a packet with recvfrom method
pkt = rawSocket.recvfrom(2048) # tuple return

# Ethernet Header tuple segmentation
eHeader = pkt[0][0:14]

# parsing using unpack
eth_hdr = struct.unpack("!6s6s2s", eHeader) # 6 dest MAC, 6 host MAC, 2 ethType

# using hexify to convert the tuple value NBO into Hex format
binascii.hexlify(eth_hdr[0])
binascii.hexlify(eth_hdr[1])
binascii.hexlify(eth_hdr[2])

ipHeader = pkt[0][14:34]
ip_hdr = struct.unpack("!12s4s4s", ipHeader) # 12s represents Identification, Time to Live, Protocol | Flags, Fragment Offset, Header Checksum

print "Source IP address %s" % socket.inet_ntoa(ip_hdr[1]) # network to ascii convertion
print "Destination IP address %s" % socket.inet_ntoa(ip_hdr[2]) # network to ascii convertion

# unapck the TCP header (source and destination port numbers)
tcpHeader = pkt[0][34:54]
tcp_hdr = struct.unpack("!HH16s", tcpHeader)

print "Source Source Port: %s" % tcp_hdr[0]
print "Source Destination Port: %s" % tcp_hdr[1]