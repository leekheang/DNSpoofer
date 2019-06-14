# DNSpoofer
DNSpoofer (MITM)

+ IPTABLES 
RUN Program 
cmd iptables -I OUTPUT -j NFQUEUE --queue-num 0
cmd iptables -I INPUT -j NFQUEUE --queue-num 0
Generate a DNS request (see respone)
ping -c 1 www.nsm.com (sent request)