ip = input().strip()
if len(ip.split('.')) == 4: # is IPv4
    print('.'.join(ip.split('.')[::-1])+'.in-addr.arpa.')
else:
    ip = ip.replace('::', ':0:'*(8-len([i for i in ip.split(':') if i])))
    for _ in range(3): ip = ip.replace('::', ':')
    ip = ip.strip(':').split(':')
    assert len(ip) == 8
    for i in range(8): ip[i] = '.'.join(ip[i].zfill(4)[::-1])
    print('.'.join(ip[::-1])+'.ip6.arpa.')