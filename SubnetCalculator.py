import IpCalculator as ic
import SubnetListCalculator as slc


class SubnetCalculator:
    host_ip: ic
    host_ip_mask = ic

    borrowed_bits = 0
    available_subnets: int
    subnet_id: str
    first_host: str
    last_host: str
    available_hosts: int
    host_bits: int
    broadcast_address: str
    subnet_index: int

    subnet_id_decimal = None
    broadcast_address_decimal = None
    first_host_decimal = None
    last_host_decimal = None

    def __init__(self, host_ip, host_ip_mask):
            # Host IP in IpCalculator format
            self.host_ip = host_ip

            # Host IP Mask in IpCalculator format
            self.host_ip_mask = host_ip_mask

    def print_subnets_list(self):
        sl = slc.SubnetListCalculator(self,self.borrowed_bits, self.available_subnets)
        sl.calculate_all_subnets()

    def calculate_all_values(self):
        self.calculate_borrowed_bits()
        self.calculate_available_subnets()
        self.calculate_subnet_id()

        self.calculate_broadcast_address()
        self.calculate_first_host()
        self.calculate_last_host()
        self.calculate_host_bits()
        self.calculate_available_hosts()
        self.calculate_decimal_values()
        self.calculate_subnet_index()

    def calculate_first_index(self):
        # gets the default network address
        network_address=''.join(self.host_ip_mask.ip_binary_octects_list).count("1") - self.borrowed_bits
        # returns the network address
        return  [str(x) for x in self.convert_binary_to_decimal_string(self.subnet_id[:network_address].ljust(32,"0"))]

    def calculate_subnet_id(self):
        c = []
        # Convert given host ip to a list of booleans
        given_host_ip_boolean = self.host_ip.convert_binarylist_to_booleanslist()

        # Convert given subnet mask ip to a list of booleans
        given_subnet_mask_boolean = self.host_ip_mask.convert_binarylist_to_booleanslist()

        # result of (AND) logic operator for all bits inside the ip
        for index, v in enumerate(given_host_ip_boolean):
            c.append(given_host_ip_boolean[index] * given_subnet_mask_boolean[index])

        # assigns result in the subnet_id as a string
        self.subnet_id = ''.join([str(x) for x in c])

    def format_binary_8bit(self, value):
        a = [value[i:i + 8] for i in range(0, len(value), 8)]
        return a

    def calculate_borrowed_bits(self):
        self.borrowed_bits = str(
            int(''.join(self.host_ip_mask.ip_binary_octects_list)) - int(self.host_ip.ip_class[1])).count('1')

    def calculate_available_subnets(self):
        if self.borrowed_bits > 0:
            self.available_subnets = 2 ** self.borrowed_bits
        else:
            self.available_subnets = "Not applicable"

    def calculate_broadcast_address(self):
        # removes the non-mask digits of the IP
        to_remove = 32 - ''.join(self.host_ip_mask.ip_binary_octects_list).count("0")

        sid = self.subnet_id[:to_remove]

        # add 1 to the remaining non-mask digits
        sid = sid.ljust(32, '1')

        self.broadcast_address = sid

    def calculate_first_host(self):
        self.first_host = str(int(self.subnet_id) + 1).zfill(32)

    def calculate_last_host(self):
        self.last_host = str(int(self.broadcast_address) - 1).zfill(32)

    def calculate_host_bits(self):
        self.host_bits = 32 - (self.borrowed_bits + self.host_ip.ip_class[3])

    def calculate_available_hosts(self):
        self.available_hosts = 2 ** self.host_bits - 2

    def calculate_decimal_values(self):
        self.subnet_id_decimal = [str(x) for x in self.convert_binary_to_decimal_string(self.subnet_id)]
        self.broadcast_address_decimal = [str(x) for x in self.convert_binary_to_decimal_string(self.broadcast_address)]
        self.first_host_decimal = [str(x) for x in self.convert_binary_to_decimal_string(str(self.first_host))]
        self.last_host_decimal = [str(x) for x in self.convert_binary_to_decimal_string(str(self.last_host))]

    def convert_binary_to_decimal_string(self, binary_string):
        a = [binary_string[i:i + 8] for i in range(0, len(binary_string), 8)]
        a = [int(x, 2) for x in a]
        return a

    def calculate_subnet_index(self):
        if self.borrowed_bits > 0:
            self.subnet_index = int(
                ''.join(self.host_ip.ip_binary_octects_list)[self.host_ip.ip_class[3]:(self.host_ip.ip_class[3] + self.borrowed_bits)], 2)
        else:
            self.subnet_index = "Not applicable"
