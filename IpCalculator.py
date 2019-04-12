import re


class IpCalculator:
    ip_decimal_octects_list = None
    ip_binary_octects_list = None
    ipv4 = None
    ip_class = None

    def __init__(self, ipv4):
        # checks if the IPV4 received is valid by using REGEX
        ip_valid_format_regex = '^(([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))$'
        if not re.match(ip_valid_format_regex, ipv4):
            raise ValueError("Invalid Ip format")
        self.ipv4 = ipv4

    def calculate_decimal_ip(self):
        """
        returns the decimal IP as an int list separated in 4 octets

        :return: Example: [000,000,000,000]
        """

        self.ip_decimal_octects_list = [int(x) for x in self.ipv4.split('.')]

    def convert_octects_to_binary(self):
        """
        Converts the binary IP as string list separated in 4 octets
        :return: Example: ['00000000', '00000000', '00000000', '00000000']
        """
        # formats the ip (string format) to a list of 4 binary octets

        self.ip_binary_octects_list = [format(int(x), '08b') for x in self.ipv4.split('.')]

    def get_ip_class(self):
        """
        returns the Class letter, binary mask, decimal mask, and mask bits
        :return: [0] Class letter, [1] binary mask, [2] decimal mask, [3] and mask bits
        """
        # selects the first octet from the ip
        first_octet = self.ip_decimal_octects_list[0]

        if 1 <= first_octet <= 126:
            self.ip_class = ['A', 11111111000000000000000000000000, '255.0.0.0', 8]
        elif 128 <= first_octet <= 191:
            self.ip_class = ['B', 11111111111111110000000000000000, '255.255.0.0', 16]
        elif 192 <= first_octet <= 223:
            self.ip_class = ['C', 11111111111111111111111100000000, '255.255.255.0', 24]
        else:
            raise Exception("Ip Classes D and E are not supported")

    def convert_binarylist_to_booleanslist(self):
        """
        converts all binary values into booleans inside of the list
        :return: Ex: [True, True, False, False]
        """
        booleanslist = []
        for x in self.ip_binary_octects_list:
            for y in x:
                booleanslist.append(int(y) == 1)
        return booleanslist
