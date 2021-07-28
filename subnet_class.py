#!/usr/bin/python3

# class for finding subnet information
# by puz00

class SubnetHelper:
    # use a constructor to define what is needed in this class
    def __init__(self):
        self.mask_1 = ["1", "2", "3", "4", "5", "6", "7", "8"]
        self.mask_2 = ["9", "10", "11", "12", "13", "14", "15", "16"]
        self.mask_3 = ["17", "18", "19", "20", "21", "22", "23", "24"]
        self.mask_4 = ["25", "26", "27", "28", "29", "30", "31", "32"]
        self.decimal = [128, 192, 224, 240, 248, 252, 254, 255]
        self.networks = [2, 4, 8, 16, 32, 64, 128, 256]
        self.hosts = [128, 64, 32, 16, 8, 4, 2, 1]
        self.ip_address = []
        self.subnet_mask = []
        self.network_address = []
        self.broadcast_address = []
        self.first_host = []
        self.last_host = []

    def populate_boundaries(self, host, nw):
        subnet_boundaries = [0]
        boundary = int(256 / nw)
        i = 0
        while i < 256:
            new_boundary = i + boundary
            subnet_boundaries.append(new_boundary)
            i += host
        return subnet_boundaries

    def mask_one(self, cidr, first):
        for i in range(8):
            if self.mask_1[i] == cidr:
                pointer = i
        dec = self.decimal[pointer]
        host = self.hosts[pointer]
        nw = self.networks[pointer]
        self.subnet_mask.append(dec)
        self.subnet_mask.append(0)
        self.subnet_mask.append(0)
        self.subnet_mask.append(0)
        # populate the subnet boundaries list
        subnet_boundaries = self.populate_boundaries(host, nw)
        length = len(subnet_boundaries)
        # find the lower and upper subnet boundaries
        for i in range(length):
            if (first >= subnet_boundaries[i]) and (first <= subnet_boundaries[i + 1]):
                lower = subnet_boundaries[i]
                upper = subnet_boundaries[i + 1]
        return lower, upper

    def mask_two(self, cidr, second):
        for i in range(8):
            if self.mask_2[i] == cidr:
                pointer = i
        dec = self.decimal[pointer]
        host = self.hosts[pointer]
        nw = self.networks[pointer]
        self.subnet_mask.append(255)
        self.subnet_mask.append(dec)
        self.subnet_mask.append(0)
        self.subnet_mask.append(0)
        # populate the subnet boundaries list
        subnet_boundaries = self.populate_boundaries(host, nw)
        length = len(subnet_boundaries)
        # find the lower and upper subnet boundaries
        for i in range(length):
            if (second >= subnet_boundaries[i]) and (second <= subnet_boundaries[i + 1]):
                lower = subnet_boundaries[i]
                upper = subnet_boundaries[i + 1]
        return lower, upper

    def mask_three(self, cidr, third):
        for i in range(8):
            if self.mask_3[i] == cidr:
                pointer = i
        dec = self.decimal[pointer]
        host = self.hosts[pointer]
        nw = self.networks[pointer]
        self.subnet_mask.append(255)
        self.subnet_mask.append(255)
        self.subnet_mask.append(dec)
        self.subnet_mask.append(0)
        # populate the subnet boundaries list
        subnet_boundaries = self.populate_boundaries(host, nw)
        length = len(subnet_boundaries)
        # find the lower and upper subnet boundaries
        for i in range(length):
            if (third >= subnet_boundaries[i]) and (third <= subnet_boundaries[i + 1]):
                lower = subnet_boundaries[i]
                upper = subnet_boundaries[i + 1]
        return lower, upper

    def mask_four(self, cidr, fourth):
        for i in range(8):
            if self.mask_4[i] == cidr:
                pointer = i
        dec = self.decimal[pointer]
        host = self.hosts[pointer]
        nw = self.networks[pointer]
        self.subnet_mask.append(255)
        self.subnet_mask.append(255)
        self.subnet_mask.append(255)
        self.subnet_mask.append(dec)
        # populate the subnet boundaries list
        subnet_boundaries = self.populate_boundaries(host, nw)
        length = len(subnet_boundaries)
        # find the lower and upper subnet boundaries
        for i in range(length):
            if (fourth >= subnet_boundaries[i]) and (fourth <= subnet_boundaries[i + 1]):
                lower = subnet_boundaries[i]
                upper = subnet_boundaries[i + 1]
        return lower, upper

    def get_networks(self, lower, upper):
        i = 0
        for b in self.subnet_mask:
            if b == 255:
                self.network_address.append(self.ip_address[i])
            elif b == 0:
                self.network_address.append(0)
            else:
                self.network_address.append(lower)
            i+=1
        j = 0
        for b in self.subnet_mask:
            if b == 255:
                self.broadcast_address.append(self.ip_address[j])
            elif b == 0:
                self.broadcast_address.append(255)
            else:
                self.broadcast_address.append(upper - 1)
            j += 1
        k = 0
        for b in self.subnet_mask:
            if b == 255:
                self.first_host.append(self.ip_address[k])
            elif (b == 0) and (k != 3):
                self.first_host.append(0)
            elif (b == 0) and (k == 3):
                self.first_host.append(1)
            elif (b != 255) and (b != 0) and (k != 3):
                self.first_host.append(lower)
            elif (b != 255) and (b !=0) and (k == 3):
                self.first_host.append(lower + 1)
            k += 1
        l = 0
        for b in self.subnet_mask:
            if b == 255:
                self.last_host.append(self.ip_address[l])
            elif (b == 0) and (l != 3):
                self.last_host.append(255)
            elif (b == 0) and (l == 3):
                self.last_host.append(254)
            elif (b != 255) and (b != 0) and (l != 3):
                self.last_host.append(upper - 1)
            elif (b != 255) and (b != 0) and (l == 3):
                self.last_host.append(upper - 2)
            l += 1
        return

    def find_networks(self, cidr_notation):
        # splits out the CIDR notation from the IP address
        ip = cidr_notation.split("/")[0]
        cidr = cidr_notation.split("/")[1]
        first = int(ip.split(".")[0])
        second = int(ip.split(".")[1])
        third = int(ip.split(".")[2])
        fourth = int(ip.split(".")[3])
        self.ip_address.append(first)
        self.ip_address.append(second)
        self.ip_address.append(third)
        self.ip_address.append(fourth)

        # this if block works for CIDR notation from /1 to /8 inclusive
        if cidr in self.mask_1:
            # get the subnet boundaries needed
            lower, upper = self.mask_one(cidr, first)
            # call the method which will calculate the subnetting information needed
            self.get_networks(lower, upper)
        # this elif block works for CIDR notation from /9 to /16 inclusive
        elif cidr in self.mask_2:
            # get the subnet boundaries needed
            lower, upper = self.mask_two(cidr, second)
            # call the method which will calculate the subnetting information needed
            self.get_networks(lower, upper)
        # this elif block works for CIDR notation from /17 to /24 inclusive
        elif cidr in self.mask_3:
            # get the subnet boundaries needed
            lower, upper = self.mask_three(cidr, third)
            # call the method which will calculate the subnetting information needed
            self.get_networks(lower, upper)
        # this elif block works for CIDR notation from /25 to /32 inclusive
        elif cidr in self.mask_4:
            # get the subnet boundaries needed
            lower, upper = self.mask_four(cidr, fourth)
            # call the method which will calculate the subnetting information needed
            self.get_networks(lower, upper)
        # return the data requested from the user
        return self.ip_address, self.subnet_mask, self.network_address, self.broadcast_address, self.first_host, self.last_host




