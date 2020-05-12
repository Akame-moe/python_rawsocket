> code from https://gist.github.com/davidlares/e841c0f9d9b31f3cd8859575d061c467
> article from https://medium.com/@davidlares/raw-sockets-with-python-sniffing-and-network-packet-injections-486043061bd5

---------------

### Using Raw sockets
This element provides a way to bypass the whole network stack traversal of a packet and deliver directly to an application. There are multiple ways to create raw sockets. For this time we are going to use the PF_PACKET Interface.


On a regular socket programming, we need to create a TCP / UDP server where network card will pass the packet up to IP Stack (IP Processing) that will be received in the client application.

Let’s make it simple, by using Raw Sockets, we can generate a quick Shortcut for the Network Stack.

Doing some memory flashback: The OSI model standardizes the communication functions of telecommunication of the computer system without regard to its underlying internal structure.

The OSI models consist of: (classified by the roles performed)
- User Land Application or Application Layer
- Socket Interface
- TCP/UDP processing
- IP Processing
- Protocol family handling routines (LPF) = from Raw Socket to Application
- Network card driver

It is a software interface to send/receive packets at layer 2 of the OSI (device drive) All packets received will be complete with all headers and data All packets sent will be transmitted without modification by the kernel to the medium Supports filtering using Berkley Packet Filtering (BPF)

### Understanding Packet Headers

To make this explanation a little bit easier, we have to make sure that the Ethernet encapsulates everything. (I think this is not 100% accurate)

Ethernet (encapsulates) -> IP -> TCP -> Application (layer approach)

The first 14 bytes represent the Ethernet Header, specifically the Ethernet Packet Data
​
0–6 = EthDhost (Destination MAC Address)

6–11 = EthShost (Source MAC Address)
​
12–14 = EthType (IP or another Inner protocol being used)

Following bytes goes to the IP headers, then the TCP and then the Application

0–3 = Version 4–7 = IHL 8–15 = Type of Service 16–31 = Total length

And other information like Identification, Time to Live, Protocol, Flags, Fragment Offset, Header Checksum, Source Address, Destination Address, Options, Padding, etc

Approximately represents 20 bytes in total

The order for parsing data will be the same for sending and receiving.

### Extracting Binary Data into Variables

When data is sent over a network is actually gets converted to network byte order: the Big Endian format

When we send data we have to ensure that the format is NBO (Big Endian), this is unpacked and used it inside the application we need to ensure that data conversion occurs accordingly using the struct.unpack(), this last one returns tuple format the information of the headers that you will process to retrieve the string understandable value.

You can use raw sockets if you have the right permissions or root user, for rawSniffer.py (should run as root)

Both subtopics: Understanding packet headers and Extracting binary data into variables represents the sniffing role on raw sockets.

### Packet Injection with Raw Sockets

This presents the ability to inject raw packets into the network, obviously, you can estimate responses from the network.

The following codes are intended to be used for standalone tests, as a matter of fact, Raw sockets aren’t quite portable, is kinda difficult to construct packets using raw sockets. This is not scalable at all.

For traceability, you can use tcpdump or any other tool for Traffic analysis like Wireshark.

tcpdump -i eth0 -vv -XX

You can check code examples written in Python for Raw Sniffers and Raw packet injection on my gist page:

Raw Sockets with Python: Sniffing and network packet injections: http://bit.ly/32i793l
