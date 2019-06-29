# Create a script that allows the user to change the MAC address of a chosen interface

import subprocess
import re

def change_mac_address(interface, mac_address):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
    subprocess.call(["ifconfig", interface, "up"])


INTERFACE = input("Interface: ")
MAC = input("MAC Address: ")

mac_regex = re.compile(r'^([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F])$')
match = mac_regex.search(MAC)
if match:
    change_mac_address(INTERFACE, MAC)
else:
    print("Sorry, incorrect MAC Address format.")
