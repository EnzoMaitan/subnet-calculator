import SubnetCalculator as sc
import IpCalculator as ic


class SubnetListCalculator:
    subnet_calculator: sc
    available_subnets : int
    borrowed_bits: int

    def __init__(self, subnet_calculator, borrowed_bits, available_subnets):
        self.subnet_calculator = subnet_calculator
        self.borrowed_bits = borrowed_bits
        self.available_subnets = available_subnets

    def calculate_new_network_address(self, network):
        new_SID = ic.IpCalculator('.'.join(network))

        new_SID.convert_octects_to_binary();
        new_SID.calculate_decimal_ip()
        new_SID.get_ip_class()

        # Gets the current borrowed part
        borrowed_zone = ''.join(new_SID.ip_binary_octects_list)[new_SID.ip_class[3]:(new_SID.ip_class[3]+self.borrowed_bits)]

        # Adding + 1 to the borrowed part
        new_borrowed_zone = format(int(borrowed_zone,2) + 1,'0'+str(self.borrowed_bits)+'b')

        # Add the new borrowed zone to the rest of the IP
        new_SID.ipv4 = ''.join(new_SID.ip_binary_octects_list)[:new_SID.ip_class[3]] + new_borrowed_zone

        # Fill the host portion with Zeroes
        new_SID.ipv4 = new_SID.ipv4.ljust(32,'0')

        # Convert the binary IPV4 into a decimal dotted format
        first_octet = str(int(new_SID.ipv4[:8],2))
        second_octet = str(int(new_SID.ipv4[8:16],2))
        third_octet = str(int(new_SID.ipv4[16:24],2))
        fourth_octet = str(int(new_SID.ipv4[24:],2))
        new_SID.ipv4 = '.'.join([first_octet, second_octet, third_octet, fourth_octet])

        return new_SID.ipv4

    def calculate_all_subnets(self):
        print("Possible Networks / Showing "+ str(self.available_subnets))
        print("+-----------------+-----------------+-----------------+-------------------+")
        print("| Network Address | First Host IP   | Last Host Ip    | Broadcast Address |")
        print("+-----------------+-----------------+-----------------+-------------------+")

        network_ipv4 = ".".join(self.subnet_calculator.calculate_first_index())
        for x in range(0, self.available_subnets):

            new = ic.IpCalculator(network_ipv4)
            new.calculate_decimal_ip()
            new.convert_octects_to_binary()

            network_ipv4 = [str(i) for i in new.ip_decimal_octects_list]
            new_calculator = sc.SubnetCalculator(new, self.subnet_calculator.host_ip_mask)

            new_calculator.subnet_id = ''.join(new.ip_binary_octects_list)
            new_calculator.calculate_broadcast_address()
            new_calculator.calculate_first_host()
            new_calculator.calculate_last_host()
            new_calculator.calculate_decimal_values()

            print("| " + '.'.join(new_calculator.subnet_id_decimal).ljust(15) + " | " + '.'.join(
                new_calculator.first_host_decimal).ljust(15) + " | " + '.'.join(new_calculator.last_host_decimal).ljust(
                15) + " | " + '.'.join(new_calculator.broadcast_address_decimal).ljust(18) + "|")

            network_ipv4 = self.calculate_new_network_address(network_ipv4)
        print("+-----------------+-----------------+-----------------+-------------------+")



