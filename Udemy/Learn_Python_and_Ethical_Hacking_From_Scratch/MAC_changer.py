# Create a script that allows the user to change the MAC address of a chosen interface

import subprocess
import optparse
import re

mac_regex = re.compile(r'([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F])')

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option('-i', '--interface', dest='interface', help='Interface to change it\'s MAC Address')
    parser.add_option('-m', '--mac', dest='mac', help='The new MAC Address')
    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error("Please specify an interface. Use --help for more info.")
    elif not options.mac:
        parser.error("Please specify a MAC Address. Use --help for more info.")
    return options

def change_mac_address(interface, mac_address):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
    subprocess.call(["ifconfig", interface, "up"])

def get_address(interface):
    ifconfig_result = subprocess.check_output(['ifconfig', interface])
    match = mac_regex.search(str(ifconfig_result))
    if match:
        return match[0]
    print("Could not read the MAC Address.")

options = get_arguments()

INTERFACE = options.interface
MAC = options.mac

mac_format_okay = mac_regex.search(MAC)
if mac_format_okay:
    change_mac_address(INTERFACE, MAC)
    if MAC == get_address(INTERFACE):
        print(f"MAC Address was successfully changed to {MAC}")
    else:
        print("Unable to change MAC Address.")
else:
    print("Incorrect MAC Address format.")
