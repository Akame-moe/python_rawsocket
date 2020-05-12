#!/usr/bin/python

import socket
import struct

# creating a rawSocket for communications
# PF_SOCKET (packet interface), SOCK_RAW (Raw socket) - htons (protocol) 0x08000 = IP Protocol
rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

# deciding interface - packet sniffing and then injection
rawSocket.bind(("eth0", socket.htons(0x0800)))

# create a ethernet packet
packet = struct.pack("!6s6s2s", '\xaa\xaa\xaa\xaa\xaa\xaa', '\xbb\xbb\xbb\xbb\xbb\xbb', '\x08\x00')
# 6 dest address, 6 source address and 2 for ethtype = IP

# inject a random string after the header
rawSocket.send(packet + "Marico el que lo lea")