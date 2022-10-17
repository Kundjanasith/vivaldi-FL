import socket
import utils
import sys 

source_ip = sys.argv[1]

ips = open('ip.txt','r')

for ip in ips:
    dest_ip = ip.split('\n')[0]
    output = open('data/FROM_%s_TO_%s.txt'%(source_ip,dest_ip),'w')
    print(source_ip, dest_ip)
    for e in range(10):
        bw = utils.client(dest_ip)
        print(e,bw)
        output.write(str(bw)+'\n')
    output.close() 