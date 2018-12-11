#Rest-API did not have Documentation on how to configure ASA routing protocols.
from netmiko import ConnectHandler

#ASA = {'username': 'linux', 'ip': '192.168.1.103', 'password': 'linux', 'device_type': 'cisco_asa'}
ASA = {'username': 'nopass', 'ip': '192.168.1.103', 'use_keys': True, 'key_file': '/root/.ssh/id_rsa', 'device_type': 'cisco_asa'}
net_connect = ConnectHandler(**ASA)
config_commands = [' router eigrp 1', 'network 10.1.1.1 255.255.255.252', 'network 10.12.12.0 255.255.255.252', 'network 10.20.20.20 255.255.255.255' , 'route null0 10.20.20.20 255.255.255.255 254']
#Host route is to advertise Web Outside into EIGRP
output = net_connect.send_config_set(config_commands)
print(output)
