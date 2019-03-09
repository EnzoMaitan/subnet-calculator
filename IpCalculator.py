import re

class IpCalculator:
    ip_decimal_octects_list = None
    ip_binary_octects_list = None
    ipv4 = None
    ip_class = None

    def __init__(self, ipv4):

        # checks if the IPV4 received is valid
        ip_valid_format = '\d{0,3}[0-255]\.\d{0,3}[0-255]\.\d{0,3}[0-255]\.\d{0,3}[0-255]'
        if not re.match(ip_valid_format, ipv4):
            raise ValueError("Invalid Ip format")

        self.ipv4 = ipv4
        self.calculate_decimal_ip()
        self.convert_octects_to_binary()
        self.get_ip_class()

    # returns the decimal IP as an int list separated in 4 octets
    # Example: [000,000,000,000]
    def calculate_decimal_ip(self):
        self.ip_decimal_octects_list = [int(x) for x in self.ipv4.split('.')]

    # returns the binary IP as string list separated in 4 octets
    # Example: ['00000000', '00000000', '00000000', '00000000']
    def convert_octects_to_binary(self):
        # formats the ip (string format) to a list of 4 binary octets
        self.ip_binary_octects_list = [format(int(x), '08b') for x in self.ipv4.split('.')]

    # returns the Class letter, binary mask, decimal mask, and mask bits
    def get_ip_class(self):

        # selects the first octet from the ip
        first_octet = self.ip_decimal_octects_list[0]

        if 1 <= first_octet <= 126:
            self.ip_class = ['A', 11111111000000000000000000000000, '255.0.0.0', 8]
        elif 128 <= first_octet <= 191:
            self.ip_class = ['B', 11111111111111110000000000000000, '255.255.0.0', 16]
        elif 192 <= first_octet <= 223:
            self.ip_class = ['C', 11111111111111111111111100000000, '255.255.255.0', 24]
        else:
            self.ip_class = ['D']

    # converts all binary values into booleans inside of the list
    def convert_binarylist_to_booleanslist(self):
        booleanslist = []
        for x in self.ip_binary_octects_list:
            for y in x:
                booleanslist.append(int(y) == 1)
        return booleanslist
