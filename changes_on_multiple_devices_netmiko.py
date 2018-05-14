from netmiko
import ConnectHandler

##Below lines will take device ip, usernames and passwords to authenticate into the device##

Device_A = {'device_type':'cisco_ios', 'ip':'10.2.0.1', 'username':'', 'password':'pwd'}
Device_B = {'device_type':'cisco_ios', 'ip':'10.32.0.1', 'username':'', 'password':'pwd'}
Device_C = {'device_type':'cisco_ios', 'ip':'192.168.2.63', 'username':'', 'password':'pwd'}
Device_D = {'device_type':'cisco_ios', 'ip':'192.168.1.1', 'username':'', 'password':'pwd'}

##Below line passes the details into a variable##

firewall = [Device_A,Device_B,Device_C,Device_D]

##Below lines will pass the config commands into the device and execute them on all the devices##

config_commands = [
 'no username test'
]

for device in firewall:

 net_connect = ConnectHandler(**device)

 output = net_connect.send_config_set (config_commands)
# output = net_connect.send_command ("wr")

 print (output)

