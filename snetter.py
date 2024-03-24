#!/usr/bin/python3

# a program to quickly calculate useful subnetting info
# this program takes an IP address with CIDR notation and provides the user with...
# the IP address
# the subnet mask
# the network (subnet) address
# the broadcast address
# the first IP available for a host
# the last IP available for a host

# by puzz00

import optparse
from subnet_class import SubnetHelper

parser = optparse.OptionParser()
parser.add_option("-c", "--cidr", action="store", dest="cidr",
                  help="IP address with CIDR notation - for example 10.50.96.25/23")

options, args = parser.parse_args()

# let the user know they need to specify an IP address with CIDR notation if they do not
if not options.cidr:
    print("\n[**] Use the -c or --cidr flag to specify an IP address with CIDR notation")
    print("\n[**] Example usage...")
    print("\n[**] python snetter.py -c 10.50.96.25/23")
    exit()

# instantiate a SubnetHelper object
sub = SubnetHelper()

# calculate the necessary data
ip, mask, nw, bc, fh, lh = sub.find_networks(options.cidr)

# print the output to the user
line = "\n------------------------"
print(line)
print("\nIP Address:\t\t\t{}.{}.{}.{}".format(ip[0], ip[1], ip[2], ip[3]))
print("\nSubnet Mask:\t\t\t{}.{}.{}.{}".format(mask[0], mask[1], mask[2], mask[3]))
print("\nNetwork Address:\t\t{}.{}.{}.{}".format(nw[0], nw[1], nw[2], nw[3]))
print("\nBroadcast Address:\t\t{}.{}.{}.{}".format(bc[0], bc[1], bc[2], bc[3]))
print("\nFirst Host:\t\t\t{}.{}.{}.{}".format(fh[0], fh[1], fh[2], fh[3]))
print("\nLast Host:\t\t\t{}.{}.{}.{}".format(lh[0], lh[1], lh[2], lh[3]))
print(line)
print()
