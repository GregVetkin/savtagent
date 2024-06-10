from psutil import net_if_addrs

addr = net_if_addrs()
for interface in addr:
    print(interface, "-->", addr[interface])