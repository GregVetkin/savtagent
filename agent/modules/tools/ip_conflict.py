import concurrent.futures
import subprocess
from psutil                 import net_if_addrs
from scapy.all              import ARP, Ether, srp
from socket                 import AddressFamily
from typing                 import Dict




def ip_is_taken(ip: str) -> bool:
    """Сканировать сеть и проверить, занят ли IP-адрес."""
    ip_prefix   = '.'.join(ip.split('.')[:-1]) + '.0/24'
    arp_request = ARP(pdst=ip_prefix)
    broadcast   = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    for sent, received in answered_list:
        if received.psrc == ip and received.hwsrc != Ether().src:
            return True
    return False



def _get_interfaces_addresses_ipv4() -> Dict[str, Dict[str, None]]:
    interfaces  = net_if_addrs()
    result      = {interface: {} for interface in interfaces}
    for interface in interfaces:
        for connection in interfaces[interface]:
            if connection.family == AddressFamily.AF_INET:
                result[interface][connection.address] = None
    return result



def check_ip_collisions() -> Dict[str, Dict[str, bool]]:
    interfaces = _get_interfaces_addresses_ipv4()
    for interface in interfaces:
        for address in interfaces[interface]:
            interfaces[interface][address] = ip_is_taken(address)
    return interfaces



def check_ip_collisions_threads() -> Dict[str, Dict[str, bool]]:
    interfaces  = _get_interfaces_addresses_ipv4()
    ip_list     = [(iface, ip) for iface, ips in interfaces.items() for ip in ips]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(lambda x: (x[0], x[1], ip_is_taken(x[1])), ip_list))

    for iface, ip, status in results:
        interfaces[iface][ip] = status

    return interfaces



def ip_duplication(ip, interface):
    """
    Linux package required: 'iputils-arping'  (sudo apt-get install iputils-arping).
    The package is present in the repository of the Astra-Linux installation disk.

    :return:  True - there is a duplicate, False - there is not
    """

    command = f'sudo arping -D -w 1 -I {interface} {ip}'
    process = subprocess.Popen([command], shell=True, stdout=subprocess.PIPE)
    bash_result = process.wait()

    if bash_result == 0:
        return False

    elif bash_result == 1:
        return True


def threading_ip_duplication():
    interfaces = _get_interfaces_addresses_ipv4()
    ip_list     = [(iface, ip) for iface, ips in interfaces.items() for ip in ips]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(lambda x: (x[0], x[1], ip_duplication(x[1], x[0])), ip_list))

    for iface, ip, status in results:
        interfaces[iface][ip] = status

    return interfaces


if __name__ == '__main__':
    pass