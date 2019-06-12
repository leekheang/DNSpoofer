#!usr/bin/env python

import netfilterqueue

def process_packet(packet):
    print(packet)
    packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(2, process_packet)
queue.run()

# from netfilterqueue import NetfilterQueue

# def print_and_accept(pkt):
#     print(pkt)
#     pkt.accept()

# nfqueue = NetfilterQueue()
# nfqueue.bind(10, print_and_accept)
# try:
#     nfqueue.run()
# except KeyboardInterrupt:
#     print('')

# nfqueue.unbind()